import math
import epics
import time
import numpy as np
import matplotlib.pyplot as plt

def scan_rotation_stage(start, step, points, mono, file_name):
    rotation_stage = epics.PV("BL62:DMC01:m4.VAL")
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
        stage_position = start + step*i
        a.append(stage_position)
        n.append(i+1)
        rotation_stage.put(stage_position, wait=True)
        c.append(epics.PV("SSRL:Camera27S5M:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("SSRL:Camera27S5M:cam1:Acquire").put('Acquire',wait=True)
        b.append(epics.PV("SSRL:Camera27S5M:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(mono)
        time.sleep(0.5)
    f = open(file_name, "a")
    f.write("\timage_name\timage_number\trotation_angle\tintensity\texposure_time\renergy\n")
    for m in range(0,len(a)):
        f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], d[m], e[m], a[m], b[m], c[m], h[m]))
    fina_image_number= epics.PV("SSRL:Camera27S5M:HDF1:FileNumber_RBV").get(as_numpy=True)-1
    time.sleep(1)
    x=a
    y=b
    plt.plot(x,y,marker="o", ms=6)
    plt.title(epics.PV("SSRL:Camera27S5M:HDF1:FileName_RBV").get(as_string=True)+" "+"scan #"+str(init_image_number)+"~"+str(fina_image_number))
    plt.xlabel('rotation_angle')
    plt.ylabel('Intensity from camera ROI')
    plt.show()

