
#!/usr/bin/env python
import argparse
import os
import glob

import boto3

now = '2019-04-05-16-15-49'
file_path = '/home/pi/'

session = boto3.session.Session()

s3_client = session.client(
    service_name='s3',
    aws_access_key_id='3WS0VKFA6WD08Y8QZBUN',
    aws_secret_access_key='oZ/XljCBdRTDhhyZc=9WzO8cd7ecEbaQ0JFmniiq',
    endpoint_url='https://53dc7c09-57d5-11e9-bde1-c606aa6eabf1.sandbox.zenko.io',
)

file_to_upload = file_path + now + ".gif"
# print(file_to_upload)

#gif = {'file': open(file_to_upload,'rb')}
# file_to_upload = ''
data = open(file_to_upload, 'rb')
# print(data)
s3_client.put_object(Bucket='zenkolocal',
                     Key='testgif',
                     Body=data,
                     Metadata={ 'name': 'firstgif' })
# myJpgs=[0 for i in range(2)]
# for i in range(2):
#     myJpgs[i]=file_path + now + "-0" + str(i+1) + ".jpg"
#     jpg = {'file': open(myJpgs[i],'rb')}
#
#
#     print "Your image is on " + json.loads(wpupload.content)['link']
