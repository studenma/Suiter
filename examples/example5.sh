#!/bin/sh
cd suiter
python ./suiter.py ../input/input_file2.json --framework JavaScript
cd result
mocha javascript_script.js