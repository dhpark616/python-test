import fileinput
import sys


def fix(file_name):
    with fileinput.input(files=(file_name), inplace=True) as f:
        for line in f:
            print(line.replace('import msg_', 'from . import msg_'), end='')


def main():
    fix(sys.argv[1])


if __name__ == "__main__":
    main()
