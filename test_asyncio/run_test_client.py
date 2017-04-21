import atexit
import inspect
import signal
import sys

from src.test_client import test_client


def main():
    if len(sys.argv) < 5:
        file_name = inspect.getfile(inspect.currentframe())
        print('Usage: sudo python3 {} {{host port user_id char_name}}'.format(file_name))
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    user_id = sys.argv[3]
    char_name = sys.argv[4]

    test_client.run(host, port, user_id, char_name)


if __name__ == '__main__':
    main()
