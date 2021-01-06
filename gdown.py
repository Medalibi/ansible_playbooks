#!/usr/bin/python3

import gdown
import sys

url = str(sys.argv[0])
output = str(sys.argv[1])
print("Downloading ...")
gdown.download(url, output, quiet=False) 
