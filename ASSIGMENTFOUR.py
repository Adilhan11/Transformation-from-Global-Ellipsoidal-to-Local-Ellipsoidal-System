# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 21:52:36 2022

@author: Asus
"""
from ASSIGMENTTHREE import xyz2blh
import math 
# Adilhan KOÇAK 2200674035 
# 26.12.2022
#This function be able to Transformation from Global Ellipsoidal to Local Ellipsoidal System.
#INPUT = [PX,PY,PZ] 3D coordinates (𝑥𝑃, 𝑦𝑃, 𝑧𝑃) of the target point
#INPUT = [RX,RY,RZ] 3D coordinates (𝑥𝑃, 𝑦𝑃, 𝑧𝑃) of the observation point
#OUTPUT = [azimuth,zenith,slant range] COORDINATES OF ELLIPSOIDAL COORDINATE SYSTEM
#PX,PY,PZ and RX,RY,RZ and s ======> meters format
#azimuth and zenith ======> degree format
#azim – ellipsoidal azimuth angle between [0, 360 degree]
#zen – ellipsoidal zenith angle between [0, 180 degree]
#NOTE:I GET ASSIGMENT3 FUNCTİON BUT RADİAN FORMAT.
def global2local(P,R):
    #I defined  assıgment 3 function for observation point to get lon and lat angle  
    llh = xyz2blh((R[0]),(R[1]),(R[2]))
    lat = llh[0]
    lon = llh[1]

    #DELTAX MATRİX difference point values P and R
    K = [P[0]-R[0],P[1]-R[1],P[2]-R[2]]
    
    #A^-1 matrix X K martix
    x = -((math.sin(lat)*math.cos(lon)*K[0])+(math.sin(lat)*math.sin(lon)*K[1])+(math.cos(lat)*K[2]))
    y = -(math.sin(lon)*K[0])              +       (math.cos(lon)*K[1])      +            0
    
    z = +(math.cos(lat)*math.cos(lon)*K[0])+ (math.cos(lat)*math.sin(lon)*K[1]) + (math.sin(lat)*K[2])
    #slant range
    
    s = math.sqrt(((P[0]-R[0])**2)+((P[1]-R[1])**2)+((P[2]-R[2])**2))
    #zenith and azimuth angle formulas
    zen = math.acos(z/s)
    az = math.asin(y/(s*math.sin(zen)))
    
    #convert degree format
    az = -(math.degrees(az) - math.degrees(math.pi))
    zen = math.degrees(zen)
    
    #check value
    if (0<=az and az<=360) and (0<=zen and zen<=180):
            return [az,zen,s]
    else:
        return "HATA"
    
a = global2local([21007733.6107 ,15033152.8348 ,-7112458.1231], [4208830.726  ,2334850.0235  ,4171267.089])
print(f"azimuth : {a[0]} zenith : {a[1]} slant range: {a[2]}")