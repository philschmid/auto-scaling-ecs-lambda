
import boto3

client = boto3.client('sqs', aws_access_key_id='AKIAW7N4JBTD2DMVRWUH',
                  aws_secret_access_key='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', region_name='eu-central-1')

def count_sqs(queue_url=''):
    try:
        count = client.get_queue_attributes(QueueUrl=queue_url,AttributeNames=['ApproximateNumberOfMessages'])
        return count['Attributes']['ApproximateNumberOfMessages']
    except:
        raise ValueError("SQS didn't return ApproximateNumberOfMessages")


count_sqs('x.eu-central-1.amazonaws.com/479820582087/talos-sqs-insight-translator-qa')