import emoji

def main():
    while True:
        str = input("Input: ").strip()
        try:
            print(emoji.emojize(str))
            break
        except:
            pass

main()