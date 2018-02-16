#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:01:56 2017

@author: jonasfunke
"""

#%%

#from __future__ import (absolute_import, division, print_function, unicode_literals)
import __future__
import numpy #for writing matrices
import matplotlib.pyplot as plt #plotting 


loop_length = 2
domain_length = 2
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
#compute contact matrix
cur_seq = 'ACTGCCTAGCATCAGTATCGATCGATCGATAGCTAGGGATCGATA'#reporter_sequences[0];

contacts = numpy.zeros((len(cur_seq),len(cur_seq)))
for i in range(len(cur_seq)):
    for j in range(i+1, len(cur_seq)):
        if (cur_seq[i]==complement[cur_seq[j]]) and abs(i-j)>loop_length:
            contacts[i][j] = 1
                    
#%
domains = []
for n in range(0, len(contacts)):
    for k in range(0,2):
        #print('-------')
        cur_trace = []
        for m in range(0, min(n+1, len(contacts)-n-k)):
            #print(str(n-m) + ', ' + str(n+m+k))
            i = n-m
            j = n+m+k
         #   print(str(i) + ', ' + str(j) + '     ' + str(n+1) + ',' + str(len(contacts)-n) )
            cur_trace.append(contacts[i][j])
            
        #print(cur_trace)
        
        if len(cur_trace)>0:
            counter = cur_trace[0]
        for i in range(1,len(cur_trace)):
            if cur_trace[i]==0 or i==len(cur_trace)-1:
                if i==len(cur_trace)-1:
                    counter = counter + cur_trace[i]
                if counter>0:
                    domains.append(counter)
                counter = 0
            else:
                counter = counter + cur_trace[i]
           # print(counter)
print(domains)




long_domains = [x for x in domains if x>domain_length]     

plt.matshow(contacts)
plt.show()        



#fig = plt.figure()

plt.hist(long_domains, bins= numpy.arange(0.5, 16.5, 1), histtype='bar') 



