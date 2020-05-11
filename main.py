import argparse
from lib.rm_comments import removeComments

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean comments from CMakeLists.")
    parser.add_argument('file_path', type=str, default='data/CMakeLists', help="Path of the targetted CMakeLists")
    args = parser.parse_args()
    removeComments(args.file_path)