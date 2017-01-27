class Santa:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.coord=[str(x),str(y)]
        
    def move(self,dir):
        
        if dir == '^':
            self.y+=1
            self.coord=[str(self.x),str(self.y)]
        elif dir == 'v':
            self.y-=1
            self.coord=[str(self.x),str(self.y)]
        elif dir == '<':
            self.x-=1
            self.coord=[str(self.x),str(self.y)]
        elif dir == '>':
            self.x+=1
            self.coord=[str(self.x),str(self.y)]
            
    

    

def count_houses_with_presents(path):
    x=y=0
    visited=[['0','0']]
    received=1
    current_pos=Santa(0,0)
    
    for dir in path:
        current_pos.move(dir)
        if not current_pos.coord in visited:
            visited.append(current_pos.coord)
            received+=1
            
    return received

def count_from_file(filename):
    with open(filename,"r") as f:
        return count_houses_with_presents(f.read())

#print count_houses_with_presents("^v^v^v^v^v")
print count_from_file("D:/varie/adventcode/input3.txt")
        
    