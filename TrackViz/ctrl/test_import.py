import os
import sys
sys.path.append("..")
sys.path.append("/home/ls/dataset/TFusion/TrackViz/profile")
sys.path.append("/home/ls/dataset/TFusion/TrackViz/util")
from util.file_helper import safe_mkdir
from profile.import_test import import_success
from util.import_test2 import import_success2

if __name__ == "__main__":
    import_success2()
    # safe_mkdir('test111')
