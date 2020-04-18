WHITE = '\033[0m'
WARNING = '\033[93m'
BOLD = '\033[1m'
BLUE = '\033[94m'
UNDERLINE = '\033[4m'
GREEN = '\033[92m'
HEADER = '\033[95m'
FAIL = '\033[91m'
DARK_BLUE = '\033[1;34;1m'
END = '\033[0m'



from time import gmtime, strftime

def log(msg):
    timestamp("Jaram: " + msg )


def debug(msg):
    timestamp( "Jaram: " + msg)


def timestamp(msg):
    print("[" + strftime("%H:%M:%S", gmtime()) + "] " + msg)