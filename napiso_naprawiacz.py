from alive_progress import alive_bar

import os
import sys


def decode_file(file_path):
    with open(file_path, 'r+',) as file:
        text = file.read()
        text = text.replace('¿', 'ż').replace('³', 'ł').replace('ê', 'ę')\
                   .replace('¹', 'ą').replace('œ', 'ś').replace('æ', 'ć')\
                   .replace('Ÿ', 'ź').replace('ñ', 'ń')
        file.seek(0)
        file.write(text)
        file.truncate()


def handle_folder(path):
    files = len([name for name in os.listdir(path)])
    with alive_bar(files) as bar:
        for file in os.listdir(path):
            if file.endswith(".txt"):
                decode_file(path + "/" + file)
            bar()


def main() -> int:
    if len(sys.argv) == 1:
        print("Please provide path to file or folder!")
        exit(0)

    path = sys.argv[1]

    if os.path.isfile(path) and path.endswith('.txt'):
        decode_file("txt file")
    elif os.path.isdir(path):
        handle_folder(path)
    else:
        print("Please provide valid file or folder!")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
