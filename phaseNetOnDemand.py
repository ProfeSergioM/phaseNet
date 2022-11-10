# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:00:51 2022

@author: sergio.morales
"""



mseed='mseed_files/'


from obspy import read
import os,shutil
with open("fname.csv", 'w') as fp:
    fp.write("fname,Z,N,E\n")
    for file in os.listdir(mseed):
        wavefile = read(mseed+'/'+file)
        channels=''
        for wave in wavefile:
            channels = channels+','+wave.stats.channel
        fp.write(file+channels+"\n")
os.system("python PhaseNet-master/phasenet/predict.py --model=PhaseNet-master/model/190703-214543 "+
          "--data_list=fname.csv --data_dir="+mseed+" --format=mseed --plot_figure")  
if os.path.isfile('results/picks.csv'): 
    shutil.copy('results/picks.csv','phases/detections.csv')
    os.remove('results/picks.csv')  
for file in os.listdir('results/figures'):
    filefull = (os.path.join('results/figures', file))
    shutil.copy(filefull, 'phases/'+file)
