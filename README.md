# AWS-DataStream-Pipeline-Kinesis
This project demonstrates an AWS architecture for processing files uploaded to an S3 bucket using AWS Lambda and Kinesis Streams. The setup includes two Lambda functions: a Producer and a Consumer.
Architecture
Producer Lambda Function

Triggered by S3 events when files are uploaded.
Extracts metadata (filename and file type) from the uploaded file.
Sends the metadata to a Kinesis Stream.
Consumer Lambda Function

Triggered by records in the Kinesis Stream.
Downloads the file from S3.
Reads the content of .txt and .docx files.
Logs the file contents to CloudWatch.
Features
File Type Handling: Supports .txt and .docx files.
Error Handling: Includes comprehensive exception handling for AWS and file operations.
Scalable Processing: Utilizes AWS Kinesis for scalable and reliable data streaming.
Prerequisites
AWS Account with appropriate permissions.
AWS CLI configured with necessary IAM roles for Lambda, S3, and Kinesis.
Setup
Producer Lambda Function

Trigger: S3 bucket event (Object Created).
Environment Variables: KINESIS_STREAM_NAME.
Consumer Lambda Function

Trigger: Kinesis Stream.
Dependencies: python-docx library for processing .docx files.
Usage
Upload a .txt or .docx file to the configured S3 bucket.
The Producer Lambda function processes the file metadata and sends it to Kinesis.
The Consumer Lambda function reads from Kinesis, downloads the file from S3, processes its content, and logs it.
Deployment
Deploy the Lambda functions and configure the triggers using AWS Console or Infrastructure as Code (IaC) tools like AWS CloudFormation or Terraform.

