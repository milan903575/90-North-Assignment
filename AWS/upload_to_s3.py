import boto3
import json
import base64
import logging

logging.basicConfig(level=logging.DEBUG)

def lambda_handler(event, context):

    s3 = boto3.client('s3')
    bucket_name = 'my-doc-storage-90'  


    file_content = event.get('file_content')  
    file_name = event.get('file_name', 'default.pdf') 

    # Validate inputs
    if not file_content or not file_name:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid input. Provide both file_content and file_name.')
        }

    try:
        # Fix Base64 padding if necessary
        file_content = file_content + '=' * (4 - len(file_content) % 4)
        logging.debug(f"Decoded file content: {file_content[:100]}...")  

        # Decode the Base64-encoded file content
        decoded_file = base64.b64decode(file_content)

        # Upload the decoded file to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,  # The name of the file in the S3 bucket
            Body=decoded_file  # The file content
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f'File "{file_name}" successfully uploaded to "{bucket_name}".')
        }
    
    except Exception as e:
        # Log and return an error if the upload fails
        logging.error(f"Error during file upload: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
