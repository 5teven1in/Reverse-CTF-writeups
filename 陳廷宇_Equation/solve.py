from z3 import *

v11 = BitVec('v11', 32)
v12 = BitVec('v12', 32)
v13 = BitVec('v13', 32)
v14 = BitVec('v14', 32)

data = [3488461145, 3488442025, 3480793513, 1793962409, 3488461136, 3488435113, 3480596905, 1710076329, 2364252004, 2364223942, 2356780998, 1223401414, 2364252002, 2364239558, 2356322246, 1156292550]
and_val = [0xffffff00, 0xffff00ff, 0xff00ffff, 0xffffff]

s = Solver()

for j in range(4):
    s.add(data[j] == v11 + (v12 & and_val[j]))
for k in range(4):
    s.add(data[k + 4] == v12 + (v11 & and_val[k]))
for l in range(4):
    s.add(data[l + 8] == v13 + (v14 & and_val[l]))
for m in range(4):
    s.add(data[m + 12] == v14 + (v13 & and_val[m]))

flag = b''

if s.check() == sat:
    m = s.model()
    flag += m[v11].as_long().to_bytes(4, byteorder='little')
    flag += m[v12].as_long().to_bytes(4, byteorder='little')
    flag += m[v13].as_long().to_bytes(4, byteorder='little')
    flag += m[v14].as_long().to_bytes(4, byteorder='little')
    print(f"MyFirstCTF{{{flag.decode()}}}")
