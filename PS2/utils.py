############################## PROBLEM 3 CODE HERE ##############################
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import warnings
sns.set_palette("Blues_d")

from IPython.display import HTML

# import the widgets module
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual

warnings.filterwarnings("ignore")
#sns.set(style="whitegrid")

def make_count(count, number):
    return np.array([np.ones(count) * number])

def make_count_array(counts):
    bases = [-2, -1, 0, 1, 2]
    arr = np.array([])
    for i, j in zip(counts, bases):
        arr = np.append(arr, make_count(i, j))
    return np.array([int(i) for i in arr])

politicalStances = {-2: 'Extreme Left', -1:'Moderate Left', 0:'Centrist',
                   1:'Moderate Right', 2:'Extreme Right'}
colors = {-2:'blue', -1:'blue', 0:'black', 1:'red', 2:'red'}

def make_color_arr(dta):
    arr = []
    for i in dta:
        arr.append(colors[i])
    return arr

def plot_voters(counts):
    pos = [] 
    keys = {} # this dict will help to keep track ...

    data = make_count_array(counts)

    # this loop will give us a list of frequencies to each number
    for num in data: 
        if num not in keys:
            keys[num] = 1
            pos.append(1)
        else:
            keys[num] += 1
            pos.append(keys[num])


    for key, value in zip(keys.keys(), keys.values()):
        print('There are ' + str(value) + ' ' + politicalStances[key] + 
              ' (' + str(key) + ') ' + 'voters')

    colorArr = make_color_arr(data)

    plt.scatter(data, pos, c=colorArr)
    plt.grid(False)
    plt.xticks([-2, -1, 0, 1, 2])
    plt.show()

def plot_voters_candidates(counts, candA, candB):
    
    pos = [] 
    keys = {} # this dict will help to keep track ...
    
    data = make_voter_array(counts)
    voting = {}
    candidates = {'candA': 'Candidate A', 'candB': 'Candidate B'}

    # this loop will give us a list of frequencies to each number
    for num in data: 
        if num not in keys:
            keys[num] = 1
            pos.append(1)
        else:
            keys[num] += 1
            pos.append(keys[num])
    
    voter_pos = set(data)
    for i in voter_pos:
        if i == 0:
            voting[i] = np.random.choice(['candA', 'candB'], 
                                         p=[0.5, 0.5])
            continue
        diffA = abs(i - candA)
        diffB = abs(i - candB)
        if diffA < diffB:
            voting[i] = 'candA'
        elif diffB == diffA:
            #distributing the voters 
            voting[i] = ('candA', 'candB')        
        else:
            voting[i] = 'candB'
        

    for key, value in zip(keys.keys(), keys.values()):
        who_voting = voting[i]
        half = False
        if type(who_voting) == tuple:   
            half = True 
        if half == False: 
            print('There are ' + str(value) + ' ' + politicalStances[key] + 
                  ' (' + str(key) + ') ' + 'voters who will vote for ' + candidates[who_voting])
        else:
            print(politicalStances[key] + ' voters are indifferent about candidates. Half will go to' + 
                  ' Candidate A, half with Candidate B')
            half = False
            int_value = value // 2
            someInt = np.random.choice([0, 1], p=[0.5, 0.5])
            remainder = value % 2
            if int_value == 0:
                who_voting_now = np.random.choice(['Candidate A','Candidate B'], p=[.5, .5])
                print('There are ' + str(value) + ' ' + politicalStances[key] + 
                      ' (' + str(key) + ') ' + 'voters who will vote for ' + who_voting_now)
                continue
            if half == False:
                who_voting_now = who_voting[0]
                if someInt == 0: 
                    numVoters = int_value + remainder
                else:
                    numVoters = int_value
                print('There are ' + str(numVoters) + ' ' + politicalStances[key] + 
                  ' (' + str(key) + ') ' + 'voters who will vote for ' + candidates[who_voting_now])
                half = True
            if half == True:
                who_voting_now = who_voting[1]
                if someInt == 1: 
                    numVoters = int_value + remainder
                else: 
                    numVoters = int_value
                print('There are ' + str(numVoters) + ' ' + politicalStances[key] + 
                  ' (' + str(key) + ') ' + 'voters who will vote for ' + candidates[who_voting_now])

                

    
        
    colorArr = make_color_arr(data)
    
            
    plt.scatter(data, pos, c=colorArr)
    plt.grid(False)
    plt.xticks([-2, -1, 0, 1, 2])
    
    plt.scatter([candA, candB], [0, 0], c=['gold', 'lime'])
    plt.annotate('Candidate A', (candA, 0), (candA, 20), arrowprops=dict(arrowstyle='wedge', 
                                                                   connectionstyle='arc3, rad=0.2'))
    plt.annotate('Candidate B', (candB, 0), (candB, 10), arrowprops=dict(arrowstyle='wedge', 
                                                                   connectionstyle='arc3, rad=-0.2'))
    
    
    
    plt.show()
    
    
    
    plt.show()
