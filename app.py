import base64
import boto3
import imghdr
import json
import random
import string
import os
import uuid


BUCKET = os.environ['BUCKET']
uname = str(uuid.uuid4())
s3_client = boto3.client('s3')


def handler(event, context):
    
    if event['httpMethod'] == "POST" :

        image = event['body']
 
        write_encode = open("/tmp/output.bin", "w")
        write_encode.write(image)
        write_encode.close()
        
        read_encode = open("/tmp/output.bin", "rb")
        byte = read_encode.read()
        read_encode.close()
        
        image_decode = open("/tmp/verify.png", "wb")
        image_decode.write(base64.b64decode(byte))
        image_decode.close
        
        verify_image_format = imghdr.what("/tmp/verify.png");
        
        if verify_image_format == 'png':
            dec = base64.b64decode(image)
            s3_client.put_object(Bucket=BUCKET, Key=uname + '.png', Body=dec)
            
        elif verify_image_format == 'jpg' or verify_image_format == 'jpeg':
            dec = base64.b64decode(image)
            s3_client.put_object(Bucket=BUCKET, Key=uname + '.jpg', Body=dec)
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(event)
    }
