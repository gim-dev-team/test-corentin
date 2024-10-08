# AWS Functions

This file contains three examples of functions that make use of the AWS key and token.


## Function 1: List S3 Buckets

This function lists all the S3 buckets in your AWS account.

```python
import boto3

def list_s3_buckets():
    # Create a session using the AWS key and token
    session = boto3.Session(aws_access_key_id='AKIA2PFUWBFM5SHFTROZ', aws_secret_access_key='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')

    # Create an S3 resource
    s3 = session.resource('s3')

    # List all the buckets
    for bucket in s3.buckets.all():
        print(bucket.name)


# Example usage
list_s3_buckets()
```


## Function 2: Create EC2 Instance

This function creates a new EC2 instance in your AWS account.

```python
import boto3

def create_ec2_instance():
    # Create a session using the AWS key and token
    session = boto3.Session(aws_access_key_id='AKIA2PFUWBFM5SHFTROZ', aws_secret_access_key='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')

    # Create an EC2 resource
    ec2 = session.resource('ec2')

    # Create a new EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-xxxxxxxx',  # Replace with the desired Amazon Machine Image (AMI) ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'  # Replace with the desired instance type
    )

    # Print the instance ID of the newly created instance
    print(instances[0].id)


# Example usage
create_ec2_instance()
```


## Function 3: Send SNS Message

This function sends a message to an SNS topic in your AWS account.

```python
import boto3

def send_sns_message():
    # Create a session using the AWS key and token
    session = boto3.Session(aws_access_key_id='AKIA2PFUWBFM5SHFTROZ', aws_secret_access_key='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')

    # Create an SNS client
    sns = session.client('sns')

    # Publish a message to the specified SNS topic
    response = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:123456789012:my-topic',  # Replace with the ARN of your SNS topic
        Message='Hello, world!'
    )

    # Print the response
    print(response)


# Example usage
send_sns_message()
