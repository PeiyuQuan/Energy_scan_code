import math
import epics
import time
import numpy as np
import random
import matplotlib.pyplot as plt

def scan_energy_1_range(start, step, points, file_name):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC02:m2.VAL")
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    h=[]
    n=[]
    epics.PV("SSRL:Camera27S5M:cam1:ImageMode").put('Single',wait=True)
    epics.PV("SSRL:Camera27S5M:cam1:TriggerMode").put('Off',wait=True)
    epics.PV("SSRL:Camera27S5M:ROIStat1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("SSRL:Camera27S5M:ROIStat1:1:Use").put('Yes',wait=True)
    init_image_number= epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True)
    for i in range(0, points):
        mono = start + step*i
        a.append(mono)
        m1 = 2*dspacing*mono
        n.append(i+1)
        crystal = math.asin(hc/m1)
        angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
        crystal_1.put(angle_crystal, wait=True)
        c.append(epics.PV("SSRL:Camera27S5M:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("SSRL:Camera27S5M:cam1:Acquire").put('Acquire')
        time.sleep(0.5)
        b.append(epics.PV("SSRL:Camera27S5M:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(epics.PV("BL62:DMC01:m4.RBV").get(as_numpy=True))
    f = open(file_name, "a")
    f.write("#\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
    for m in range(0,len(a)):
        f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], d[m], e[m], a[m], b[m], c[m], h[m]))
    fina_image_number= epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True)-1
    time.sleep(1)
    x=a
    y=b
    plt.plot(x,y,marker="o", ms=6)
    plt.title(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True)+" "+"scan #"+str(init_image_number)+"~"+str(fina_image_number))
    plt.xlabel('energy')
    plt.ylabel('Intensity from camera ROI')
    plt.show()

def scan_energy_2_ranges(start, step, points, start1, step1, points1, file_name):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC02:m2.VAL")
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    h=[]
    n=[]
    epics.PV("SSRL:Camera27S5M:cam1:ImageMode").put('Single',wait=True)
    epics.PV("SSRL:Camera27S5M:cam1:TriggerMode").put('Off',wait=True)
    epics.PV("SSRL:Camera27S5M:ROIStat1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("SSRL:Camera27S5M:ROIStat1:1:Use").put('Yes',wait=True)
    init_image_number= epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True)
    for i in range(0, points):
        mono = start + step*i
        a.append(mono)
        m1 = 2*dspacing*mono
        n.append(i+1)
        crystal = math.asin(hc/m1)
        angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
        crystal_1.put(angle_crystal, wait=True)
        c.append(epics.PV("SSRL:Camera27S5M:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("SSRL:Camera27S5M:cam1:Acquire").put('Acquire')
        time.sleep(0.5)
        b.append(epics.PV("SSRL:Camera27S5M:ROIStat1:1:Total_RBV").get(as_numpy=True)) 
        h.append(epics.PV("BL62:DMC01:m4.RBV").get(as_numpy=True))
    for i in range(0, points1):
        mono = start1 + step1*i
        a.append(mono)
        m1 = 2*dspacing*mono
        n.append(i+points+1)
        crystal = math.asin(hc/m1)
        angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
        crystal_1.put(angle_crystal, wait=True)
        c.append(epics.PV("SSRL:Camera27S5M:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("SSRL:Camera27S5M:cam1:Acquire").put('Acquire')
        time.sleep(0.5)
        b.append(epics.PV("SSRL:Camera27S5M:ROIStat1:1:Total_RBV").get(as_numpy=True)) 
        h.append(epics.PV("BL62:DMC01:m4.RBV").get(as_numpy=True))
    f = open(file_name, "a")
    f.write("#\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
    for m in range(0,len(a)):
        f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], d[m], e[m], a[m], b[m], c[m], h[m]))
    fina_image_number= epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True)-1
    time.sleep(1)
    x=a
    y=b
    plt.title(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True)+" "+"scan #"+str(init_image_number)+"~"+str(fina_image_number))
    plt.plot(x,y,marker="o", ms=6)
    plt.xlabel('energy')
    plt.ylabel('Intensity from camera ROI')
    plt.show()

def scan_energy_3_ranges(start, step, points, start1 , step1, points1, start2, step2, points2, file_name):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC02:m2.VAL")
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    h=[]
    n=[]
    epics.PV("SSRL:Camera27S5M:cam1:ImageMode").put('Single',wait=True)
    epics.PV("SSRL:Camera27S5M:cam1:TriggerMode").put('Off',wait=True)
    epics.PV("SSRL:Camera27S5M:ROIStat1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("SSRL:Camera27S5M:ROIStat1:1:Use").put('Yes',wait=True)
    init_image_number= epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True)
    for i in range(0, points):
        mono = start + step*i
        a.append(mono)
        m1 = 2*dspacing*mono
        n.append(i+1)
        crystal = math.asin(hc/m1)
        angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
        crystal_1.put(angle_crystal, wait=True)
        c.append(epics.PV("SSRL:Camera27S5M:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("SSRL:Camera27S5M:cam1:Acquire").put('Acquire')
        time.sleep(0.5)
        b.append(epics.PV("SSRL:Camera27S5M:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(epics.PV("BL62:DMC01:m4.RBV").get(as_numpy=True))
    for i in range(0, points1):
        mono = start1 + step1*i
        a.append(mono)
        m1 = 2*dspacing*mono
        n.append(i+points+1)
        crystal = math.asin(hc/m1)
        angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
        crystal_1.put(angle_crystal, wait=True)
        time.sleep(0.2)
        c.append(epics.PV("SSRL:Camera27S5M:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("SSRL:Camera27S5M:cam1:Acquire").put('Acquire')
        time.sleep(0.5)
        b.append(epics.PV("SSRL:Camera27S5M:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(epics.PV("BL62:DMC01:m4.RBV").get(as_numpy=True))
    for i in range(0, points2):
        mono = start2 + step2*i
        a.append(mono)
        m1 = 2*dspacing*mono
        n.append(i+1+points+points1)
        crystal = math.asin(hc/m1)
        angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
        crystal_1.put(angle_crystal, wait=True)
        c.append(epics.PV("SSRL:Camera27S5M:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("SSRL:Camera27S5M:cam1:Acquire").put('Acquire')
        time.sleep(0.5)
        b.append(epics.PV("SSRL:Camera27S5M:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(epics.PV("BL62:DMC01:m4.RBV").get(as_numpy=True))
    f = open(file_name, "a")
    f.write("#\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
    for m in range(0,len(a)):
        f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], d[m], e[m], a[m], b[m], c[m], h[m]))
    fina_image_number= epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True)-1
    time.sleep(1)
    x=a
    y=b
    plt.title(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True)+" "+"scan #"+str(init_image_number)+"~"+str(fina_image_number))
    plt.plot(x,y,marker="o", ms=6)
    plt.xlabel('energy')
    plt.ylabel('Intensity from camera ROI')
    plt.show()

def scan_energy_4_ranges(start, step, points, start1 , step1, points1, start2, step2, points2, start3 , step3, points3, file_name):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC02:m2.VAL")
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    h=[]
    n=[]
    epics.PV("SSRL:Camera27S5M:cam1:ImageMode").put('Single',wait=True)
    epics.PV("SSRL:Camera27S5M:cam1:TriggerMode").put('Off',wait=True)
    epics.PV("SSRL:Camera27S5M:ROIStat1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("SSRL:Camera27S5M:ROIStat1:1:Use").put('Yes',wait=True)
    init_image_number= epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True)
    for i in range(0, points):
        mono = start + step*i
        a.append(mono)
        m1 = 2*dspacing*mono
        n.append(i+1)
        crystal = math.asin(hc/m1)
        angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
        crystal_1.put(angle_crystal, wait=True)
        c.append(epics.PV("SSRL:Camera27S5M:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("SSRL:Camera27S5M:cam1:Acquire").put('Acquire')
        time.sleep(0.5)
        b.append(epics.PV("SSRL:Camera27S5M:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(epics.PV("BL62:DMC01:m4.RBV").get(as_numpy=True))
    for i in range(0, points1):
        mono = start1 + step1*i
        a.append(mono)
        m1 = 2*dspacing*mono
        n.append(i+1+points)
        crystal = math.asin(hc/m1)
        angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
        crystal_1.put(angle_crystal, wait=True)
        c.append(epics.PV("SSRL:Camera27S5M:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("SSRL:Camera27S5M:cam1:Acquire").put('Acquire')
        time.sleep(0.5)
        b.append(epics.PV("SSRL:Camera27S5M:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(epics.PV("BL62:DMC01:m4.RBV").get(as_numpy=True))
    for i in range(0, points2):
        mono = start2 + step2*i
        a.append(mono)
        m1 = 2*dspacing*mono
        n.append(i+1+points+points1)
        crystal = math.asin(hc/m1)
        angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
        crystal_1.put(angle_crystal, wait=True)
        c.append(epics.PV("SSRL:Camera27S5M:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("SSRL:Camera27S5M:cam1:Acquire").put('Acquire')
        time.sleep(0.5)
        b.append(epics.PV("SSRL:Camera27S5M:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(epics.PV("BL62:DMC01:m4.RBV").get(as_numpy=True))
    for i in range(0, points3):
        mono = start3 + step3*i
        a.append(mono)
        m1 = 2*dspacing*mono
        n.append(i+1+points+points1+points2)
        crystal = math.asin(hc/m1)
        angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
        crystal_1.put(angle_crystal, wait=True)
        c.append(epics.PV("SSRL:Camera27S5M:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("SSRL:Camera27S5M:cam1:Acquire").put('Acquire')
        time.sleep(0.5)
        b.append(epics.PV("SSRL:Camera27S5M:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(epics.PV("BL62:DMC01:m4.RBV").get(as_numpy=True))
    f = open(file_name, "a")
    f.write("#\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
    for m in range(0,len(a)):
        f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], d[m], e[m], a[m], b[m], c[m], h[m]))
    fina_image_number= epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True)-1
    x=a
    y=b
    plt.title(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True)+" "+"scan #"+str(init_image_number)+"~"+str(fina_image_number))
    plt.plot(x,y,marker="o", ms=6)
    plt.xlabel('energy')
    plt.ylabel('Intensity from camera ROI')
    plt.show()
    
    


