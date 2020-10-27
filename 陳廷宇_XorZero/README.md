Use `file Encrypted` command and we can see the output is encrypted data.

Check out the challenge name and binary hexdump.

```
➜ xxd Encrypted | head
00000000: 3d37 2927 6940 6d6c 4272 6561 6b41 6c6c  =7)'i@mlBreakAll
00000010: 4072 5b61 6a41 6c6c 7276 2561 6b41 6c6c  @r[ajAllrv%akAll
00000020: 0272 6561 6b41 6c6c 2a63 6561 6b41 6c6c  .reakAll*ceakAll
00000030: 4272 6561 2b41 546c 4b72 2561 7641 706c  Brea+ATlKr%avApl
00000040: 4472 6561 6e41 6c6c 0272 6561 6b41 6c6c  DreanAll.reakAll
00000050: 0272 2561 6b41 6c6c 0272 2561 6b41 6c6c  .r%akAll.r%akAll
00000060: ba73 6561 6b41 6c6c ba73 6561 6b41 6c6c  .seakAll.seakAll
00000070: 4a72 6561 6b41 6c6c 4172 6561 6f41 6c6c  JreakAllAreaoAll
00000080: 7a70 6561 6b41 6c6c 7a70 2561 6b41 6c6c  zpeakAllzp%akAll
00000090: 7a70 2561 6b41 6c6c 5e72 6561 6b41 6c6c  zp%akAll^reakAll
```

We could guess the file is XOR encrypted and use `xortool` to solve it.

```
➜ xortool Encrypted
The most probable key lengths:
   1:   7.9%
   4:   13.8%
   8:   20.7%
  12:   9.4%
  16:   14.1%
  20:   6.5%
  24:   9.9%
  28:   4.7%
  32:   7.3%
  40:   5.7%
Key-length can be 4*n
Most possible char is needed to guess the key!

➜ xortool -l 8 -c 00 Encrypted
1 possible key(s) of length 8:
BreakAll
Found 0 plaintexts with 95.0%+ valid characters
See files filename-key.csv, filename-char_used-perc_valid.csv
```

Just use `strings` to extract the printable strings in output file.

```
➜ strings xortool_out/0.out | grep 'BreakAll'
BreakAllCTF{X0r_1s_s0m37h1ng_funny}
```

Flag is `BreakAllCTF{X0r_1s_s0m37h1ng_funny}`.
