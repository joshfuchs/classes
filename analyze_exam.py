#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:56:59 2017

@author: Josh Fuchs, Texas Lutheran University

This program will read in a csv file of exam (or other) scores and make 
relevant plots
"""

import numpy as np
import matplotlib.pyplot as plt


import os
#os.chdir('/Users/jfuchs/Documents/Classes/Phys141/Archive/2017_Fall/Exams/Exam1/')

#Read in the csv file
#filename = 'test.txt'
filename = raw_input('Enter file name: ')

#ID, student_name, version, q1, q2, q3, q4, q5, q6, q7, score_total = np.genfromtxt(filename,unpack=True,filling_values='Nan')
sheet = np.genfromtxt(filename,delimiter = '\t',skip_header=1)
#This is in the format [row,column]
#print type(sheet)
#print sheet.shape

#print sheet[0,:]
#print sheet[:,0]

#######################################
#Make histogram showing percentage correction
#######################################
avg_scores = sheet[-5,:-1]/ sheet[-6,:-1]
std_scores = sheet[-3,:-1]/ sheet[-6,:-1]
x_pos = 1.+ np.arange(len(avg_scores))


plt.clf()
plt.figure(figsize=(12, 9))
plt.bar(x_pos,avg_scores,yerr=std_scores,capsize=10,align='center',color="#3F5D7D")
plt.xticks(x_pos,x_pos,fontsize=16)
plt.yticks(fontsize=16)  
ax = plt.subplot(111)  
ax.spines["top"].set_visible(False)  
ax.spines["right"].set_visible(False)
plt.ylabel('Average Score',fontsize=16)
plt.xlabel('Problem Number',fontsize=16)
plt.title('Pecentage Correct by Problem',fontsize=16)
plt.savefig('Percentage.png',bbox_inches='tight')
#plt.show()





#######################################
#Make plots showing correlation value and quality factor
#######################################
correlation = sheet[-2,:-1]
quality = sheet[-1,:-1]
x_posi = 1. + np.arange(len(quality))

plt.clf()
f, axarr = plt.subplots(2,sharex=True,figsize=(12,9))
axarr[0].plot(x_posi,correlation,'ks',markersize=16)
#axarr[0].set_title('Problem Number',fontsize=16)
axarr[1].plot(x_posi,quality,'ks',markersize=16)
axarr[0].set_ylabel('Correlation',fontsize=16)
axarr[1].set_ylabel('Quality',fontsize=16)
axarr[1].set_xlabel('Problem Number',fontsize=16)
plt.xticks(np.arange(min(x_posi),max(x_posi)+1,1.0),fontsize=16)
plt.yticks(fontsize=16)
plt.savefig('Quality.png',bbox_inches='tight')
#plt.show()




#######################################
#Make plot showing histogram of total scores
#######################################
total_score = sheet[:-6,-1]
total_average = np.mean(total_score)
bins = [30,40,50,60,70,80,90,100]
plt.clf()
plt.figure(figsize=(12, 9))  
ax = plt.subplot(111)  
ax.spines["top"].set_visible(False)  
ax.spines["right"].set_visible(False)  
plt.xticks(fontsize=16)  
plt.yticks(fontsize=16)  
plt.hist(total_score,bins=bins,color="#3F5D7D")
plt.axvline(total_average,color='k',linestyle='dashed',linewidth=4)
plt.xlabel('Total Score',fontsize=16)
plt.ylabel('Number',fontsize=16)
plt.savefig("histogram.png", bbox_inches="tight")
