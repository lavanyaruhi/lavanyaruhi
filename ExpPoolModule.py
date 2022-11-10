import multiprocessing
import time

def square(x):
    return x*x

if __name__=='__main__':

    #creating multiprocessesing pool object
    pool=multiprocessing.Pool()
    # pool object with number of elements
    pool=multiprocessing.Pool(processes = 4)
    # input list
    inputs=[0,1,2,3,4]
    #map the function to the list and pass
    # functions and input list as arguments
    outputs=pool.map(square,inputs)
    #print input list
    print("Inputs: {}".format(inputs))
    #print output list
    print("Outputs: {}".format(outputs))
