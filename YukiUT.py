import sys
import importlib
import io

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
    tmp_arg = ""
    i = 0
    for arg_value in arg:
        if (i == 0):
            tmp_arg += str(arg_value)
        else:
            tmp_arg += ", " + str(arg_value)
        i += 1
    try:
        value = eval('Checking_file.' + fonction + "(" + tmp_arg + ")")
    except:
        print(pcolors.red + "Fonction Crash or fonction doesn't exist." + pcolors.white)
        return -1

    if value == attempt:
        print(pcolors.green + "Succeed!" + pcolors.white)
        return 0
    else:
        print(pcolors.yellow + "Don't match" + pcolors.white)
        return 1

def check_print(fonction, arg, attempt):
    tmp_arg = ""
    i = 0
    for arg_value in arg:
        if (i == 0):
            tmp_arg += str(arg_value)
        else:
            tmp_arg += ", " + str(arg_value)
        i += 1
    value = ""
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    try:
        eval('Checking_file.' + fonction + "(" + tmp_arg + ")")
        value = new_stdout.getvalue()
        sys.stdout = old_stdout
    except:
        sys.stdout = old_stdout
        print(pcolors.red + "Fonction Crash or fonction doesn't exist." + pcolors.white)
        return -1
    if value == attempt:
        print(pcolors.green + "Succeed!" + pcolors.white)
        return 0
    else:
        print(pcolors.yellow + "Don't match" + pcolors.white)
        return 1