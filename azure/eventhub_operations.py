from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from azure.redis_operations import write_intermediate_with_redis, get_partial_with_redis
import json
import os


CONN_STR = os.environ["CONN_STR"]
EH_NAME = os.environ["EH_NAME"]


async def run(data, filename):
    producer = EventHubProducerClient.from_connection_string(conn_str=CONN_STR, eventhub_name=EH_NAME)
    count = get_partial_with_redis()
    async with producer:
        for i in range(len(data)):
            event_data_batch = await producer.create_batch()
            event_data_batch.add(EventData(json.dumps(data[i])))
            if i % 10 == 0:
                write_intermediate_with_redis(filename, count + i)
            await producer.send_batch(event_data_batch)
