#!/bin/bash

set -ex

xortool -l 8 -c 00 ./Encrypted
strings xortool_out/* | grep BreakAllCTF
