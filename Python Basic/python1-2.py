#1후반부
'''
def plus(a,b):
    if type(b) is int or type(b) is float:
        return a+b
    else:
        return None

print(plus(5,3.4))
'''
'''
#if,else
def age_check(age):
    print(f"you are {age}")
    if age<18:
        print("you can't drink")
    elif age==18:
        print("you are new to this")
    elif age>20 and age<25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")

age_check(23)
'''
'''#for
days = ("Mon","Tue","Wed","Thur","Fri")

for day in days:
    if day == "Wed":
        break
    else:
        print(day)

for letter in "Kimjae":
    print(letter)
'''
#module
'''
import math #math 모듈 전체를 가져옴 -비추

print(math.ceil(1.2))
'''
from math import ceil, fsum  #math 모듈중 원하는 함수만 가져옴
from math import floor as ff  #함수 이름 원하는대로 바꿔주기

print(ceil(2.6))
print(fsum([1,2,3,4,5,5.9]))
print(ff(4.3))
