#!/usr/bin/python
import numpy as np

STEP = 0.05

def remove_nans(M)
  NANS = np.isnan(M)
  if np.count_nonzero(NANS) > 0:
    print "WARNING: %d 'nan' exist in dependency matrix. Filtering..."
    print "Previous size of M: %d" % np.size(M)
    Q = M[~NANS]
    print "Prior size of M (raveled) after removing nans: %d" % np.size(M)
  else:
    print "0 nans in M. Echoing M without changes..."
  return Q

def text_histogram(M, step=STEP):
  """Cannot handle masked arrays; compress or remove NANs first."""
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
    print "%.4f\t%d\t%.6f\t%.6f\t%.6f" % (bins[i], counts[i], frac, cumm, 1-cumm)
  return bins, counts


def print_degrees(M, bins, counts, step=STEP):
  """M must be a rectangular matrix"""
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


def histogram(M, step=STEP):
  """Generate histogram for dependency matrix.

  Cannot handle masked arrays; compress or remove NANs first.
  """
  m_min, m_max = M.min(), M.max() 
  assert abs(m_max) <= 1 and abs(m_min) <= 1
  if m_min < 0:
    bins = np.arange(-1, 1+step, step)
  else:
    bins = np.arange(0, 1+step, step)
  return np.histogram(M, bins=bins)


  
# Given a dependency matrix
# histogram
# cummulative stats


# if has negative values, repeat for absolute value


# distribution of connect
