from celery.result import AsyncResult
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('myrabbitmqserver'))

# Replace 'task_id' with the ID of the task you want to check
result = AsyncResult('task_id', backend='rpc', app=app)

# Check the status of the task
if result.ready():
    print('Task is complete')
else:
    print('Task is still running')