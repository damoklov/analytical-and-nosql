from strategies.utils import Strategy


class FileStrategy(Strategy):

    def do_algorithm(self, filename, data):
        with open('test.txt', 'w') as f:
            for line in data:
                f.write(str(line) + '\n')
        return None
