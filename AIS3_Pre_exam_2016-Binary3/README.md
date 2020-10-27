Run `time python solve.py` to solve the challenge by angr and calculate the execution time.

```
WARNING | 2020-10-27 17:09:41,034 | angr.simos.simos | stdin is constrained to 30 bytes (has_end=True). If you are only providing the first 30 bytes instead of the entire stdin, please use stdin=SimFileStream(name='stdin', content=your_first_n_bytes, has_end=False).
WARNING | 2020-10-27 17:09:41,586 | angr.storage.memory_mixins.default_filler_mixin | The program is accessing memory or registers with an unspecified value. This could indicate unwanted behavior.
WARNING | 2020-10-27 17:09:41,586 | angr.storage.memory_mixins.default_filler_mixin | angr will cope with this by generating an unconstrained symbolic variable and continuing. You can resolve this by:
WARNING | 2020-10-27 17:09:41,586 | angr.storage.memory_mixins.default_filler_mixin | 1) setting a value to the initial state
WARNING | 2020-10-27 17:09:41,586 | angr.storage.memory_mixins.default_filler_mixin | 2) adding the state option ZERO_FILL_UNCONSTRAINED_{MEMORY,REGISTERS}, to make unknown regions hold null
WARNING | 2020-10-27 17:09:41,586 | angr.storage.memory_mixins.default_filler_mixin | 3) adding the state option SYMBOL_FILL_UNCONSTRAINED_{MEMORY,REGISTERS}, to suppress these messages.
WARNING | 2020-10-27 17:09:41,586 | angr.storage.memory_mixins.default_filler_mixin | Filling memory at 0x7fffffffffeff0e with 18 unconstrained bytes referenced from 0x700010 (strlen+0x0 in extern-address space (0x10))
WARNING | 2020-10-27 17:09:41,586 | angr.storage.memory_mixins.default_filler_mixin | Filling memory at 0x7fffffffffeff30 with 8 unconstrained bytes referenced from 0x700010 (strlen+0x0 in extern-address space (0x10))
WARNING | 2020-10-27 17:09:42,329 | angr.storage.memory_mixins.default_filler_mixin | Filling memory at 0xc0000f51 with 1 unconstrained bytes referenced from 0x700000 (strcpy+0x0 in extern-address space (0x0))
b'ais3{a XOR b XOR 1oo1l} @ @@ @'
python solve.py  582.64s user 285.25s system 196% cpu 7:21.09 total
```

Flag is `ais3{a XOR b XOR 1oo1l}`.
