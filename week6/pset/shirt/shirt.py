import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    name_input, name_output = sys.argv[1], sys.argv[2]
    input_ext = check_extension(name_input)
    output_ext = check_extension(name_output)
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    merge_picture(name_input, name_output)


def merge_picture(input_file, name_output):
    try:
        shirt = Image.open("shirt.png")
        img = Image.open(input_file)
        new_img = ImageOps.fit(img, (600, 600))
        new_img.paste(shirt, shirt)
        new_img.save(name_output)
    except:
        sys.exit("File does not exist")

def check_extension(str):
    valid_ext = ["jpg", "jpeg", "png"]
    try:
        extension = str.split(".")[1]
    except:
        sys.exit("Invalid input")
    else:
        for ext in valid_ext:
            if ext == extension:
                return extension
        sys.exit("Invalid input")

main()