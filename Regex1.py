import re

name = "rohithgk2@gmail.com"

result = re.match("\w+[@]\w+[.]\w+",name)

if result:
    print("Yes")
else:
    print("No")
print(result)

txt = "I am Rohith G Krishna"

print(re.findall("[a-z]",txt))

txt = "I am about to be 28 years"

print(re.findall("\d+",txt))

msg = "hello world"

print(re.findall("h....",msg))

if re.match("^hello",msg):
    print("Yaya")
else:
    print("Nono")

x = re.findall("world$", msg)
if x:
  print("Yes, the string ends with 'world'")
else:
  print("No match")
