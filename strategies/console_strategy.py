from utils import Strategy


class ConsoleStrategy(Strategy):

    def do_algorithm(self, data):
        for line in data:
            print(line)
        return None
