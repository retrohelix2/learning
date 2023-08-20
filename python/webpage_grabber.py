import urllib.request
import time

def getWebPage(url):
    start = time.time()

    with urllib.request.urlopen(url) as response:
        html = response.read()

    end = time.time()
    return end - start

def main():
    url = input("URL: ")

    for i in range(1,11):
        print(getWebPage(url))

if __name__ == '__main__':
    main()