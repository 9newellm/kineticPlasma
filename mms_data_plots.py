# -*- coding: utf-8 -*-
"""MMS DATA PLOTS

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j359Z5lE7CrDUKYg6PttnFTuXgSbIZGm
"""

import pyspedas
import pytplot as pyt
from pytplot import tplot, tplot_names, timebar
import numpy as np
import math

omni_vars = pyspedas.omni.data(trange=['2016-07-19/22:00:00', '2016-07-20/22:00:00'],datatype='1min',time_clip=True)

tplot_names()

omni_V_x = pyt.data_quants['Vx'].values
omni_V_x_time = pyt.data_quants['Vx'].coords['time'].values
omni_V_x_numpy = np.array(omni_V_x)

omni_V_y = pyt.data_quants['Vy'].values
omni_V_y_time = pyt.data_quants['Vy'].coords['time'].values
omni_V_y_numpy = np.array(omni_V_y)

omni_V_z = pyt.data_quants['Vz'].values
omni_V_z_time = pyt.data_quants['Vz'].coords['time'].values
omni_V_z_numpy = np.array(omni_V_x)

omni_V_tot_numpy = np.sqrt(omni_V_x_numpy**2+omni_V_y_numpy**2+omni_V_z_numpy**2)
pyt.store_data("V", data={'x': omni_V_z_time, 'y': omni_V_tot_numpy})

omni_B_x = pyt.data_quants['BX_GSE'].values
omni_B_x_time = pyt.data_quants['BX_GSE'].coords['time'].values
omni_B_x_numpy = np.array(omni_B_x)

omni_B_y = pyt.data_quants['BY_GSE'].values
omni_B_y_time = pyt.data_quants['BY_GSE'].coords['time'].values
omni_B_y_numpy = np.array(omni_B_y)

omni_B_z = pyt.data_quants['BZ_GSE'].values
omni_B_z_time = pyt.data_quants['BZ_GSE'].coords['time'].values
omni_B_z_numpy = np.array(omni_B_z)

omni_B_tot_numpy = np.sqrt(omni_B_x_numpy**2+omni_B_y_numpy**2+omni_B_z_numpy**2)
pyt.store_data("B_tot", data={'x': omni_B_z_time, 'y': omni_B_tot_numpy})

Mag_Cone_Angle = np.arccos(abs(omni_B_x_numpy)/abs(omni_B_tot_numpy))
pyt.store_data("theta_x", data={'x': omni_B_z_time, 'y': Mag_Cone_Angle})

freq_fw = (7.6 * omni_B_tot_numpy * (np.cos(Mag_Cone_Angle))**2)/1000 # foreshock wave frequency
pyt.store_data("f_fw", data = {'x': omni_B_z_time, 'y': freq_fw} )

H_numpy = np.sqrt(omni_B_x**2 + omni_B_y**2)
pyt.store_data("H",data={'x': omni_B_z_time, 'y': H_numpy} )

tplot(['V','proton_density','BX_GSE','BY_GSM','BZ_GSM','B_tot','RMS_SD_B','theta_x','SYM_H','AL_INDEX','ASY_H','f_fw','H'])

def GetHrsBetween(trange, delDay=0, delHr=1, retHrs=True):
    """Increment the string interval on your own.

    Args:
        datetime_str (str, optional): _description_. Defaults to '2023-08-09/10:45:00'.
        delDay (int, optional): _description_. Defaults to 1.
        delHr (int, optional): _description_. Defaults to 1.
    """
    from datetime import datetime

    datetimeFormat = '%Y-%m-%d/%H:%M:%S'
    time_dif = datetime.strptime(trange[1], datetimeFormat) - datetime.strptime(trange[0], datetimeFormat)
    time_dif_in_s = time_dif.total_seconds()
    if not retHrs: return time_dif_in_s
    time_dif_in_hr = time_dif_in_s/3600

    return int(round(time_dif_in_hr)) #! ROUND MOMENT 0.5
    # return floor(diiference_hours)

import pyspedas
import pytplot as pyt
from pytplot import tplot, tplot_names, timebar
import numpy as np

start = '2016-07-19/22:00:00'
end = '2016-07-20/22:00:00'
trange = [start, end]


def RunThroughListOfTimes(listOfTimes = ['00:00:00',] ):

    refTime = '1970-01-01/00:00:00'
    # Create List of times to add.
    listOfTimeValues = []
    for instance in listOfTimes:

        print(instance)
        value = start.split('/')[0]+'/'+instance # for the instant in time.
        listOfTimeValues.append(GetHrsBetween(trange=[refTime, value], retHrs=False)) # Append each value WRT to the reference in seconds.

    return listOfTimeValues


def RunThroughListOfTimes(listOfTimes = ['00:00:00',] ):

    refTime = '1970-01-01/00:00:00'
    # Create List of times to add.
    listOfTimeValues = []
    for instance in listOfTimes:

        print(instance)
        value = start.split('/')[0]+'/'+instance # for the instant in time.
        listOfTimeValues.append(GetHrsBetween(trange=[refTime, value], retHrs=False)) # Append each value WRT to the reference in seconds.
    return listOfTimeValues

if __name__ == "__main__":
    omni_vars = pyspedas.omni.data(trange=['2016-07-19/22:00:00', '2016-07-20/22:00:00'],datatype='1min',time_clip=True)
    # Show all timebars:
    timebar(RunThroughListOfTimes()) # Using default times
    listOfTimes = ['12:00:00', '09:30:00'] # This is a test value
    timebar(RunThroughListOfTimes(listOfTimes), dash=True, color="green") # Testing functions.

    tplot_names()

    omni_B_x = pyt.data_quants['BX_GSE'].values
    omni_B_x_time = pyt.data_quants['BX_GSE'].coords['time'].values
    omni_B_x_numpy = np.array(omni_B_x)

    omni_B_y = pyt.data_quants['BY_GSE'].values
    omni_B_y_time = pyt.data_quants['BY_GSE'].coords['time'].values
    omni_B_y_numpy = np.array(omni_B_y)

    omni_B_z = pyt.data_quants['BZ_GSE'].values
    omni_B_z_time = pyt.data_quants['BZ_GSE'].coords['time'].values
    omni_B_z_numpy = np.array(omni_B_z)

    omni_B_tot_numpy = np.sqrt(omni_B_x_numpy**2+omni_B_y_numpy**2+omni_B_z_numpy**2)

    pyt.store_data("B_tot", data={'x': omni_B_z_time, 'y': omni_B_tot_numpy})

    tplot(['BX_GSE','BY_GSM','BZ_GSM','B_tot'])



import pyspedas
import pytplot as pyt
from pytplot import tplot, tplot_names, timebar, tdpwrspc
import numpy as np
trange=['2016-07-20/00:00:00', '2016-07-20/12:00:00']

pyspedas.themis.fgm(probe='d', trange=['2016-07-20/10:00:00', '2016-07-20/12:00:00'],time_clip=True) # Clear existing data no_update=False.
omni_vars = pyspedas.omni.data(trange=trange,datatype='1min',time_clip=True)
tplot_names()
mss1_B_tot = pyt.data_quants['thd_fgs_btotal'].values
# names = pytplot.tplot_names()
#mms1_B_vec = pyt.data_quants['mms1_fgm_b_gse_srvy_l2_bvec'].values
mms1_B_xNumpyArray_time = pyt.data_quants['thd_fgs_btotal'].coords['time'].values

#mms1_Bvec_np=np.array(mms1_B_vec)

mss1_B_tot_np=np.array(mss1_B_tot)


omni_B_x = pyt.data_quants['BX_GSE'].values
omni_B_x_time = pyt.data_quants['BX_GSE'].coords['time'].values
omni_B_x_numpy = np.array(omni_B_x)

omni_B_y = pyt.data_quants['BY_GSE'].values
omni_B_y_time = pyt.data_quants['BY_GSE'].coords['time'].values
omni_B_y_numpy = np.array(omni_B_y)

omni_B_z = pyt.data_quants['BZ_GSE'].values
omni_B_z_time = pyt.data_quants['BZ_GSE'].coords['time'].values
omni_B_z_numpy = np.array(omni_B_z)

omni_B_tot_numpy = np.sqrt(omni_B_x_numpy**2+omni_B_y_numpy**2+omni_B_z_numpy**2)

pyt.store_data("B_tot", data={'x': omni_B_z_time, 'y': omni_B_tot_numpy})

tplot(['BX_GSE','BY_GSM','BZ_GSM','B_tot'])
tplot('thd_fgs_btotal')
ImfConeAngle_rad = np.arccos(np.absolute(omni_B_x_numpy)/omni_B_tot_numpy)
ImfConeAngle_deg = np.rad2deg(ImfConeAngle_rad)

freq_approx=7.6*omni_B_tot_numpy*((np.cos(ImfConeAngle_rad))**2)

freq_approz_Hz=freq_approx/1000

pyt.store_data("freq_tplot", data={'x':omni_B_x_time, 'y':freq_approz_Hz})

# Test a load in of data for the power spectral density.
# scm_vars = pyspedas.themis.scm(probe='d', trange=['2013-11-5', '2013-11-6'])
# pyspedas.mms.scm(trange=['2015-10-16', '2015-10-16/3:00'], time_clip=True)

# pytplot.tplot("mms1_scm_acb_gse_scsrvy_srvy_l2") # B-field vectors
# tplot_names()


# exit()

# Fast fourier transform power spectrum analysis.
#! need to do tmeis a
scm_vars = pyspedas.themis.fgm(probe='d', trange=['2016-07-20/10:00:00', '2016-07-20/12:00:00'],time_clip=True)
### https://spedas.org/wiki/index.php?title=Wavelet -> Perform a wavelet analysis of the system.
tplot_names()
#tplot('thd_fgs_btotal')

#tdpwrspc('thd_fgs_btotal', bin=3)
# hanning window reduces spectral lecakge; bin=5
tdpwrspc('thd_fgs_btotal', nboxpoints=80, nshiftpoints=1, bin=1,newname='bannana')
#bin: frequency resolution; nshift: time resolution; nbox: PSD resoltuion

tplot_names()

#tplot(["thd_fgs_btotal", "thd_fgs_btotal_dpwrspc"])
tplot("bannana")

pyt.store_data("new_variable", data=["freq_tplot", "bannana"])
tplot("new_variable")