import magic as ma
from utils import length
import os, sys

# fpath = os.path(os.path.dirname(__file__),'utils')
# sys.path.append(fpath)
res = length.get_length("Hello")

print("the length of hello is ", res, "characters long")
