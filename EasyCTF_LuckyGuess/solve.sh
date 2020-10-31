#!/bin/bash

set -ex

gcc -fPIC -shared -o hook.so ./hook.c -ldl
echo 0 | LD_PRELOAD=./hook.so ./LuckyGuess
