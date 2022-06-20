import redis
import os


REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PASS = os.environ["REDIS_PASS"]
REDIS_PORT = os.environ["REDIS_PORT"]


def check_with_redis(filename):
    r = redis.StrictRedis(host=REDIS_HOST, port=int(REDIS_PORT), password=REDIS_PASS, ssl=False)
    status = r.get(filename).decode("utf-8")
    if status == "Completed":
        print("Completed")
        r.set(filename, "Override")
        return "Completed"
    elif status == "Started":
        print("Started")
        return "Started"
    elif status == "Override":
        print("Override")
        return "Override"
    elif status == "Partially processed":
        return "Partially processed"
    else:
        return "N/A"


def start_with_redis(filename):
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS, ssl=False)
    r.set(filename, "Started")


def get_partial_with_redis():
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS, ssl=False)
    count = int(r.get("Processed").decode("utf-8"))
    return count


def write_intermediate_with_redis(filename, count_processed):
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS, ssl=False)
    r.set("Processed", count_processed)
    r.set(filename, "Partially processed")


def finalize_with_redis(filename):
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS, ssl=False)
    r.set(filename, "Completed")
