import inspect
import sys

from src.ch_server import ch_server


def main():
    if len(sys.argv) < 2:
        file_name = inspect.getfile(inspect.currentframe())
        print('Usage: sudo python3 {} {{develop|testing|staging|product}}'.format(file_name))
        sys.exit()

    phase = sys.argv[1]
    ch_server.run(phase)


if __name__ == '__main__':
    main()
