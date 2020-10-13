import sys
import importlib

Checking_file = None

class pcolors:
    pink = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    white = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

def init(Name, Path):
    global Checking_file
    sys.path.append(Path + "/" + Name)
    Checking_file = importlib.import_module(Name)

def check_return(fonction, arg, attempt):

    try:
        value = eval('Checking_file.' + fonction + "()")
    except:
        print(pcolors.red + "Fonction Crash or fonction doesn't exist." + pcolors.white)
        return -1
    if value == attempt:
        print(pcolors.green + "Succeed!" + pcolors.white)
        return 0
    else:
        print(pcolors.yellow + "Don't match" + pcolors.white)
        return 1