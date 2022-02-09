from unittest import result


s1 = input ("Введите значение s1 ")
s2 = input ("Введите значение s2 ")

print (f'Вы ввели строку " {s1} " и " {s2} ".')

print ( len(s1), len(s2), sep = ', ' )

print ( s1[0], s2[-1], sep = ', ' )

print (s1 == s2)

print(s1 in s2, s2 in s1, sep='\n')