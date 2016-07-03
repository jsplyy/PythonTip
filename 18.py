a ,b = 1,24
c, d = b,b
finish = False
for i in range(1, a*b+1):
    for j in range(1,a*b+1):
        for k in range(min(i,j),0,-1):
            if finish:
                break
            if i % k == 0 and j % k ==0:
                if k == a:
                    for m in range(max(i,j),i*j+1):
                        if m % i == 0 and m % j == 0:
                            if m == b:
                                finish = True
                                break
                            else:
                                break
                else:
                    break
        if finish:
            if c + d > i + j:
                c,d = i,j
        finish = False
print str(c) + ' ' + str(d)