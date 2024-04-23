# make func check takes 1 arg str
def checkArgs(str):
    # make switch case for each extension
    match str:
        case ".gif":
            print("image/gif")
        case ".jpg" | ".jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

def main():
    # ask user for file name
    fileName = input("File name: ").strip().lower()
    # seek where last index of "." is
    idx = fileName.rfind(".")
    # set ext to be the extension type from idx to end of string
    ext = fileName[idx:]
    checkArgs(ext)

main()