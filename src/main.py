from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import boto3
import io

def create_pdf(file_name):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)

    # Define S3
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'  # replace with your bucket name

    # Download image file from S3 to local storage
    with open('/tmp/background.png', 'wb') as file:
        s3.download_fileobj(bucket_name, 'onboard_pdf_background.png', file)

    # Add a full-width background image
    img_path = "/tmp/background.png"  # Temporary local path to your image file

    # Assuming resolution is 72 PPI, convert inches to pixels for width and height
    width, height = int(8.5 * 72), int(11 * 72)
    c.drawImage(img_path, 0, 0, width=width, height=height)

    # Set the font for the next operation
    c.setFont('Helvetica-Bold', 14)

    # Create a title and save the state
    c.drawString(10, 750, "Title")
    c.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    
    # Save the buffer content (the PDF) to an S3 bucket
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket_name, file_name).put(Body=packet)

def lambda_handler(event, context):
    file_name = 'test.pdf'
    create_pdf(file_name)
    
    # create presigned URL
    s3_client = boto3.client('s3')
    response = s3_client.generate_presigned_url('get_object', Params={'Bucket': 'your-bucket-name', 'Key': file_name})
    return {
        'statusCode': 200,
        'body': response
    }
