str1 = "Python is a case sensitive language"
# a
print(len(str1))

# b
print(str1[::-1])

# c
str2 = str1[10:26:1]
print(str2)

# d
a = str1[12:26:1]
b = "object oriented"
str3 = str1.replace(a,b)
print(str3)

# e
print(str1.find("a"))

# f
print(str1.replace(" ",""))