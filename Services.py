import boto3
session = boto3.Session()
services = session.get_available_services()
print(services)