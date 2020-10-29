#!/bin/bash

objdump -M intel -d ./search | \
    grep '#.*<s.*>' | \
    awk -F 'x' '{print $3}' | \
    cut -d ' ' -f1 | \
    xargs | \
    tr -d '[:space:]' | \
    python3 -c 'print(bytes.fromhex(input()).decode())' | \
    sed -n 's/.*\(MyFirstCTF{\w*}\).*/\1/p'
