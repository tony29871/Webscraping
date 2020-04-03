''' 
#list[]
days= ["mon","tue","wed","thur","fri"]
print(days[2])
days.append("sat")
days.reverse()
print(days)
'''
"""
#tuple
days = ("Mon","Tue", "Wed", "Thur","Fri")

#dic
kimjae = {
    "name":"JaeHyun",
    "age":25,
    "korean": True,
    "fav_food":["Gookbab","Pizza"]
}

print(kimjae)
kimjae["handsome"] = True
print(kimjae)
"""
'''
# 제공된 함수
age="18"
print(type(age))
n_age = int(age)
print(type(n_age))
'''
'''
#함수 만들기
def say_hello(who):
    print("hello",who)
    print("bye")

say_hello("Nico")

def plus(a,b=4):
    print(a+b)

plus(2,5)
plus(2)

#리턴함수
def r_plus(a,b):
    return a+b
    #여기 뒤에는 무의미

print(r_plus(1,4))
'''

#keyworded arguments
def say_hello(name,age):
    return f"Hello {name} you are {age} years old"
    #return "Hello " + name + " you are " + age + " years old"

hello = say_hello("Kimjae",25)
#hello = say_hello(age="25", name= "KimJae")
print(hello)