import boto3
import os
from utils.count_sqs import count_sqs

client = boto3.client('ecs', region_name='eu-central-1')

# Required env vars:
# $ecs_cluster: name of the ECS cluster
# $ecs_task: name and revision of the task definition (i.e. `mytask:1`)
# $ecs_service: name of the ECS service
# $sqs_queue_url: URL of SQS-Queue
def autoscaler(event,context):

    #
    # count messages in QUEUE
    #
    try:
        # message_number = count_sqs(os.environ['sqs_queue_url'])
        message_number = count_sqs('')
    except ValueError:
        return False
    #
    # if no messages in Queue set desired_count to 0
    #
    if(message_number == 0):
       desired_count = 0
    else:
    #
    # evaluates scale for message_number and sets desired_count
    #
        try:
            desired_count = evaluate_scale(message_number)
        except ValueError:
            return False
    #
    # updates ECS-Cluster
    # 
    try:
        response = client.update_service(
        cluster=os.environ['ecs_cluster'],
        service=os.environ['ecs_service'],
        taskDefinition=os.environ['ecs_task'],
        desiredCount=desired_count
    )
    except:
        return False

    return True


autoscaler('','')