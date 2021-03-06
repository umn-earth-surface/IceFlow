import iceflow
ic = iceflow.IceFlow()

import numpy as np
import scipy
from scipy.io import loadmat
from scipy.sparse import linalg
import os
import sys
from matplotlib import pyplot as plt

ic.useGRASS = True
ic.location='Iceland'
ic.gisbase = '/usr/local/src/grass7_trunk/dist.x86_64-unknown-linux-gnu'

ic.run_length_years = 3000. # years
ic.t_start_years = 0. # years
ic.dt_years = 2

ic.elevation = 'elev'

ic.n = 792000
ic.s = 240000
ic.w = 108000
ic.e = 868000
ic.dx = 4000
ic.dy = 4000

ic.mass_balance_parameterization = 'TP_PDD'
# Goes to Ta variable
ic.temperature_melt_season = 'TwentiethCenturyTemp_NCAR_CIRES_JJA_degC'
ic.melt_season_length_days = 120
#self.Pa /= 1000. / self.secyr # e.g., PRISM is in mm/yr, change to m/s.
# CONVERT THIS IN GRASS BEFOREHAND!!! <----------------------------------------
# Goes to Pair variable
ic.precipitation_solid = 'TwentiethCenturyPrecip_NCAR_CIRES_annual'
ic.T_correction = -5
ic.P_factor = 1

ic.ELA = None
ic.dbdz = None
ic.bcap = None

# Set this up to automatically number IceFlow outputs using glob
ic.output_filename=None
ic.output_figure=None
ic.plot_at_end_flag=False
ic.plot_during_run_flag = True
#ic.plot_t_years = ic.run_length_years

ic.GRASS_raster_ice_extent = 'FakeMeasuredExtents'

ic.verbose = True

ic.initialize()
ic.Pa /= (1000. * ic.secyr)
ic.run()
ic.finalize()


self = ic
"""

# INITIALIZE
self.initialize_define_region()
self.initialize_GRASS()
self.initialize_elevation_x_y_and_ice_grids_from_GRASS()
if self.mass_balance_parameterization == 'TP_PDD':
  self.initialize_climate_from_GRASS()
elif self.mass_balance_parameterization == 'ELA':
  self.basic_mass_balance_with_GRASS()
self.initialize_compute_variables()
self.initialize_output_lists()
self.initialize_runtime()
self.enforce_boundary_conditions()
self.initialize_sparse_array()

# RUN
for self.t_i in self.t_all:
  self.update()
  self.output()
"""
