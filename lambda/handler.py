import boto3
import os
from utils.count_sqs import count_sqs
from utils.evaluate_scale import evaluate_scale

client = boto3.client('ecs', region_name='eu-central-1')


# Required env vars:
# $ecs_cluster: name of the ECS cluster
# $ecs_task: name and revision of the task definition (i.e. `mytask:1`)
# $ecs_service: name of the ECS service
# $sqs_queue_url: URL of SQS-Queue
def autoscaler(event,context):
    # #
    # # count messages in QUEUE
    # #
    # try:
    #     # message_number = count_sqs(os.environ['sqs_queue_url'])
    #     message_number = count_sqs(os.environ['sqs'])
    #     # message_number = count_sqs(queue_url)
    # except ValueError:
    #     return False
    # print(message_number)
    # #
    # # if no messages in Queue set desired_count to 0
    # #
    # if(message_number == 0):
    #    desired_count = 0
    # else:
    # #
    # # evaluates scale for message_number and sets desired_count
    # #
    #     try:
    #         desired_count = evaluate_scale(message_number)
    #     except ValueError:
    #         return False
    # # #
    # # # updates ECS-Cluster
    # # # 
    desired_count = 0
    print(desired_count)
    # try:
    response = client.update_service(
        # cluster=os.environ['ecs_cluster'], #arn
        cluster='arn:aws:ecs:eu-central-1:479820582087:cluster/talos-ecs-cluster-insight-translator-qa', #arn
        # service=os.environ['ecs_service'], #name 
        service='arn:aws:ecs:eu-central-1:479820582087:service/talos-ecs-service-insight-translator-qa', #name 
        # taskDefinition=os.environ['ecs_task'], #arn 
        taskDefinition='arn:aws:ecs:eu-central-1:479820582087:task-definition/tanslator-scale-ECSTaskdefintion-4Z9LA7YRTEF0:1', #arn 
        desiredCount=desired_count
    )
    # except:
    #     return False

    # return True


autoscaler('','')