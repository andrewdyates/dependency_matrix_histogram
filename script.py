
"""Print histogram for a matrix to STDOUT

EXAMPLE USE:

python $HOME/compile_dependency_reports2/script.py npy_fname=$HOME/gse15745/gse15745_gpl6104_gpl8490_spearman.values.npy absvalue=True step=0.05
"""
from __future__ import division
from __init__ import *
import numpy as np
import sys

def main(npy_fname=None, absvalue=False, step=0.05):
  M = np.load(npy_fname)
  step = float(step)
  M = remove_nans(M)
  if absvalue:
    M = np.abs(M)
  text_histogram(M, step=STEP)

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
