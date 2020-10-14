import sys
import importlib
import io

Checking_file = None
Testing_call = [0, 0]

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

def result():
    percent = Testing_call[1] / Testing_call[0] * 100
    print("------")
    if (percent < 33):
        print("Result: " + pcolors.red + str(round(percent, 2)) + "% of your test succeed!")
    elif (percent < 66):
        print("Result: " + pcolors.yellow + str(round(percent, 2)) + "% of your test succeed!")
    else:
        print("Result: " + pcolors.green + str(round(percent, 2)) + "% of your test succeed!")
    print(pcolors.blue + "\tTotal Test: " + str(Testing_call[0]))
    print(pcolors.green + "\tSucceed: " + str(Testing_call[1]))
    print(pcolors.red + "\tFailed: " + str(Testing_call[0] - Testing_call[1]) + pcolors.white)
    print("------")

def check_return(fonction, arg, attempt):
    Testing_call[0] += 1
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
        Testing_call[1] += 1
        return 0
    else:
        print(pcolors.yellow + "Don't match")
        print(pcolors.blue + "Get:\n" + str(value))
        print(pcolors.white + "Attempt:\n" + str(attempt))
        return 1

def check_print(fonction, arg, attempt):
    Testing_call[0] += 1
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
        Testing_call[1] += 1
        return 0
    else:
        print(pcolors.yellow + "Don't match")
        print(pcolors.blue + "Get: " + value)
        print(pcolors.white + "Attempt: " + attempt)
        return 1