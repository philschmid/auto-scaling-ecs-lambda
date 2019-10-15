import boto3
import os
from utils.count_sqs import count_sqs

client = boto3.client('ecs', region_name='eu-central-1')

def autoscaler(event,context):
    try:
        # message_number = count_sqs(os.environ['sqs_queue'])
        message_number = count_sqs('')
    except ValueError:
        return False


    try:
        desired_count = evaluate_scale(message_number)
    except ValueError:
        return False
      
    try:
        response = client.update_service(
        cluster=os.environ['test_ecs_cluster'],
        service=os.environ['test_ecs_service'],
        taskDefinition=os.environ['test_ecs_task'],
        desiredCount=desired_count
    )
    except:
        return False

    return True
# Required env vars:
# $test_ecs_cluster: name of the ECS cluster
# $test_ecs_task: name and revision of the task definition (i.e. `mytask:1`)
# $test_ecs_service: name of the ECS service

autoscaler('','')