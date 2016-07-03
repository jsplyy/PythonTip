a ,b = 8,16
counter = 0
for i in range(1,max(a,b)+1):
    if a % i == 0 and b % i == 0:
        counter += 1
print counter