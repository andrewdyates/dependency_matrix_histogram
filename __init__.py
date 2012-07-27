#!/usr/bin/python
import numpy as np

STEP = 0.05

def remove_nans(M)
  NANS = np.isnan(M)
  if np.count_nonzero(NANS) > 0:
    print "WARNING: %d 'nan' exist in dependency matrix. Filtering..."
    print "Previous size of M: %d" % np.size(M)
    M = M[~NANS]
    print "Prior size of M (raveled) after removing nans: %d" % np.size(M)
  else:
    print "0 nans in M. Echoing M without changes..."
  return M

def text_histogram(M, step=STEP):
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

def histogram(M, step=STEP):
  """Generate histogram for dependency matrix."""
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
