def kr(x):
        n = [0,0,0,0]
        o = []
        n[0] = int(x[0])
        n[1] = int(x[1])
        n[2] = int(x[2])
        n[3] = int(x[3])

        tempMax = 0
        for k in x:
                for i in n:
                        for j in n:
                                if i > tempMax:
                                        tempMax = i
                o.append(tempMax)
                n.remove(tempMax)
                tempMax = 0

        g = int(''.join(map(str, o)))
        o.reverse()
        l = int(''.join(map(str, o)))

        out = g-l
        out = str(out)
        if len(out) < 4:
                out = '0' + out
        
        return out