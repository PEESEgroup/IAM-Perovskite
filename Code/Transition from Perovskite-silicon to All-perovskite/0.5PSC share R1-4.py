from scipy.interpolate import interp1d
import scipy.optimize, os, time, struct
from math import *
from socket import *
import numpy as np
import matplotlib.pyplot as plt
import math


#### This Program is for SSP2-BASE-3.5℃ to 2050 ####

share = 0.5  # Share

xh = []; yh = []  ## Array for storing data
f = open('GLO PV 3.5.txt', 'r')  # Open the txt file
line = f.readline()  # Read data from txt file into array
while line:
    arr = line.split()
    xh.append(float(arr[0]))
    yh.append(float(arr[1]))
    line = f.readline()
f.close()
dHcata = interp1d(xh, yh)
def dglosi(T):
    return dHcata(T)

xh2 = []; yh2 = []  ###### Similar functionality as above
f = open('BASE PSC.txt', 'r')
line = f.readline()
while line:
    arr = line.split()
    xh2.append(float(arr[0]))
    yh2.append(float(arr[1]))
    line = f.readline()
f.close()
dHcata2 = interp1d(xh2, yh2)
def dbasepsc(T):
    return dHcata2(T)

xh3 = []; yh3 = []  ###### Similar functionality as above
f = open('RPSI.txt', 'r')
line = f.readline()
while line:
    arr = line.split()
    xh3.append(float(arr[0]))
    yh3.append(float(arr[1]))
    line = f.readline()
f.close()
dHcata3 = interp1d(xh3, yh3)
def R_A(T):
    return dHcata3(T)

xh4 = []; yh4 = []  ###### Similar functionality as above
f = open('RPP.txt', 'r')
line = f.readline()
while line:
    arr = line.split()
    xh4.append(float(arr[0]))
    yh4.append(float(arr[1]))
    line = f.readline()
f.close()
dHcata4 = interp1d(xh4, yh4)
def R_B(T):
    return dHcata4(T)

region = 0
while region < 4:
    
    if region == 0:
        print("China")
        xh1 = []; yh1 = []  ###### Similar functionality as above
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
        xh1 = []; yh1 = []  ###### Similar functionality as above
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
        xh1 = []; yh1 = []  ###### Similar functionality as above
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
        xh1 = []; yh1 = []  ###### Similar functionality as above
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

    a = 2009  # Starting year for calculation
    b = 2030  # Year PSC enters the market
    PV_C_exist = 0
    PSC_C_exist = 0
    year = a
    nc = []; nu = []; ne = []; ni = []; nr = []; npsc_c = []; nsi_c = []; nexist_psc = []; nexist_si = []; nshare_psc = []
    Cap_PSC = []; GLO_CAP_PSC = []; Sideg = []; PSCdeg = []; aa = 0; bb = 0; cc = 0; dd = 0
    nnewsi = []; nsi_c_lj = []; npsc_c_lj = []; PSCdeg_lj = []; Sideg_lj = []
    Cap_PSC_A = []; Cap_PSC_B = []; GLO_CAP_PSC_A = []; GLO_CAP_PSC_B = []; PSIdeg = []; PPdeg = []
    lt_Si = 30; PSI_TOT = 0; PSI_OLD = 0; PP_TOT = 0; PP_OLD = 0; PPEXIST = []; PSIEXIST = []       

    while year < 2050:
        year = year + 1

        ### Si aging can be placed at the beginning, using PV_deg
        PV_deg_1 = PV_C_exist * (0.2 / lt_Si)  # Natural aging per year
        if year - lt_Si > a:  # Indicates retirements this year
            PV_deg_2 = nnewsi[year - lt_Si - 2010] * 0.8  ## Retire 80% of the year's amount, as the remaining 20% has already retired along the way; lifespan here is 30 years
        else:  # No direct retirements yet
            PV_deg_2 = 0
        PV_deg = PV_deg_1 + PV_deg_2  # Total aging

        if year > 2019:
            aa = aa + PV_deg
        Sideg.append(PV_deg)
        Sideg_lj.append(aa)
        PV_C_exist = PV_C_exist - PV_deg  # Calculate aging based on the start of each year, then consider the amount to be invested this year based on aging
        if year < b:  # At this point, no PSC involvement; let it proceed normally
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
            PSC_NEW_A = PSC_NEW * R_A(year)
            PSC_NEW_B = PSC_NEW * R_B(year)
            PSI_deg = 0; PP_deg = 0
            PSC_C_R = 0
            
        else:  # Start adding PSC, share is already processed; each country multiplies by that share
  
            CHINA_PSC = dchinasi(year) * dbasepsc(year) * share  # Local multiplied by DOI multiplied by target share
            CHINA_SI = dchinasi(year) - CHINA_PSC
            PV_C_R = CHINA_SI
            PSC_C_R = CHINA_PSC  # PSC required amount for this year

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
            
            PSC_deg = A_old - A_new  # This gives the yearly aging situation
            
            PSI_old = sum(Cap_PSC_A)
         
            k = len(Cap_PSC_A)
            i = 0
            while i < k:
                if i < 6:
                    if Cap_PSC_A[i] != 0:
                        Cap_PSC_A[i] = Cap_PSC_A[i] - GLO_CAP_PSC_A[i] * (1.344 - 0.3567 * i + 0.0646 * i * i - 0.00404 * i * i * i) / 100
                    if Cap_PSC_A[i] < 0.8 * GLO_CAP_PSC_A[i] and Cap_PSC_A[i] != 0:
                        Cap_PSC_A[i] = 0
                else:
                    if Cap_PSC_A[i] != 0:
                        Cap_PSC_A[i] = Cap_PSC_A[i] - GLO_CAP_PSC_A[i] * (0.667) / 100
                    if Cap_PSC_A[i] < 0.8 * GLO_CAP_PSC_A[i] and Cap_PSC_A[i] != 0:
                        Cap_PSC_A[i] = 0
                i = i + 1
            PSI_new = sum(Cap_PSC_A)
            PSI_deg = PSI_old - PSI_new  # This gives the yearly aging situation
            
            PP_old = sum(Cap_PSC_B)
            k = len(Cap_PSC_B)
            i = 0
            while i < k:
                if i < 6:
                    if Cap_PSC_B[i] != 0:
                        Cap_PSC_B[i] = Cap_PSC_B[i] - GLO_CAP_PSC_B[i] * (1.344 - 0.3567 * i + 0.0646 * i * i - 0.00404 * i * i * i) / 100
                    if Cap_PSC_B[i] < 0.8 * GLO_CAP_PSC_B[i] and Cap_PSC_B[i] != 0:
                        Cap_PSC_B[i] = 0
                else:
                    if Cap_PSC_B[i] != 0:
                        Cap_PSC_B[i] = Cap_PSC_B[i] - GLO_CAP_PSC_B[i] * (0.667) / 100
                    if Cap_PSC_B[i] < 0.8 * GLO_CAP_PSC_B[i] and Cap_PSC_B[i] != 0:
                        Cap_PSC_B[i] = 0
                i = i + 1
            PP_new = sum(Cap_PSC_B)
            PP_deg = PP_old - PP_new
            
            PSIdeg.append(PSI_deg)
            PPdeg.append(PP_deg)
            bb = bb + PSC_deg
            PSCdeg.append(PSC_deg)
            PSCdeg_lj.append(bb)
            PSC_C_exist = PSC_C_exist - PSC_deg  # Aging last year’s, first aging, then investment
            if PSC_C_R < PSC_C_exist:  # PV regression
                ## First, PSC is zero, only processing Si
                print(year)
                PSC_NEW = 0
                PSC_NEW_A = PSC_NEW * R_A(year)
                PSC_NEW_B = PSC_NEW * R_B(year)
                Cap_PSC_A.append(PSC_NEW_A); Cap_PSC_B.append(PSC_NEW_B)
                GLO_CAP_PSC_A.append(PSC_NEW_A); GLO_CAP_PSC_B.append(PSC_NEW_B)
                Cap_PSC.append(PSC_NEW); GLO_CAP_PSC.append(PSC_NEW)
                PSC_C_R = PSC_C_exist
                
                ### Silicon remains unchanged
                if PV_C_R > PV_C_exist:  # Still need new Si PV with this share
                    PV_C_NEW = PV_C_R - PV_C_exist
                    PV_C_exist = PV_C_R
                    
                else:  # Silicon insufficient
                    PV_C_R = PV_C_exist  # Si does not change this year
                    PV_C_NEW = 0

                    
            else:  # Normal operation
                if PV_C_R > PV_C_exist:  # Still need new Si PV with this share
                    PV_C_NEW = PV_C_R - PV_C_exist
                    PV_C_exist = PV_C_R
                    
                    ## Regarding PSC
                    PSC_NEW = PSC_C_R - PSC_C_exist
                    PSC_NEW_A = PSC_NEW * R_A(year)
                    PSC_NEW_B = PSC_NEW * R_B(year)
                    Cap_PSC_A.append(PSC_NEW_A); Cap_PSC_B.append(PSC_NEW_B)
                    GLO_CAP_PSC_A.append(PSC_NEW_A); GLO_CAP_PSC_B.append(PSC_NEW_B)
                    Cap_PSC.append(PSC_NEW); GLO_CAP_PSC.append(PSC_NEW)
                    PSC_C_exist = PSC_C_R
                    
                else:  # Adjust PSC penetration
                    PV_C_R = PV_C_exist  # Si does not change this year
                    PV_C_NEW = 0

                    PSC_C_R = CHINA_SI + CHINA_PSC - PV_C_R  # Adjust PSC target this year
                    if PSC_C_R < PSC_C_exist:
                        PSC_NEW = 0
                        PSC_NEW_A = PSC_NEW * R_A(year)
                        PSC_NEW_B = PSC_NEW * R_B(year)
                        Cap_PSC_A.append(PSC_NEW_A); Cap_PSC_B.append(PSC_NEW_B)
                        GLO_CAP_PSC_A.append(PSC_NEW_A); GLO_CAP_PSC_B.append(PSC_NEW_B)
                        Cap_PSC.append(PSC_NEW); GLO_CAP_PSC.append(PSC_NEW)
                        PSC_C_R = PSC_C_exist
                    else:
                        PSC_NEW = PSC_C_R - PSC_C_exist  # Growth limited by Si market
                        PSC_NEW_A = PSC_NEW * R_A(year)
                        PSC_NEW_B = PSC_NEW * R_B(year)
                        Cap_PSC_A.append(PSC_NEW_A); Cap_PSC_B.append(PSC_NEW_B)
                        GLO_CAP_PSC_A.append(PSC_NEW_A); GLO_CAP_PSC_B.append(PSC_NEW_B)
                        PSC_C_exist = PSC_C_R
                        Cap_PSC.append(PSC_NEW); GLO_CAP_PSC.append(PSC_NEW)
        
        cc = cc + PSC_NEW
        dd = dd + PV_C_NEW

        ## P-SI and PP total investment minus cumulative aging amount
        PSI_TOT = PSI_TOT + PSC_NEW_A
        PSI_OLD = PSI_OLD + PSI_deg
        PSI_EXIST = PSI_TOT - PSI_OLD

        PP_TOT = PP_TOT + PSC_NEW_B
        PP_OLD = PP_OLD + PP_deg
        PP_EXIST = PP_TOT - PP_OLD        
        PPEXIST.append(PP_EXIST)
        PSIEXIST.append(PSI_EXIST)

        nnewsi.append(PV_C_NEW)
        npsc_c_lj.append(cc)
        npsc_c.append(PSC_NEW)
        nsi_c_lj.append(dd)
        nsi_c.append(PV_C_NEW)
        nexist_psc.append(PSC_C_R)
        nexist_si.append(PV_C_R)
        nshare_psc.append(PSC_C_R / dchinasi(year))

    print("PPTOT")
    for i in range(len(PPEXIST)):
        print(PPEXIST[i])
    print("\n")

    print("PSITOT")
    for i in range(len(PSIEXIST)):
        print(PSIEXIST[i])
    print("\n")
