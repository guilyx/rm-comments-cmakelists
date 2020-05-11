import os

def removeComments(filename):
    savedFile = filename.replace('.txt', 'Copy.txt')
    os.rename(filename, savedFile)
    with open(filename, 'w') as new_file:
        with open(savedFile) as old_file:
            for line in old_file:
                if '#' not in line and line != '\n':
                    new_file.write(line)
    return(True)