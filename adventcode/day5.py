import re

def check_vowels(string):
    count=0
    
    for c in string:
        if c in "aeiouAEIOU":
            count+=1
            
    return count>=3
    

def check_rep(string):
    prev=''
    for c in string:
        if c==prev:
            return True
        else:
            prev=c
    return False
    
def check_substring(string):
    return ('ab' not in string) and ('cd' not in string) and ('pq' not in string) and ('xy' not in string)

def check_nice_string(string):    
    if check_vowels(string) and check_rep(string) and check_substring(string):
        return True
    else:
        return False

def count_nice_strings(filename):
    count=0
    
    with open(filename) as f:
        for line in f:
            count+=check_nice_string(line)
    return count
            
#print check_nice_string("aaa")
print count_nice_strings("D:/varie/adventcode/input5.txt")