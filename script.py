"""Print histogram for a matrix to STDOUT"""
from __future__ import division
from __init__ import *
import numpy as np

def main(npy_fname=None, absvalue=False):
  M = np.load(npy_fname)
  assert np.count_nonzero(np.isnan(M)) == 0
  if absvalue:
    M = np.abs(M)
  counts, bins = histogram(M)
  print "Distribution for %s (abs=%s)" % (npy_fname, absvalue)
  cumm = 0
  total = np.sum(counts)
  # histogram print
  for i in xrange(len(bins)):
    frac = counts[i] / total
    cumm += frac
    print bins[i], counts[i], frac, cumm
  # plot histogram
  # graph density
  
