import re
s = "Alex:1994, Sunny:1996"
pattern = r"\w+:\d+"
l = re.findall(pattern, s)
print(l)
regx = re.compile(pattern)

l = regx.findall(s)
print(l)

l = re.split(r":，", s)
print(l)