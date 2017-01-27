def calculate_single_paper(dim):
    
    dim_list=dim.split("x")
    dim_list=map(int,dim_list)
    dim_list.sort()
    l=dim_list[0]
    w=dim_list[1]
    h=dim_list[2]
    
    return 2*l*w+2*w*h+2*l*h+dim_list[0]*dim_list[1]
    
def total_paper(filename):
    
    result=0
    with open(filename) as f:
        for line in f:
            print calculate_single_paper(line)
            result+=calculate_single_paper(line)
            
    return result
    
print calculate_single_paper("23x11x5")
print total_paper("D:/varie/adventcode/day2.txt")