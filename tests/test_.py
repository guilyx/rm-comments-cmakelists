import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from lib.rm_comments import removeComments

def test_file():
    t = removeComments("data/CMakeLists.txt")
    assert(t == True)