import argparse
import os

def main(filename):
    savedFile = filename.replace('.txt', 'Copy.txt')
    os.rename(filename, savedFile)
    with open(filename, 'w') as new_file:
        with open(savedFile) as old_file:
            for line in old_file:
                if '#' not in line and line != '\n':
                    new_file.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean comments from CMakeLists.")
    parser.add_argument('file_path', type=str, default='data/CMakeLists', help="Path of the targetted CMakeLists")
    args = parser.parse_args()
    main(args.file_path)