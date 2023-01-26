str1='Python is the best programming language in the world'
print(str1[5:-7])
str2 = "Guido van Rossum is the benevolent dictator for life"
print(str2[2::3])
str3 = "You have a problem with authority, Mr. Anderson."
str3list = list(str3)
str3set = set(str3list)
str3count = list(map(str3list.count, str3set))
dict = dict(zip(str3set , str3count))
print(str3)
print(dict)