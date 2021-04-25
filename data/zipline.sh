#!/bin/sh

pip install -U -q PyDrive
curl -sO https://raw.githubusercontent.com/algo-stocks/data/master/data/zipline.py
python zipline.py && sh zipline.sh
