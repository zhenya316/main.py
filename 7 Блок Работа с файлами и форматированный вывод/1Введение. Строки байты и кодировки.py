# a = 'hello'     #ASCII - таблица символов содержит символы от 0-127
# print(ord('a'))
# chars = []
# for i in a:
#     chars.append(ord(i))
# print(chars)
# s = ''
# for i in chars:
#     s += chr(i)
# print(s)
a = []
for i in range(128):
    a.append(chr(i))
print(a)

b = []
for i in range(1000, 1200):
    b.append(chr(i))
print(b)

print(hex(ord('h')))        # вначале перевели символ в шестнадцатиричную систему, после в байт код
b = b'\x68'
print(type(b))              # class 'bytes'
print(b.decode())

# Существует большое количество различных кодировок, но наиболее распространённым и общепринятым стандартом является «UTF-8»
# Он имеет ограничения на количество байт, занимаемое каждым символом.