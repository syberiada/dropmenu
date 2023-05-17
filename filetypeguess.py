import filetype
import os

def main():
    for file in os.scandir():
        if file.is_file() and not file.name.startswith('.'):
            print(file.path)
            try:
                kind = filetype.guess(file.path)
                if kind is None:
                    print('Cannot guess file type!')
                else:
                    print('File extension: %s' % kind.extension)
                    print('File MIME type: %s' % kind.mime)
            except:
                print('error parsing file')

if __name__ == '__main__':
    main()