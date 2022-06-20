import asyncio

from azure.eventhub_operations import run
from strategies.utils import Strategy
from azure.redis_operations import start_with_redis, check_with_redis, \
    finalize_with_redis, get_partial_with_redis


class KafkaStrategy(Strategy):

    def do_algorithm(self, filename, data):
        file_status = check_with_redis(filename)
        if file_status == "Partially processed":
            print("File partially processed, continuing ...")
            count = get_partial_with_redis()
            try:
                asyncio.run(run(data[count:], filename))
            except BaseException:
                return
            else:
                finalize_with_redis(filename)
        elif file_status == "Override" or file_status == "Completed":
            print("File present, doing nothing")
            return
        else:
            print("New file, starting ...")
            start_with_redis(filename)
            try:
                asyncio.run(run(data, filename))
            except BaseException:
                return
            else:
                finalize_with_redis(filename)
        return
