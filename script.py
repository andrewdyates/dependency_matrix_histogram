#!/usr/bin/python
"""Print histogram for a matrix to STDOUT

EXAMPLE USE:

python $HOME/dependency_matrix_histogram/script.py npy_fname=$HOME/gse15745/gse15745_gpl6104_gpl8490_spearman.values.npy absvalue=True step=0.05
"""
from __future__ import division
from __init__ import *
import numpy as np
import sys

def main(npy_fname=None, absvalue=False, step=0.05):
  M = np.load(npy_fname)
  step = float(step)
  if absvalue:
    M = np.abs(M)
  Q = remove_nans(M)
  print "#Value Distribution for %s (abs=%s)" % (npy_fname, absvalue)
  bins, counts = text_histogram(Q, step=step)
  print_degrees(M, bins, counts)


  
if __name__ == "__main__":
  main(**dict([s.split('=') for s in sys.argv[1:]]))
