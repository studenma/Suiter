#!/bin/sh
cd suiter
python ./suiter.py ../input/input_file2.json
cd result
pytest python_script.py