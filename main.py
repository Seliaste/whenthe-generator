import sys
import src.generator


def main():
    if len(sys.argv) < 2:
        print("Not enough arguments")
        return 1
    src.generator.generate_image("\"I love Python, the syntax is so simple and awesome to use!\"")


if __name__ == '__main__':
    sys.exit(main())
