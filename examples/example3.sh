#!/bin/sh
cd suiter
python ./suiter.py ../input/input_file3.json
cd result
pytest python_script.py