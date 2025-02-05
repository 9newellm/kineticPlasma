# -*- coding: utf-8 -*-
"""Copy of getDataNplot

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tQxXzqpUDGYd791PGlhpkdnC1PNSCSYx
"""

!pip install pyspedas

import pyspedas
import pytplot
import numpy as np

def ImfConeAngle(trange=['2015-09-08-/08:00', '2015-09-08-/23:00']):

    pyspedas.mms.fgm(trange=trange, data_rate='brst', probe=[1], time_clip=True)
    # pyspedas.mms.mec(trange=trange, data_rate='brst', probe=[1], time_clip=True)
    # pyspedas.mms.fpi(center_measurement=True, datatype=['dis-moms', 'des-moms'], trange=trange, probe=[1,2,3,4])#Get number density here; not sure what datatypes specify
    # pyspedas.mms.edp(trange=trange, data_rate='brst', probe=[1], datatype=['dce', 'scpot'], time_clip=True)
    # pyspedas.mms.edi(trange=trange, probe=4)

    mss1_B_tot = pytplot.data_quants['mms1_fgm_b_dmpa_brst_l2_btot'].values
    mms1_B_vec = pytplot.data_quants['mms1_fgm_b_gse_brst_l2_bvec'].values
    mms1_B_xNumpyArray_time = pytplot.data_quants['mms1_fgm_b_gse_brst_l2_bvec'].coords['time'].values

    mss1_B_tot_np = np.array(mss1_B_tot)
    mms1_Bvec_np = np.array(mms1_B_vec)
    mms1_Bx_np = mms1_Bvec_np[:,1]

    ### Obtain Cone Angle:
    ImfConeAngle_rad = np.arccos(np.abs(mms1_Bx_np)/mss1_B_tot_np)
    ImfConeAngle_deg = np.rad2deg(ImfConeAngle_rad)

    ### Plot Cone Angle:
    pytplot.store_data("mms1_ImfConeAngle_deg", data={'x': mms1_B_xNumpyArray_time,'y': (ImfConeAngle_deg)})
    pytplot.tplot('mms1_ImfConeAngle_deg')
    # pytplot.store_data("mms1_ImfConeAngle_rad", data={'y': (ImfConeAngle_rad), 'x': mms1_B_xNumpyArray_time})

    return ImfConeAngle


ImfConeAngle()  #! Can