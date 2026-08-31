import sys

import requests

DEFAULT_URL = "https://something.com"


def fetch(url):
    return requests.get(url)


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    r = fetch(url)
    print(r.status_code)
    print(r.content)


if __name__ == "__main__":
    main()