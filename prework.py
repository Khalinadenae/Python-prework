#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 

import numbers
from tabnanny import check


def hello_name(user_name):

         print(f"Hello {user_name}!")

hello_name("kdb033")
       
        
#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for i in range(1,101):
        if i % 2 != 0:
            print(i)
            continue

first_odds()
        
#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
numbers=list(range(3,99))

def max_num_in_list(a_list):
    return max(a_list)

max_num_in_list(numbers)


#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).


def is_leap_year(a_year):
#leap year is divisible by 4, but not divisible by 100 unless it is divisible by 400
    if (a_year % 4 == 0) and (a_year % 100 != 0) or (a_year % 400 == 0) :
     return True 
    else: 
     return False 
    
is_leap_year(1988)
               
#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(list_a):
    return sorted(list_a) == list(range(min(list_a), max(list_a)+1))

numbers=[4,90,8,7,6,45,66,79,0,1,4]
is_consecutive(numbers)

print(is_consecutive(numbers))
 