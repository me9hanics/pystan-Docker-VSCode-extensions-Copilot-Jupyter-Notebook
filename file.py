import sys
import os

def main():
    with open("file.txt", "w") as f:
        f.write("The current working directory is: " + os.getcwd() + "\n")
        f.write("Python version: " + sys.version + "\n")
