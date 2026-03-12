for x in range(1, 8):
    for y in range(1, 18):
        for z in range(2, 98, 2):
            if (x*10 + y*5 + z/2 == 100) and (x + y + z == 100):
                print(x, y, z)