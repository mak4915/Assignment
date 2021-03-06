import boto3
#List objects in an Amazon S3 bucket
s3 = boto3.resource('s3')
bucket = s3.Bucket('my-bucket')
for obj in bucket.objects.all():
    print(obj.key)
#Restore Glacier objects in an Amazon S3 bucket
s3 = boto3.resource('s3')
bucket = s3.Bucket('glacier-bucket')
for obj_sum in bucket.objects.all():
    obj = s3.Object(obj_sum.bucket_name, obj_sum.key)
    if obj.storage_class == 'GLACIER':
        # Try to restore the object if the storage class is glacier and
        # the object does not have a completed or ongoing restoration
        # request.
        if obj.restore is None:
            print('Submitting restoration request: %s' % obj.key)
            obj.restore_object(RestoreRequest={'Days': 1})
        # Print out objects whose restoration is on-going
        elif 'ongoing-request="true"' in obj.restore:
            print('Restoration in-progress: %s' % obj.key)
        # Print out objects whose restoration is complete
        elif 'ongoing-request="false"' in obj.restore:
            print('Restoration complete: %s' % obj.key)
