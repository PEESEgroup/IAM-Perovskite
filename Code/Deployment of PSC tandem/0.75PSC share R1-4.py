from scipy.interpolate import interp1d
import scipy.optimize, os, time, struct
from math import *
from socket import *
import numpy as np
import matplotlib.pyplot as plt
import math


####This Program is for SSP2-BASE-3.5℃  to 2050####

share=0.75##share

xh = []; yh = []
f = open('GLO PV 3.5.txt', 'r')  # Open the txt file
line = f.readline()  # Read data from the txt file into an array
while line:
    arr = line.split()
    xh.append(float(arr[0]))
    yh.append(float(arr[1]))
    line = f.readline()
f.close()
dHcata = interp1d(xh, yh)
def dglosi(T):
    return dHcata(T)

xh2 = []; yh2 = []  ####### Open txt file
f = open('BASE PSC.txt', 'r')  # HSC; kJ/(mol*T) open is equivalent to opening our txt file
line = f.readline()  # Read data from the txt file into an array
while line:
    arr = line.split()
    xh2.append(float(arr[0]))
    yh2.append(float(arr[1]))
    line = f.readline()
f.close()
dHcata2 = interp1d(xh2, yh2)
def dbasepsc(T):
    return dHcata2(T)

region = 0
while region < 4:
    
    if region == 0:
        print("China")
        xh1 = []; yh1 = []  ## Same functionality as above
        f = open('China SSP2 3.5 SI.txt', 'r')
        line = f.readline()
        while line:
            arr = line.split()
            xh1.append(float(arr[0]))
            yh1.append(float(arr[1]))
            line = f.readline()
        f.close()
        dHcata1 = interp1d(xh1, yh1)
        def dchinasi(T):
            return dHcata1(T)

        
    if region == 1:
        print("India")
        xh1 = []; yh1 = []  ### Same functionality as above
        f = open('India SSP2 3.5 SI.txt', 'r')
        line = f.readline()
        while line:
            arr = line.split()
            xh1.append(float(arr[0]))
            yh1.append(float(arr[1]))
            line = f.readline()
        f.close()
        dHcata1 = interp1d(xh1, yh1)
        def dchinasi(T):
            return dHcata1(T)

        
    if region == 2:
        print("USA")
        xh1 = []; yh1 = []  ### Same functionality as above
        f = open('USA SSP2 3.5 SI.txt', 'r')
        line = f.readline()
        while line:
            arr = line.split()
            xh1.append(float(arr[0]))
            yh1.append(float(arr[1]))
            line = f.readline()
        f.close()
        dHcata1 = interp1d(xh1, yh1)
        def dchinasi(T):
            return dHcata1(T)

    if region == 3:
        print("Brazil")
        xh1 = []; yh1 = []
        f = open('Brazil SSP2 3.5 SI.txt', 'r')
        line = f.readline()
        while line:
            arr = line.split()
            xh1.append(float(arr[0]))
            yh1.append(float(arr[1]))
            line = f.readline()
        f.close()
        dHcata1 = interp1d(xh1, yh1)
        def dchinasi(T):
            return dHcata1(T)
        
    region = region + 1


    

    a = 2009  # a is the starting year for calculation
    b = 2030  # b is the year PSC tandem enters the market
    PV_C_exist = 0
    PSC_C_exist = 0
    year = a; nc = []; nu = []; ne = []; ni = []; nr = []; npsc_c = []; nsi_c = []; nexist_psc = []; nexist_si = []; nshare_psc = []
    Cap_PSC = []; GLO_CAP_PSC = []; Sideg = []; PSCdeg = []; aa = 0; bb = 0; cc = 0; dd = 0; nnewsi = []; nsi_c_lj = []; npsc_c_lj = []; PSCdeg_lj = []; Sideg_lj = []
    lt_Si = 30

    while year < 2050:
        year = year + 1

        ### Si aging can be placed at the beginning, all using PV_deg
        PV_deg_1 = PV_C_exist * (0.2 / lt_Si)  # This is the natural aging each year
        if year - lt_Si > a:  # Indicates that there are retirements this year
            PV_deg_2 = nnewsi[year - lt_Si - 2010] * 0.8  ## Retire 80% of the year's amount, as the remaining 20% has already been retired along the way; lifespan here is 30 years, so use the total amount, retire only up to 2020
        else:  # No direct retirements yet
            PV_deg_2 = 0
        PV_deg = PV_deg_1 + PV_deg_2  # Total aging
 
        if year > 2019:
            aa = aa + PV_deg
        Sideg.append(PV_deg)
        Sideg_lj.append(aa)
        PV_C_exist = PV_C_exist - PV_deg  # Calculate aging based on the start of each year, then consider the amount to be invested this year based on aging
        if year < b:  # At this point, no PSC tandem is involved
            PV_C_R = dchinasi(year)
            PSCdeg.append(0)
            PSCdeg_lj.append(0)
            if PV_C_R > PV_C_exist:
                PV_C_NEW = PV_C_R - PV_C_exist
                PV_C_exist = PV_C_R
            else:
                PV_C_NEW = 0
                PV_C_R = PV_C_exist
            PSC_NEW = 0
            PSC_C_R = 0
            
        else:  # Start adding PSC, share is already processed; there will be a share, then each country multiplies by that share
            CHINA_PSC = dchinasi(year) * dbasepsc(year) * share  # Local multiplied by DOI multiplied by target share
            CHINA_SI = dchinasi(year) - CHINA_PSC
            PV_C_R = CHINA_SI
            PSC_C_R = CHINA_PSC  # PSC tandem required amount for this year
            
            A_old = sum(Cap_PSC)
            k = len(Cap_PSC)
            i = 0
            while i < k:
                if i < 6:
                    if Cap_PSC[i] != 0:
                        Cap_PSC[i] = Cap_PSC[i] - GLO_CAP_PSC[i] * (1.344 - 0.3567 * i + 0.0646 * i * i - 0.00404 * i * i * i) / 100
                    if Cap_PSC[i] < 0.8 * GLO_CAP_PSC[i] and Cap_PSC[i] != 0:
                        Cap_PSC[i] = 0
                else:
                    if Cap_PSC[i] != 0:
                        Cap_PSC[i] = Cap_PSC[i] - GLO_CAP_PSC[i] * (0.667) / 100
                    if Cap_PSC[i] < 0.8 * GLO_CAP_PSC[i] and Cap_PSC[i] != 0:
                        Cap_PSC[i] = 0
                   
                i = i + 1
            A_new = sum(Cap_PSC)
            PSC_deg = A_old - A_new  # This gives the yearly aging situation; consider writing it directly outside
            bb = bb + PSC_deg
            PSCdeg.append(PSC_deg)
            PSCdeg_lj.append(bb)
            PSC_C_exist = PSC_C_exist - PSC_deg  # Aging last year’s
            if PSC_C_R < PSC_C_exist:  # PV regression
                ## First, PSC is zero, processing only Si
                ## Here, status quo is maintained, no new addition, normal aging last year
                print(year)
                PSC_NEW = 0
                Cap_PSC.append(PSC_NEW); GLO_CAP_PSC.append(PSC_NEW)
                PSC_C_R = PSC_C_exist
                

                    
                ### Silicon remains unchanged
                if PV_C_R > PV_C_exist:  # Still need new Si PV with this share, everything normal
                    PV_C_NEW = PV_C_R - PV_C_exist
                    PV_C_exist = PV_C_R

                    
                else:  # Silicon insufficient
                    PV_C_R = PV_C_exist  # Si does not change this year
                    PV_C_NEW = 0

                    
            else:  # Normal situation
                if PV_C_R > PV_C_exist:  # New Si PV investment
                    PV_C_NEW = PV_C_R - PV_C_exist
                    PV_C_exist = PV_C_R
                    
                    ## Regarding PSC tandem
                    PSC_NEW = PSC_C_R - PSC_C_exist
                    Cap_PSC.append(PSC_NEW); GLO_CAP_PSC.append(PSC_NEW)
                    PSC_C_exist = PSC_C_R
                    

                else:  # Adjust PSC tandem penetration
                    PV_C_R = PV_C_exist  # Si does not change this year
                    PV_C_NEW = 0

                    PSC_C_R = CHINA_SI + CHINA_PSC - PV_C_R  # Adjust PSC target this year
                    if PSC_C_R < PSC_C_exist:
                        PSC_NEW = 0
                        Cap_PSC.append(PSC_NEW); GLO_CAP_PSC.append(PSC_NEW)
                        PSC_C_R = PSC_C_exist
                    else:
                        PSC_NEW = PSC_C_R - PSC_C_exist  # Growth limited by Si market
                        PSC_C_exist = PSC_C_R
                        Cap_PSC.append(PSC_NEW); GLO_CAP_PSC.append(PSC_NEW)

        
        cc=cc+PSC_NEW
        dd=dd+PV_C_NEW
        nnewsi.append(PV_C_NEW)
        npsc_c_lj.append(cc)
        npsc_c.append(PSC_NEW)
        nsi_c_lj.append(dd)
        nsi_c.append(PV_C_NEW)
        nexist_psc.append(PSC_C_R)
        nexist_si.append(PV_C_R)
        nshare_psc.append(PSC_C_R/dchinasi(year))
        
    print("TOT PSC")
    for i in range (len(nexist_psc)):
        print(nexist_psc[i])
    print("\n")
    
    print("TOT SI")
    for i in range (len(nexist_si)):
        print(nexist_si[i])
    print("\n")    
               
    print("NEW PSC")
    for i in range (len(npsc_c)):
        print(npsc_c[i])
    print("\n")
    
    print("NEW SI")
    for i in range (len(nsi_c)):
        print(nsi_c[i])
    print("\n")
    
    print("累计 NEW PSC")
    for i in range (len(npsc_c_lj)):
        print(npsc_c_lj[i])
    print("\n")

    print("累计 NEW SI")
    for i in range (len(nsi_c_lj)):
        print(nsi_c_lj[i])
    print("\n")

    print("PSCdeg")
    for i in range (len(PSCdeg)):
        print(PSCdeg[i])
    print("\n")
    
    print("Sideg")
    for i in range (len(Sideg)):
        print(Sideg[i])
    print("\n")

    print("累计PSCdeg")
    for i in range (len(PSCdeg_lj)):
        print(PSCdeg_lj[i])
    print("\n")

    print("累计Si deg")
    for i in range (len(Sideg_lj)):
        print(Sideg_lj[i])
    print("\n")

    print("Share")
    for i in range (len(nshare_psc)):
        print(nshare_psc[i])
    print("\n")

    
