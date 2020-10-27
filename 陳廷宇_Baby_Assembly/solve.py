data = [1634038338, 1819033963, 2068206659, 1597322073, 862805809, 929001057, 1601384808, 2100522544]
flag = b''

for i in data:
    flag += i.to_bytes(4, byteorder = 'big')[::-1]

print(flag)
