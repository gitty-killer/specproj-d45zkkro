"""Command line entry."""

import sys
from . import pipeline


def main():
    text = sys.stdin.read()
    results = pipeline.run_pipeline(text)
    for item in results:
        print(item)


if __name__ == '__main__':
    main()

