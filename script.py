"""Print histogram for a matrix to STDOUT"""
from __future__ import division
from __init__ import *
import numpy as np
import sys

def main(npy_fname=None, absvalue=False, step=0.05):
  M = np.load(npy_fname)
  step = float(step)
  assert np.count_nonzero(np.isnan(M)) == 0
  if absvalue:
    M = np.abs(M)
  counts, bins = histogram(M, step=step)
  print "#Value Distribution for %s (abs=%s)" % (npy_fname, absvalue)
  print "#Min: %.3f Max: %.3f Num Values: %d (%d by %d)" % \
    (M.min(), M.max(), np.size(M.ravel()), np.size(M,0), np.size(M,1))
  print "\t".join(['bin', 'count', 'density', 'accumulation', '1-accumulation'])
  cumm = 0
  total = np.sum(counts)
  # histogram print
  for i in xrange(len(counts)):
    frac = counts[i] / total
    cumm += frac
    print "%.2f\t%d\t%.6f\t%.6f\t%.6f" % (bins[i], counts[i], frac, cumm, 1-cumm)

  # GRAPH DENSITY
  # for each threshold
  # 1 Threshold dependency matrix
  # 2 remove rows and columns (nodes) with no edges. Report this.
  # 3 compute average, min, max, and std row and column degree
  print "\t".join(("threshold", "n_col_conn", "n_row_conn", "col_avg_degree", "col_avg_degree_all", "row_avg_degree", "row_avg_degree_all", "avg_degree", "avg_degree_all"))
  for i in xrange(len(counts)):
    threshold = bins[i]
    G = M >= threshold
    col_sums, row_sums = np.sum(G,0), np.sum(G,1)
    n_col_conn, n_row_conn = np.count_nonzero(col_sums), np.count_nonzero(row_sums)
    col_avg_degree_all, col_avg_degree = col_sums.sum() / np.size(G,1), col_sums.sum() / n_col_conn
    row_avg_degree_all, row_avg_degree = col_sums.sum() / np.size(G,0), row_sums.sum() / n_row_conn
    avg_degree_all, avg_degree = (col_sums.sum()+row_sums.sum()) / (np.size(G,0)+np.size(G,1)), \
      (col_sums.sum()+row_sums.sum()) / (n_col_conn+n_row_conn)
    print "\t".join(map(lambda x: "%.4f"%x, (threshold, n_col_conn, n_row_conn, col_avg_degree, col_avg_degree_all, row_avg_degree, row_avg_degree_all, avg_degree, avg_degree_all)))

  
if __name__ == "__main__":
  main(**dict([s.split('=') for s in sys.argv[1:]]))
