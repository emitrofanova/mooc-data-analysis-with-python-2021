#!/usr/bin/env python3

def file_extensions(filename):
    with open(filename, "r") as f:
        dct = {}
        lst = []
        for line in f:
            line = line[:-1]
            if "." in line:
                ext = line.split(".")[-1]
                if ext not in dct:
                    dct[ext] = []
                dct[ext].append(line)
            else:
                lst.append(line)
    return (lst, dct)

def main():
    files = file_extensions("src/filenames.txt")
    print(len(files[0]), "files with no extension")
    for ext in sorted(files[1]):
        print(ext, len(files[1][ext]))

if __name__ == "__main__":
    main()
