import numpy as np
import gzip 
import os as os
from os.path import isfile, join


mnist_path = './mnist/'

def list_files(mnist_path):
    return [join(mnist_path, f) for f in os.listdir(mnist_path) if f]


for f in list_files(mnist_path): 
    print(f)