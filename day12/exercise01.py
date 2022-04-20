import re

a = "张三三李四王五张三"
print(re.findall("[^张].", a))

print(re.findall("^五", a))
print(re.findall("王五$", a))
print(re.findall("张三*李", a))

b = "How are you"
print(re.findall("[A-Z][a-z]*", b))

print(re.findall("\d", "36545512345365550"))

print(re.findall("\\$\\d+", "$100"))
print("\r")
print(1)
print("\n")
print(1)

s = "[ 峨天皇]，[dsfkjoag]"
print(re.findall(r"\[.\w+\]", s))


print(re.findall(r"ab+", "abababab"))

