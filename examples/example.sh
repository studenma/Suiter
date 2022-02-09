#!/bin/sh
cd suiter
python ./suiter.py ../input/input_file.json
cd result
pytest python_script.py