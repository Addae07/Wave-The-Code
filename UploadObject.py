import boto3

s3 = boto3.client('s3')

bucket_name = 'wlawrence-bucket-test-boto3'
s3_resource.Bucket(bucket_name).put_object(Key='TimeOfYear.jpeg', Body=updated_file)
print('Yas, file uploaded')