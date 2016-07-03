#coding:utf-8
a=10000

s='圆'
neg = ''
counter = 0
zero = False
values = {0:'零',1:'壹',2:'贰',3:'叁',4:'肆',5:'伍',6:'陆',7:'柒',8:'捌',9:'玖'}
unit = {2:'拾',3:'佰',4:'仟',5:'万'}
if a < 0:
    neg = '负'
    a = abs(a)
if a == 0:
    s = values[a] + s
while a > 0:
    counter += 1
    if counter > 5:
        counter -= 4
    if a % 10 == 0:
        if not zero and s != '圆':
            s = values[0] + s
            zero = True
        a /= 10
        if counter == 5:
            s = unit[5] + s
        continue
    if counter in unit:
        s = unit[counter] + s
    s = values[a % 10] + s
    a /= 10
    zero = False
s = neg + s
print s.decode('utf8')



