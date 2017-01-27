import re
import ast

def count_compr_length(string):
    #print "complen",len(string)
    return len(string)
    
def count_full_length(string):
    string=string.rstrip('\n')
    


    #return len(string)+quotes+backslash+ascii+2
    print len(string)
    
#print ast.literal_eval("\"cacca\x54a")
var='\"cacca\x54a'
var2="%r"%var
print var2
print count_compr_length(var2)
count_full_length(var2)

#print re.findall(r"[\x00-\xff]","\x27")


def count_diff(filename):
    full=0
    compr=0
    s=""
    with open(filename) as f:
        for line in f:
            s=line.rstrip('\n')
            #print repr(line)
            full+=count_full_length(s)
            compr+=count_compr_length(s)
            
    return full-compr
    
#print count_diff("D:/varie/adventcode/input8a.txt")
        

