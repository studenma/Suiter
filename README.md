# Suiter
Tool Supporting Generation of Automatic Test Set

## Installation
Prepare python environment
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python suiter/web_interface/flask_app.py
```
Run suiter python script:
```
$ python suiter/suiter.py
```
## Sample use cases
Start local web service:
```
$ source venv/bin/activate
$ python suiter/web_interface/flask_app.py
```
Run examples in new terminal:
```
$ source venv/bin/activate
$ ./examples/example.sh
$ ./examples/example2.sh
$ ./examples/example3.sh
$ ./examples/example4.sh
$ ./examples/example5.sh
```
### example.sh
* Single HTTP request, 4 parameters combined, globals parameters included, T-way:3
* Combiantions are made only on the request level
* Expected number of test cases: 72
    * All of them should pass

### example2.sh
* Two HTTP requests
* Combinations are made on the first two levels
* Expected number of test cases: 72 (24*3)
    * All of them should pass

### example3.sh
* Same as the example2.sh, but with dividing by zero
* Expected number of test cases: 72 (24*3)
    * 3 of them should have fail

### example4.sh
* More complicated combinations
    * parameters are also in the file content
* The max TC limit is reached - user is going to be prompt
* Expected number of test cases: 198
* All tests should have fail - the input JSON data are totally random
    * You can check the resulted script in: ./suiter/result/python_script.py

### example5.sh
* Same as the example2.sh, but with a JavaScript template


## Testing
Run following
```
$ pytest
```