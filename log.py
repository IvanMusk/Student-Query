import sys

class Logger(object):
    def __init__(self, file="Default.log"):
        self.terminal = sys.stdout
        self.log = open(file, "a+")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger("action_out.log")
