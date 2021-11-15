
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--title", help="Title of application")
    parser.add_argument("-b", "--button-text", help="Button text")
    parser.add_argument("-f", "--fixed-size", help="Window fixed size")
    parser.add_argument("-s", "--size", help="Window's size")
    parser.parse_args()


if __name__ == '__main__':
    main()
