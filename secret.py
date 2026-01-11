from random import randint

def ReturnDlhText():
    return "dih" if randint(0, 1000) == 1000 else "dlh"

def ReturnDlhText_capital():
    return ReturnDlhText().capitalize()