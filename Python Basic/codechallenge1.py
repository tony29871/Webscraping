#Code challenge1

def cal(a,b,op=''):
    if op =='+':
        return int(a)+int(b)
    elif op=='-':
        return int(a)-int(b)
    elif op=='*':
        return int(a)*int(b)
    elif op=='/':
        return int(a)/int(b)
    elif op=='%':
        return int(a)%int(b)
    elif op=='**':
        return int(a)**int(b)

a,b=7,3

print(cal(a,b,'**'))