import hashlib

def hash_int(input):
    m=hashlib.md5()
    n=0;
    m.update(input+str(n))
    
    while not m.hexdigest().startswith("00000"):
        n+=1
        m=hashlib.md5()
        m.update(input+str(n))
    return n
    
print hash_int("iwrupvqb")

#m=hashlib.md5()
#m.update("ciao"+str(3))
#print m.hexdigest().startswith("3")