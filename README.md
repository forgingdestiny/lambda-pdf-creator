# Lambda PDF Creator

![988C3CB4-20C0-41C4-87E6-7430A16BFA1A](https://github.com/forgingdestiny/lambda-pdf-creator/assets/595530/d314f8b7-3812-4904-b4f5-d4025fca0b6b)


This project includes an AWS Lambda function that generates a PDF using ReportLab and uploads it to an S3 bucket.

## Directory Structure

```
/lambda-pdf-creator
├── src/
│   ├── main.py
│   └── requirements.txt
├── templates/
│   └── cloudformation-template.yml
├── package/
├── .gitignore
├── README.md
├── LICENSE
└── serverless.yml
```

## Setup

### Prerequisites

- AWS CLI already configured with Administrator permission
- [NodeJS 12.x installed](https://nodejs.org/en/download/)
- [Serverless Framework installed](https://serverless.com/framework/docs/getting-started/)

### Installation

1. **Install required Python packages**

In the `src/` directory, run:

```bash
pip install -r requirements.txt -t package/
```

This command installs the required Python packages in the `package/` directory.

2. **Package the Lambda function**

In the `src/` directory, run:

```bash
cp main.py package/
```

Then navigate to the `package/` directory and run:

```bash
zip -r ../pdf-lambda.zip .
```

This command packages the Python script and the dependencies into a ZIP file `my-lambda.zip`.

3. **Upload the ZIP file to S3**

Upload the `pdf-lambda.zip` file to your S3 bucket.

4. **Deploy the CloudFormation Stack**

In the `templates/` directory, run:

```bash
aws cloudformation deploy --template-file ./cloudformation-template.yml --stack-name MyLambdaStack --capabilities CAPABILITY_IAM
```

This command deploys the CloudFormation stack.

## Usage

After the CloudFormation stack is deployed, you can trigger the Lambda function to generate a PDF and upload it to the S3 bucket.

## Updating the Lambda function

To update the code of the Lambda function, repeat the packaging and upload steps, then update the stack using the same CloudFormation command.

## Troubleshooting

Logs for the Lambda function are stored in CloudWatch. If the function is not behaving as expected, check the CloudWatch logs for errors.

## Cleanup

To delete the CloudFormation stack and all associated resources, run:

```bash
aws cloudformation delete-stack --stack-name MyLambdaStack
```

## Security

This function uses your AWS credentials to access resources. Keep your AWS credentials confidential to prevent unauthorized access to your AWS account. The provided CloudFormation template includes an IAM role that the Lambda function assumes when it is executed. This role has full S3 and CloudWatch permissions. For a production environment, you should limit these permissions to only what the function needs to perform its tasks.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
