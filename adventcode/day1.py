def count_floor(input):
    floor=0
    
    for char in input:
        if char == '(':
            floor+=1
        elif char == ')':
            floor -=1
    
    return floor
    
def input_floor(filename):
    
    f=open(filename,"r")
    input=f.read()
    f.close()
    return count_floor(input)
    
print input_floor("D:/varie/adventcode/input1.txt")