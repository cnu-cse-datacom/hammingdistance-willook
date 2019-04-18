import numpy as np
import pandas as pd
import random
from hamming_parctice import hamming

def hamming(a,b):
    return len([i for i in filter(lambda x: x[0] != x[1], zip(a,b))])


def main():
    df = pd.read_csv('sample.csv',names=['word', bin])
    print()
    min = -1
    count  = 1
    length = df.shape[0]
    #length = 10
    #print(df.size)
    for i in range(length-1):
        for j in range(i+1, length):
            #print(i,j)
            hd = hamming(df.iloc[i,1],df.iloc[j,1])
            print(count,"(",df.iloc[i,0],df.iloc[j,0],")hamming_distance:",hd)
            if min == -1 or min > hd:
                min = hd;
            count += 1
    print("min hamming distance", min)    
    
  

    
if __name__ == "__main__":
    main()
