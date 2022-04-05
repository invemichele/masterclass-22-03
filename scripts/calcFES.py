#! /usr/bin/env python3

# Calculate Free Energy Surface (FES) from a trajectory using a (weighted) kernel density estimation (KDE)
# Only 1D and 2D are currently supported, but a 3D FES is hard to visualize...
# The calculated FES is dimensionless, and uses the logweights (e.g. bias/kbt) instead of the weights w
#   fes = -log w*p_{KDE}
#
# Contrary to scipy.stats.gaussian_kde and sklearn.neighbors.KernelDensity,
# this supports also periodic variables
# TODO: make it run faster
#

import numpy as np

### some other useful things ###
def calcDeltaF(fes, basinMask, kbt=1):
  fesA = -kbt*np.logaddexp.reduce(-1/kbt*fes[basinMask])
  fesB = -kbt*np.logaddexp.reduce(-1/kbt*fes[np.logical_not(basinMask)])
  return fesB - fesA

def calcESS(logweights): #Effective Sample Size
  return np.exp(2*np.logaddexp.reduce(logweights)-np.logaddexp.reduce(2*logweights))

### calc FES functions ###
### 1D stuff ###
def calcFESpoint1D(point, bandwidth, data, logweights):
  dist = (point - data) / bandwidth
  return -np.logaddexp.reduce(logweights - 0.5*dist*dist)

def calcFESpoint1Dperiodic(point, bandwidth, data, logweights, periodicity):
  dd = np.absolute(point - data)
  dist = np.minimum(dd, periodicity - dd) / bandwidth
  return -np.logaddexp.reduce(logweights - 0.5*dist*dist)

def calcFES1D(grid, bandwidth, data, logweights=None, periodic=False, mintozero=True):
  if logweights is None:
    logweights = np.zeros(len(data))
  if periodic is False:
    fes = np.array([calcFESpoint1D(point, bandwidth, data, logweights) for point in grid])
  else:
    periodicity = 2*np.pi
    if isinstance(periodic, float):
      periodicity = periodic
    fes = np.array([calcFESpoint1Dperiodic(point, bandwidth, data, logweights, periodicity) for point in grid])
  if mintozero:
    return fes - np.amin(fes)
  else:
    return fes

### 2D stuff ###
def calcFESpoint2D(point, bandwidth, data, logweights):
  dist = np.array([(point[i] - data[i]) / bandwidth[i] for i in range(2)])
  return -np.logaddexp.reduce(logweights - np.sum(0.5*dist*dist, axis=0))

def calcFESpoint2Dperiodic(point, bandwidth, data, logweights, periodicity):
  arg = np.array(logweights)
  for i in range(2):
    if periodicity[i] is None:
      dist_i = (point[i] - data[i]) / bandwidth[i]
    else:
      dd_i = np.absolute(point[i] - data[i])
      dist_i = np.minimum(dd_i, periodicity[i] - dd_i) / bandwidth[i]
    arg -= 0.5 * dist_i * dist_i
  return -np.logaddexp.reduce(arg)

def calcFES2D(meshgrid, bandwidth, data, logweights=None, periodic=False, mintozero=True):
  if logweights is None:
    logweights = np.zeros(len(data[0]))
#  X, Y = np.meshgrid(grid[0], grid[1])
  X, Y = meshgrid[0], meshgrid[1]
  fes = np.empty((len(X), len(Y)))
  if periodic is False:
    for i in range(len(X)):
      for j in range(len(Y)):
        fes[i,j] = calcFESpoint2D((X[i,j], Y[i,j]), bandwidth, data, logweights)
  else:
    periodicity = (2*np.pi, 2*np.pi)
    if np.ndim(periodic) == 1:
      periodicity = periodic #e.g. (None, 2*np.pi)
    for i in range(len(X)):
      for j in range(len(Y)):
        fes[i,j] = calcFESpoint2Dperiodic((X[i,j], Y[i,j]), bandwidth, data, logweights, periodicity)
  if mintozero:
    return fes - np.amin(fes)
  else:
    return fes

### the generic funcion ###
def calcFES(meshgrid, bandwidth, data, logweights=None, periodic=False, mintozero=True):
  if np.ndim(bandwidth) == 0:
    return calcFES1D(meshgrid, bandwidth, data, logweights, periodic, mintozero)
  elif np.ndim(bandwidth) == 1 and len(bandwidth) == 2:
    return calcFES2D(meshgrid, bandwidth, data, logweights, periodic, mintozero)
  else:
    assert False, 'can handle only 1D or 2D free energies'
