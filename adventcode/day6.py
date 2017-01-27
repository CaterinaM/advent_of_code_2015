def get_init_x(list):
    coord=str(list[len(list)-3]).split(',')
    return int(coord[0])
    
def get_init_y(list):
    coord=str(list[len(list)-3]).split(',')
    return int(coord[1])
    
def get_final_x(list):
    coord=str(list[len(list)-1]).split(',')
    return int(coord[0])
    
def get_final_y(list):
    coord=str(list[len(list)-1]).split(',')
    return int(coord[1])
    
def parse_command(string):
    list=string.split(' ')
    return list
    
def switch_light(string,m):
    command=parse_command(string)
    
    x1=get_init_x(command)
    y1=get_init_y(command)
    x2=get_final_x(command)
    y2=get_final_y(command)

    
    if string.startswith("turn on"):
        for i in range(y1,y2+1):
            for j in range(x1,x2+1):
                m[i][j]=1
    elif string.startswith("turn off"):
        for i in range(y1,y2+1):
            for j in range(x1,x2+1):
                m[i][j]=0
    elif string.startswith("toggle"):
        for i in range(y1,y2+1):
            for j in range(x1,x2+1):
                if m[i][j]==0:
                    m[i][j]=1
                else:
                    m[i][j]=0

def count_ones(m):
    count=0
    for i in range(1000):
        for j in range(1000):
            count+=m[i][j]
    return count
    
def lights_battle(filename,m):
    with open(filename) as f:
        for line in f:
            switch_light(line,m)
    return count_ones(m)
    
m=[[0 for x in range(1000)] for x in range(1000)]
print lights_battle("D:/varie/adventcode/input6.txt",m)

#print switch_light("toggle 0,0 through 999,0",m)
#print m[0]