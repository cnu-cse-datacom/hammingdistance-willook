import numpy as np
import pandas as pd
import random

def hamming(a,b):
    return len([i for i in filter(lambda x: x[0] != x[1], zip(a,b))])

def main():
    original_word = input("input words:")
    compare_word = input("input compare words:")
    result = hamming(original_word, compare_word)
    print("different number:",result)


    
  

    
if __name__ == "__main__":
    main()
