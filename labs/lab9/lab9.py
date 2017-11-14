import numpy as np
import pandas as pd
import math
import random


class AssociationRule(object):
    
    def __init__(self, trans, minsup, k):
        self.trans = trans
        self.minsup = minsup
        self.kitemset = {}  # key k is number-of-elements-per-itemset. value are these k-itemset.
        self.k = k
        
    def count(self, itemset):    
        # Return count of one itemset in all transactions
        # Your code goes here:
        pass
        
    
    
    def support(self, itemset):
        # Retuen support of one itemset
        # Your code goes here:
        pass
        
        
    
    def generate(self, kitemset):
        # Generate candidate of itemset in next level of the tree using F_k-1 * F_k-1 method.
        # Merge two frequent itemsets in length of k-1 to get a new candidate itemset in length of k.
        # Suppose here we have two itemsets in length of n: Itemseta = [a1, a2, ... , an] and Itemsetb = 
        #    [b1, b2, ... , bn]. We merge Itemseta and Itemsetb if all first n-1 elements of them are same
        #    except the last elements of them are different. Mathematically, a new candidate item
        #    Itemset_New = [a1, a2, a3, ..., an, bn] only if a1=b1, a2=b2, ..., a_n-1=b_n-1, but an != bn.
        
        # Your code goes here:
        pass
        
        
        
    
    def run(self):
        # Find all frequent itemsets and store them in the dictionary self.kitemset
        # You code goes here:
        pass
    
    
    
        
    def getdata(self):
        # Update test data
        random.seed(1)
        row = 100
        trans = []
        for i in range(row):
            col = random.randint(1,100)
            trans.append(list(set([random.randint(1,30) for i in range(col)]))) 
        self.trans = trans
            
    def printset(self,k):
        print str(k) + "-itemset contains:"
        for itemset in self.kitemset[k]:
            print itemset
    
if __name__ == "__main__":
    
    minsup = 0.5
    
    # data set 1 
    trans = [["Bread", "Milk"], 
             ["Bread", "Diaper", "Beer", "Eggs", "Milk"],
             ["Milk", "Diaper", "Beer", "Coke"],
             ["Bread", "Milk", "Diaper", "Beer"],
             ["Bread", "Milk", "Diaper", "Coke"]]
    k = 3
    model = AssociationRule(trans, minsup, k)
    model.run()
    model.printset(k)
    
    # data set 2
    k = 5
    model = AssociationRule(None, minsup, k)
    model.getdata()
    model.run()
    model.printset(k)
    
    