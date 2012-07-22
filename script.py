"""Print histogram for a matrix to STDOUT"""
from __future__ import division
from __init__ import *
import numpy as np
import sys

def main(npy_fname=None, absvalue=False):
  M = np.load(npy_fname)
  assert np.count_nonzero(np.isnan(M)) == 0
  if absvalue:
    M = np.abs(M)
  counts, bins = histogram(M)
  print "Value Distribution for %s (abs=%s)" % (npy_fname, absvalue)
  print "Min: %.3f Max: %.3f Num Values: %d (%d by %d)" % \
    (M.min(), M.max(), np.size(M.ravel()), np.size(M,0), np.size(M,1))
  print "\t".join(['bin', 'count', 'density', 'accumulation'])
  cumm = 0
  total = np.sum(counts)
  # histogram print
  for i in xrange(len(counts)):
    frac = counts[i] / total
    cumm += frac
    print "%.2f\t%d\t%.4f\t%.4f" % (bins[i], counts[i], frac, cumm)
  # plot histogram
  # graph density
  
if __name__ == "__main__":
  main(**dict([s.split('=') for s in sys.argv[1:]]))
