from z3 import *

v = [BitVecVal(0, 32) for i in range(58)]
dest = [BitVecVal(0, 32) for i in range(30)]
flag = [BitVec(f'flag{i}', 32) for i in range(30)]

s = Solver()

for i in range(30):
    s.add(flag[i] >= 0)
    s.add(flag[i] <= 255)
    dest[i] = flag[i]
    v[2 + i] = dest[i]

v[2] = dest[3] ^ (dest[21] | dest[11] | dest[1] ^ (dest[4] + (dest[10] ^ v[2]))) ^ dest[6];
v[21] = dest[19] ^ dest[0] ^ (dest[20] | (dest[8] + dest[5] + (dest[9] ^ v[21]))) ^ dest[14];
v[18] = dest[3] ^ (dest[22] | (dest[20] + (dest[2] | v[18]))) | dest[1];
v[9] = v[9] + dest[9] + dest[2];
v[24] = (dest[22] | (dest[4] + (dest[17] | dest[0] | dest[12] | v[24]))) + dest[7];
v[21] = (dest[3] | dest[2] | (dest[11] + (dest[19] ^ v[21]))) ^ dest[12];
v[24] = v[24] + dest[13] + dest[1];
v[16] = dest[5] | (dest[20] + (dest[2] ^ dest[9] ^ (dest[1] + dest[3] + v[16]))) | dest[16];
v[10] = (dest[20] | (dest[0] + (dest[13] ^ (dest[3] + v[10])))) + dest[10];
v[5] = (dest[3] | v[5]) ^ dest[6];
v[24] = (dest[19] | v[24]) + dest[2];
v[8] = (dest[16] | dest[0] ^ (dest[12] | dest[8] | (dest[22] + (dest[18] | v[8])))) ^ dest[21];
v[15] = dest[10] | dest[13] ^ (dest[21] + dest[1] + v[15]) | dest[2];
v[16] = (dest[16] + (dest[5] ^ (dest[2] + (dest[6] ^ v[16])))) ^ dest[10];
v[22] = (dest[13] + (dest[10] | dest[22] ^ (dest[12] + (dest[17] ^ dest[2] ^ dest[15] ^ dest[6] ^ v[22])))) | dest[9];
v[8] = v[8] | dest[1] | dest[8];
v[4] = (dest[15] + dest[21] + dest[22] + (dest[11] | dest[9] | (dest[3] + (dest[7] ^ v[4])))) | dest[10];
v[23] = dest[11] ^ dest[18] ^ (dest[3] + (dest[12] ^ dest[9] ^ (dest[13] | dest[4] | v[23]))) ^ dest[7];
v[6] = (dest[19] ^ dest[21] ^ (dest[0] + dest[12] + (dest[7] | dest[22] ^ v[6]))) + dest[16];
v[21] = dest[7] | (dest[4] + dest[21] + (dest[3] | (dest[22] + v[21]))) | dest[13];
v[19] = (dest[2] + (dest[18] | dest[4] ^ (dest[16] + (dest[14] | v[19])))) ^ dest[21];
v[2] = (dest[22] | dest[0] | dest[18] ^ (dest[10] | v[2])) ^ dest[15];
v[9] = (dest[6] | (dest[2] + (dest[8] | dest[18] ^ v[9]))) ^ dest[19];
v[17] = (dest[9] ^ (dest[5] + dest[8] + dest[0] + (dest[10] ^ (dest[20] + (dest[11] ^ v[17]))))) + dest[17];
v[13] = dest[17] ^ (dest[20] + dest[0] + (dest[13] | v[13])) ^ dest[16];
v[14] = v[14] ^ dest[3] ^ dest[9] ^ dest[19] ^ dest[5];
v[4] = (dest[0] + (dest[2] | v[4])) ^ dest[17];
v[16] = (dest[4] | (dest[22] + (dest[2] | dest[20] | dest[15] | dest[3] ^ v[16]))) ^ dest[18];
v[19] = (dest[1] + (dest[13] | dest[9] | (dest[6] + (dest[19] | dest[5] | v[19])))) ^ dest[11];
v[24] = (dest[0] ^ (dest[11] | v[24])) + dest[17];
v[21] = v[21] | dest[16] | dest[2];
v[4] = (dest[1] ^ (dest[3] + (dest[21] ^ (dest[22] + v[4])))) + dest[8];
v[6] = dest[20] ^ (dest[9] | dest[11] | dest[17] | dest[10] | (dest[6] + v[6])) | dest[0];
v[23] = dest[19] ^ (dest[8] | (dest[20] + (dest[15] ^ dest[9] ^ (dest[5] + dest[1] + v[23])))) ^ dest[21];
v[12] = (dest[1] | (dest[7] + dest[6] + dest[12] + (dest[14] | dest[21] | v[12]))) + dest[0];
v[23] = (dest[21] ^ (dest[2] + (dest[17] | dest[11] | dest[5] | dest[18] ^ v[23]))) + dest[1];
v[12] = dest[8] ^ dest[0] ^ dest[15] ^ (dest[18] | v[12]) | dest[19];
v[12] = dest[1] | (dest[11] + (dest[20] | (dest[16] + (dest[2] ^ dest[3] ^ (dest[15] + v[12]))))) | dest[8];
v[4] = dest[9] + (dest[10] ^ (dest[7] | v[4])) + dest[3];
v[24] = (dest[7] ^ (dest[1] + (dest[16] ^ v[24]))) + dest[10];
v[4] = (dest[2] | (dest[7] + (dest[12] ^ (dest[10] | v[4])))) ^ dest[0];
v[18] = (dest[18] | (dest[0] + (dest[3] ^ (dest[8] | (dest[1] + (dest[6] ^ v[18])))))) + dest[16];
v[6] = dest[2] | dest[18] | (dest[4] + (dest[9] ^ v[6])) | dest[20];
v[18] = (dest[18] + dest[5] + (dest[16] | dest[3] ^ dest[14] ^ v[18])) | dest[20];
v[15] = (dest[18] ^ dest[16] ^ (dest[22] | dest[15] ^ dest[12] ^ v[15])) + dest[1];
v[12] = (dest[13] | (dest[20] + dest[9] + (dest[0] | v[12]))) ^ dest[14];
v[21] = dest[7] + (dest[10] ^ (dest[8] | dest[20] | dest[6] ^ (dest[1] + v[21]))) + dest[14];
v[4] = (dest[7] + v[4]) | dest[0];
v[4] = dest[10] ^ (dest[2] + (dest[14] | v[4])) | dest[19];
v[14] = (dest[0] | (dest[19] + (dest[18] ^ dest[7] ^ (dest[13] | dest[5] ^ v[14])))) ^ dest[6];
v[3] = (dest[4] ^ (dest[0] + v[3])) + dest[8];
v[7] = dest[13] ^ (dest[3] | dest[6] ^ (dest[2] | v[7])) | dest[14];
v[11] = (dest[11] + (dest[3] ^ dest[17] ^ (dest[6] | v[11]))) | dest[21];
v[20] = (dest[2] | dest[22] | v[20]) + dest[5];
v[47] = dest[16] + dest[15] + dest[13] + dest[12] + dest[11] + dest[10] + dest[17];
v[46] = dest[21] + dest[20] + dest[19] + dest[18] + dest[17] + dest[16] + dest[22];
v[45] = dest[11] + dest[10] + dest[9] + dest[8] + dest[7] + dest[6] + dest[12];
v[44] = 6 * dest[21] + 5 * dest[22] + 31 * dest[20];
v[43] = 36 * dest[19] + 19 * dest[22] + 7 * dest[17];
v[42] = 37 * dest[18] + 21 * dest[16] + 2 * dest[14];

for i in range(20):
    v[51] += v[2 + i]
s.add(v[51] == 8828)

s.add(v[47] == 413)
s.add(v[46] == 585)
s.add(v[45] == 443)
s.add(v[44] == 2792)
s.add(v[43] == 6714)
s.add(v[42] == 4937)

v[56] = 0;
v[55] = 0;
v[54] = 0;
v[53] = 0;
v[52] = 0;
while True:
    v[41] = dest[v[56]];
    s.add( v[41] <= 0x7E )
    v[56] += 1;
    v[52] += v[41];
    v[54] = v[41] ^ (10 * v[54]);
    v[55] = 24 * v[55] + v[41];
    v[53] = ((v[53] >> 20) + 7 * v[41]) | (v[53] << 12);
    if v[56] == 16:
        break

v[56] = 0;
s.add(v[52] == 1280)
s.add(v[53] == -1924661067)
s.add(v[54] == -1485183740)
s.add(v[55] == -1412452934)

dest[0] ^= 0x11;
dest[1] ^= 0xAA;
v[40] = (0xff & (dest[1] ^ dest[0]));
dest[2] ^= 0x55;
dest[3] ^= 0x33;
v[39] = v[40] ^ dest[2];
v[38] = v[40] ^ (0xff & (dest[3] ^ dest[2]));
v[37] = v[40] ^ (0xff & (dest[3] ^ dest[4] ^ dest[2]));
v[36] = v[40] ^ (0xff & (dest[3] ^ dest[4] ^ dest[5] ^ dest[2]));
v[35] = v[40] ^ (0xff & (dest[3] ^ dest[4] ^ dest[5] ^ dest[6] ^ dest[2]));
v[34] = dest[3] ^ dest[4] ^ dest[5] ^ dest[6] ^ dest[7] ^ dest[8] ^ dest[2] ^ v[40];
v[33] = v[40] ^ (0xff & (dest[3] ^ dest[4] ^ dest[5] ^ dest[6] ^ dest[7] ^ dest[2]));
dest[8] = v[34];
v[32] = (0xff & (v[34] ^ dest[9]));
v[31] = v[32] ^ dest[10];
v[30] = v[32] ^ (0xff & (dest[11] ^ dest[10]));
v[29] = (0xff & (dest[19] ^ dest[20] ^ dest[21] ^ dest[22] ^ dest[15]));
v[28] = (0xff & (dest[16] ^ dest[17] ^ dest[18] ^ dest[14]));
v[27] = v[32] ^ (0xff & (dest[11] ^ dest[12] ^ dest[10]));
v[26] = v[32] ^ (0xff & (dest[11] ^ dest[12] ^ dest[13] ^ dest[14] ^ dest[10]));
v[25] = v[32] ^ (0xff & (dest[11] ^ dest[12] ^ dest[13] ^ dest[10]));
dest[15] ^= v[26];
dest[0] ^= 0x63;
dest[8] ^= 0x30;
dest[1] = ((2 * v[40]) | (v[40] >> 1)) ^ 0x2F;
dest[2] = ((4 * v[39]) | (v[39] >> 2)) ^ 0xDC;
dest[3] = ((8 * v[38]) | (v[38] >> 3)) ^ 0x20;
dest[4] = ((16 * v[37]) | (v[37] >> 4)) ^ 0xCD;
dest[5] = ((32 * v[36]) | (v[36] >> 5)) ^ 0xA0;
dest[6] = (((0xff & (v[35])) << 6) | (v[35] >> 6)) ^ 0x83;
dest[7] = ((0xff & (v[33])) << 7) | (v[33] >> 7);
dest[9] = ((2 * v[32]) | (v[32] >> 1)) ^ 0x7D;
dest[10] = ((4 * v[31]) | (v[31] >> 2)) ^ 0x19;
dest[11] = ((8 * v[30]) | (v[30] >> 3)) ^ 4;
dest[12] = ((16 * v[27]) | (v[27] >> 4)) ^ 0xC4;
dest[13] = ((32 * v[25]) | (v[25] >> 5)) ^ 0x20;
v[56] = dest[15];
dest[14] = (((0xff & (v[26])) << 6) | (v[26] >> 6)) ^ 0xC1;
dest[15] = ((0xff & (v[56])) << 7) | (v[56] >> 7);
# v[56] = v[29] + (((0xff & (dest[0] | dest[2] | dest[3])) | (0xff & dest[1])) == 0xFF) + v[28] - 77;
v[56] = v[29] + v[28] - 77;

s.add(v[56] == 1)

if s.check() == sat:
    m = s.model()
    for i in range(30):
        print(chr(m[flag[i]].as_long()), end = '')
