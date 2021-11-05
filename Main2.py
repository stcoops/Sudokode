import random
import math
import numpy as np

def transpose(mat):
    new=[]
    mew=[] # I mean i got this far without importing Numpy...
    for x in range(len(mat[0])):
        for y in range(len(mat)):
            new.append(mat[y][x])
        mew.append(new)
        new = []
    return mew

def vectorfix(matrix):
    if type(matrix[0]) == int:
        new = []
        new.append(matrix)
        return new
    else:
        return(matrix)


#def dot(matA,matB):
#    vectorfix(matA)
#    vectorfix(matB)
#    #initialize res(ult) matrix
#    res = []
#    w = []
#    for y in range(len(matB[0])):
#        w.append(0)
#    for x in range(len(matA)):
#        res.append(w)
#    for x in range(len(matA)):
#        for y in range(len(matB[0])):
#            for z in range(len(matB)):
#                res[x][y]+= matA[x][z] * matB[z][y]
#    return res

#print(dot([[1,1],[1,1]],[[1,1],[1,1]]))
class neuron:
    def __init__(self,inp):
        self.weights=[]
        #for x in range(inp):
        #    self.weights.append(random.uniform(-10,10))
        #self.bias = random.randint(-100,100)

        for x in range(inp):
            self.weights.append(2)
        self.bias = 2

    def calc(self,inputs):
        t = 0 
        for x in range(len(inputs)):
            t += inputs[x]*self.weights[x]
        t+=self.bias
        relu(t)
        return t

class Network:
    def __init__(self, dim):
        self.dim = dim
        net = []
        lay = []
        for x in range(len(dim)):
            for y in range(dim[x]):
                lay.append(neuron(dim[x-1]))
            net.append(lay)
            lay = []
        self.net = net
            
def run(network, inputs):
    for layer in range(len(network.dim)-1):
        output = []
        for y in range(network.dim[layer+1]):
            out = network.net[layer+1][y].calc(inputs)
            output.append(out)
        inputs = output
    return output   

def cost(output, solution):
    t = 0
    for x in range(len(output)):
        t+=(output-solution)**2
    return t #NOTE: research the difference between these NOTE NOTE

def error(output, solution):
    return  (output-solution)


#Activation Functions
def relu(x):
    if x > 0:
        return x
    else:
        return 0

def relu_d(x):
    if x < 0:
        return 0
    else:
        return 1

def sigmoid(x): #Sigmoid Activation Function
    return 1 / (1 + math.exp(-x))

def sigmoid_d(x): #Sigmoid Derivative
    return x * (1.0 - x)

def leaky_relu(x):
    if x > 0:
        return x
    else:
        return 0.01*x
    
def back_prop(network, output, solution):
    error = output-solution
    adjustments = error * sigmoid_d(output)
    synaptic weights += np.dot(input_layer.transpose, adjustments)

network = Network([1,2,2,1])
#print(run(network, [1]))