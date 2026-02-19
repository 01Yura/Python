# буз оптимизации, работает очень долго
from math import pow

for a in range(1,151):
    for b in range(1,151):
        for c in range(1,151):
            for d in range(1,151):
                for e in range(1,151):
                    print(a,b,c,d,e)
                    if pow(a,5)+pow(b,5)+pow(c,5)+pow(d,5)==pow(e,5):
                        print(a+b+c+d+e)