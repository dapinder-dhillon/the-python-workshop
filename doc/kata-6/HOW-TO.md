
## Story 6: Boto3 overview  

### Objectives:
- Using boto3 to understand the session.
- Difference between client and resource.
- Object-Oriented, type followed, test coverage

### Steps:
```shell
pipenv install boto3 --dev --python 3.8.10
```
- Above will update your `Pipfile` and `Pipfile.lock` to include `boto3` under `[dev-packages]`.
- Create a new file named `boto3_seesion.py` under logs_processor directory and copy below contents.
```python
import logging
import os

import boto3
import botocore

REGION = "eu-west-1"


def get_boto3_session():
    # Get environment variable
    aws_profile_name = os.getenv("AWS_PROFILE_NAME")
    try:
        return boto3.session.Session(profile_name=aws_profile_name)
    except botocore.exceptions.ProfileNotFound as profile_not_found:
        logging.debug(
            'ProfileNotFound "%s", executing boto3 on IAM Role', aws_profile_name
        )
        logging.debug("Exception: %s", profile_not_found)
    return boto3.session.Session()
```
- Create a new file named `s3_processor.py` under logs_processor directory and copy below contents.
```python
from .boto3_seesion import get_boto3_session


class S3Processor:

    def list_tio_bucket_contents_as_client(self, account_id: int) -> list:
        keys = []
        session = get_boto3_session()
        s3_client = session.client("s3")
        response = s3_client.list_objects_v2(Bucket="elsevier-tio-" + str(account_id))
        for content in response['Contents']:
            obj_dict = s3_client.get_object(Bucket="elsevier-tio-" + str(account_id), Key=content['Key'])
            print(content['Key'], obj_dict['LastModified'])
            keys.append(content['Key'])
        return keys

    def list_tio_bucket_contents_as_resource(self, account_id: int) -> list:
        keys = []
        session = get_boto3_session()
        s3_resource = session.resource("s3")
        bucket = s3_resource.Bucket(name="elsevier-tio-" + str(account_id))
        for obj in bucket.objects.all():
            print(obj.key, obj.last_modified)
            keys.append(obj.key)
        return keys
```
- In the resource case you do not have to make a second API call (`get_object`) to get the objects; they're available to you as a collection on the bucket. These collections of sub-resources are lazily-loaded.
- with a low-level client, you directly interact with response dictionary from a deserialized API response.
- in contrast, with the resource, you interact with standard Python classes and objects rather than raw response dictionaries.
- Overall, the resource abstraction results in a more readable code
- You can see that the Resource version of the code is much simpler, more compact, and has more capability.
- The Client version of the code would actually be more complicated than shown above if you wanted to include pagination.
- Create a new file named `test_s3_processor.py` under `/python_workshop_demo/python/tests`
```python
import os
import unittest

import boto3

from python.logs_processor.s3_processor import S3Processor


class TestNotification(unittest.TestCase):
    def setUp(self):
        os.environ["AWS_PROFILE_NAME"] = "aws-ifp-nonprod"

    def test_list_tio_bucket_contents_as_client(self):
        s3_processor = S3Processor()
        client_object_keys = s3_processor.list_tio_bucket_contents_as_client(account_id=596362325115)
        resource_object_keys = s3_processor.list_tio_bucket_contents_as_resource(account_id=596362325115)
        self.assertListEqual(client_object_keys, resource_object_keys)
```
- Execute the test
- Awesome, you have successfully completed kata-6 and the python-workshop.