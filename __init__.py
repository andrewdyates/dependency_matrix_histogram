#!/usr/bin/python
import numpy as np


STEP = 0.05

def histogram(M):
  """Generate histogram for dependency matrix."""
  m_min, m_max = M.min(), M.max() 
  assert abs(m_max) <= 1 and abs(m_min) <= 1
  if m_min < 0:
    bins = np.arange(-1, 1+STEP, STEP)
  else:
    bins = np.arange(0, 1+STEP, STEP)
  return np.histogram(M, bins=bins)


  
# Given a dependency matrix
# histogram
# cummulative stats


# if has negative values, repeat for absolute value


# distribution of connect
