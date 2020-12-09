import os


HERE = os.path.abspath(os.path.dirname(__file__))
INPUT_FP = os.path.join(HERE, "input.txt")

with open(INPUT_FP, "r") as fp:
    INPUT_DATA = fp.read()
