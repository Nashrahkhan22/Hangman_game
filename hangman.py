# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 06:20:54 2019

@author: Nashrah
"""
#step 1 imorting and random
import random
print("This is Hangman game,\nTotal lives=4")
list=["pea","mango","orange"]
x=random.choice(list)

#step=2 slpiting the word in list and joining amd for __
m=" ".join(x)
l=m.split()

m=["__"]
for r in range(len(l)-1):
     m.append("__")
f=[]
f=l.copy()

#step 5 display and then play
display(x)
play(x)

#Ste 3 hints
def display(x): 
    if x=="pea":
        print("Hint:I am green in color,bulb shaped fruit")   
    elif x=="mango":  
        print("Hint:I am yellow in color,fruit")  
    else: 
        print("Hint:I am orange in color,fruit") 

#step 4 game played
count=3
n=[]
def play(x):    
   print("Enter the letter")
   print(m) 
   global count
   while count>0:
        z=input()
        if z in l:
         
            #find index of l and equlas in with m and relace that index
            indexfind=l.index(z)
            
            
            if z in f and z in l:
                f.remove(z)
                m.remove("__")
                m.insert(indexfind,z)
                print(m)
                n.append(z)
            else:
                print("You repeated")
            if len(n)==len(l):
                print("You are Winner")
                break
            continue
            
        else:
            count=count-1     
            print("Your lives left "+ str(count))
            play(x)  
           
            print("Game Over")
     
                 
                 
            

  
    
       
