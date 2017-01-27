def apply_op(op,arg1,arg2,dest,map):
    if op=="AND":
        assign_value(dest,arg1 & arg2, map)
    elif op=="OR":
        assign_value(dest, arg1 | arg2, map)
    elif op=="RSHIFT":
        assign_value(dest, arg1 >> arg2, map)
    elif op=="LSHIFT":
        assign_value(dest,arg1 << arg2, map)
        
def parse_command(string,map):
    list=string.rstrip('\n').split(' ')
    
    if len(list)==3:
        
        if list[0] not in map.keys() and not list[0].isdigit():
            return False
        else:
            arg=check_arg(list[0],map)  
            dest=list[2]
            check_arg(list[2],map)
            assign_value(list[2],arg,map)
            print arg,'->',list[2]
        
    elif len(list)==4:
        
        if list[1] not in map.keys() and not list[1].isdigit():
            return False
        else:
            arg=check_arg(list[1],map)
            dest=list[3]
            check_arg(list[3],map)
            assign_value(list[3],~arg & 0xffff
            ,map)    
            print list[0],arg,'->',list[3]
        
    else:
        
        if (list[0] not in map.keys() and not list[0].isdigit()) or (list[2] not in map.keys() and not list[2].isdigit()):
            return False
        else:
            arg1=check_arg(list[0],map)
            arg2=check_arg(list[2],map)
            check_arg(list[4],map)
            dest=list[4]
            op=list[1]
            apply_op(op,arg1,arg2,dest,map) 
            print arg1,op,arg2,'->',dest
    return True
                
    

def assign_value(dest,val,map):
    map[dest]=val

def check_arg(arg,map):    
    if arg.isdigit():
        return int(arg)
    elif arg not in map.keys():
        map[arg]=0
    return map[arg]


def process_file(filename,map):
    lines=[]
    done=False
    
    with open(filename) as f:
        lines=f.readlines()
        
    while 1:
        for line in lines:
            done=parse_command(line,map)
            print done
            if done:
                lines.remove(line)
        if len(lines)==0: break

    print sorted(lines)
    print len(lines)

            
            
            
registers={}
process_file("D:/varie/adventcode/input7.txt",registers)
for i in sorted(registers.keys()):
    print i,registers[i]
