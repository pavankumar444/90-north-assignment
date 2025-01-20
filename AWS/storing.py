import json
import boto3
import base64

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        file_name = event.get('fileName')
        bucket_name = event.get('bucketName')
        file_content_base64 = event.get('fileContent')

        if not file_name or not bucket_name or not file_content_base64:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'fileName, bucketName, and fileContent are required'})
            }
        file_content = base64.b64decode(file_content_base64)
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'File {file_name} uploaded successfully to bucket {bucket_name}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
