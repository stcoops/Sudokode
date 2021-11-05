# Imports
#import tensorflow as tf
import pandas as pd
from pandas.core.frame import DataFrame
import numpy as np
from    tensorflow.keras import datasets, layers, optimizers, Sequential, metrics
#import matplotlib as mpl
#import tkinter as tk
#import time
#
def unscientify(num):
    numarr = num.split("E")
    return numarr[0] * (10 **numarr[1])

def bigtings():
    data = pd.read_csv("test.csv")
    try:
        data = pd.DataFrame({"quizzes":data["puzzle"],"solutions":data["solution"]})
    except:
        pass
    data.head()
    print("Quiz:\n",np.array(list(map(int,list(data['quizzes'][0])))).reshape(9,9))
    print("Solution:\n",np.array(list(map(int,list(data['solutions'][0])))).reshape(9,9))

bigtings()


def dataInit():
    dataset = pd.read_csv("test.csv")
    puzzle = dataset.drop(columns="solution")
    #print(puzzle)
    #print(type(puzzle))
    for x in range(len(puzzle)):
        dat = str(np.int(puzzle.iat[x, 0]))
        while len(dat) < 81:
            dat = "0" + dat
        print(dat)
        datArr = ([c for c in dat])
        #print(datArr)
        y=0
        a=0 
        b=0
        bigarr = []
        minarr = [None,None,None,None,None,None,None,None,None]
        for w in range(9):
            bigarr.append(minarr)
        #print(bigarr)
        while True:
            if a == 9:
                b+=1
                a = 0
            if b == 9:
                break
            
            bigarr[a][b] = datArr[y]
            y+=1
            a+=1
        #print(bigarr)

#dataInit()

def get_model():
    # Create a simple model.
    net = Sequential([layers.Dense(82, activation='relu'),layers.Dense(82, activation='relu'),layers.Dense(81)])
    net.build(input_shape=(None, 81))
    net.summary()
    #inputs = keras.Input(shape=(32,))
    #outputs = keras.layers.Dense(1)(inputs)
    #model = keras.Model(inputs, outputs)
    #model.compile(optimizer="adam", loss="mean_squared_error")
    #return model
#get_model()