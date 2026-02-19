for b in range(1,11):
    for k in range(1,21):
        for t in range(1,201):
            if 10*b+5*k+1/2*t==100:
                if b+k+t==100:
                    print(b,k,t)