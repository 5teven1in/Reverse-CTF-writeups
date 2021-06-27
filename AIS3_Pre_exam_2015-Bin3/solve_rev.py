key = 0xDDDDAAAADADADDAA
inp = 0xBCB4DEC4BFB7B8CE

print((key ^ inp).to_bytes(8, 'little'))
