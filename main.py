import sys
import src.generator


def main():
    if len(sys.argv) < 2:
        print("Not enough arguments")
        return 1
    src.generator.generate_image(" ".join(sys.argv[1:]))


if __name__ == '__main__':
    sys.exit(main())
