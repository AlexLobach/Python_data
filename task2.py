a = input ("Введите значение a: ")
a = float(a)
b = input ("Введите значение b: ")
b = float(b)
c = input ("Введите значение c: ")
c = float(c)

s1 = (a**2 + b**2)/(3*b-4)
#print (s1)
s2 = (4*c**5)/6
#print (s2)
print(s1//s2, int(s1 % s2), sep="\n")