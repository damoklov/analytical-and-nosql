from flask import Flask, request
import requests
import os

from strategies.console_strategy import ConsoleStrategy
from strategies.file_strategy import FileStrategy
from strategies.kafka_strategy import KafkaStrategy
from strategies.utils import Context

app = Flask(__name__)


@app.route('/')
def load_file():
    endpoint = request.args.get("path")

    if not endpoint:
        return "Provide path"

    r = requests.get(endpoint)

    if os.environ["CHOICE"] == 'CONSOLE':
        context = Context(ConsoleStrategy())
        print("Client: Strategy is set to console output.")
        context.do_some_business_logic(endpoint, r.json())
    elif os.environ["CHOICE"] == 'CLOUD':
        context = Context(KafkaStrategy())
        print("Client: Strategy is set to cloud output.")
        context.do_some_business_logic(endpoint, r.json())
    elif os.environ["CHOICE"] == 'FILE':
        context = Context(FileStrategy())
        print("Client: Strategy is set to file output.")
        context.do_some_business_logic(endpoint, r.json())
    else:
        print("Something went wrong")
        return "NOT OK"

    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

