import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint # print beautifully

usercommand = "Yes"
while (usercommand != "No"):
    print("How many elements?")
    num_elements = int(input())
    filenamelist = [""] * num_elements * 2 # Use this list to store filenames of PDOS.
    print("Please type in the elements, press enter after type each element.")
    for i in range(num_elements):
        element_name = input()
        index = i*2
        filenamelist[index] = "PDOS_" + element_name + "_DW.dat"
        filenamelist[index+1] = "PDOS_" + element_name + "_UP.dat"
    print("The following PDOS files are being plotted.")
    print(filenamelist)
    datalist = [""] * num_elements * 2
    for i in range(len(datalist)):
        datalist[i] = pd.read_table(filenamelist[i], delim_whitespace = True)
        datalist[i]['d'] = datalist[i]['dxy'] + datalist[i]['dyz'] + datalist[i]['dz2'] + datalist[i]['dxz'] + datalist[i]['dx2']
        datalist[i]['p'] = datalist[i]['px'] + datalist[i]['py'] + datalist[i]['pz']
        datalist[i].to_csv(filenamelist[i] + ".csv")
    print("Do you want to continue? (Yes/No)")
    usercommand = input()
    
