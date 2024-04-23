import requests
import sys


def main():
    # check if there is a arg
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    if len(sys.argv) > 2:
        sys.exit("Too much command-line arguments")
    # try to convert str to float
    try:
        value = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        convert_to_btc(value)


def convert_to_btc(value):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        # try to get a request from api and convert as json
        req = requests.get(url).json()
        # extract price from json
        price = req["bpi"]["USD"]["rate_float"]
        print(f"${price * value:,.4f}")
    except requests.RequestException:
        sys.exit("Request timeout")


main()
