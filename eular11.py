# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:24:58 2017

@author: Saloni.Kothari
"""
sum=0

def get_divisors(num):
    divisors = []
    for i in range(1,num):
        if num % i == 0:
            divisors.append(i)
    divisors.append(num)
    return divisors
#divisors = get_divisors(45)
#print(divisors)
#print(len(divisors))

for i in range(1,10000):
    sum=sum+i
    print(sum," :",end='')
    divisors=get_divisors(sum)
    #print(divisors,"\t",end='')
   # if len(divisors)<500:
       # break
    #print(sum)
    
    
    print("count is",len(divisors))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ''''for i in range(1,sum+1):
        if sum%i==0:
            count+=1
            print("\t",i)
            
    
         

   # if sum%i==0:
       # print(sum)
       
   '''
'''for i in range(1, sum-1):
		 if sum%i == 0:
				print("number and factor is %s %s",sum,i)
            	
				i += 1'''


