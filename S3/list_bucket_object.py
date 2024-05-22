import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()
# # response will be in json format
# print(response)

# print(response ['ResponseMetadata'] ['HostId'])

# print(response ['Buckets'][0]['Name'])
# print(response ['Buckets'][3])

# it will give the length of buckets
# print(len(response['Buckets']))

# for loop for displaying buckets
for i in range(0,len(response['Buckets'])):
    print(response ['Buckets'][i]['Name'])


# Print the bucket names
# for bucket in response['Buckets']:
#     print(bucket['Name'])

#list objects

# bucket_name= "cloud-magdalene"
# s3 = boto3.client('s3')
# response = s3.list_objects(Bucket=bucket_name)
# print(response ['Contents'] [0] ['Key'])



