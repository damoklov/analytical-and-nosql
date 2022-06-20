from strategies.utils import Strategy


class ConsoleStrategy(Strategy):

    def do_algorithm(self, filename, data):
        for line in data:
            print(line)
        return None
