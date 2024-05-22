import boto3

# Specify your bucket name
bucket_name = 'my-bucket-23-18-18'

# File content as a string
file_content = 'Hello, this is the content of the file.'

# Create an S3 client
s3 = boto3.client('s3')

# Upload the file content
s3.put_object(Bucket=bucket_name, Key='destination/object-key.txt', Body=file_content.encode('utf-8'))

print(f"File content uploaded to {bucket_name} successfully.")
