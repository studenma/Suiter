Git Setup:
To create a new key:
$ ssh-keygen 


$ eval `ssh-agent`
$ ssh-add studenma


Combine Flask setup:
1. Go to folder combine-master/combine/web_interface
2. $ python3 -m venv venv
3. $ source venv/bin/activate
4. Change the port in 'combine-master/combine/web_interface/flask_app.py' to run two separated Flask apps
5. Run the Flask app:
$ python3 flask_app.py 


Suiter Flask setup:
$ source /venv/bin/activate
$ deactivate



Python modules location:
/usr/lib/python3.8




Run a command 10 times:
for run in {1..10}; do python3 suiter.py; done

Create a 999 files in a dir
$ for run in {001..999}; do touch "test_suite-"$run".py"; done

CORS error
https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

TODO: logging in Python, Flask, javacript



ALIASES
alias lsout='ls -la ../test_suite_output/'



EXTENSIONS:
TODO Highlight - potreba pro zvyrazneni TODO v test suite


"""
TODO: Add assert text
TODO: Make a GUI app to simply edit a resulted test suite
TODO: Make script to setup ssh
TODO: code celanup
"""



DOXYGEN configuration:
PROJECT_NAME      = "Python"
OUTPUT_DIRECTORY  = pyexample
GENERATE_LATEX    = NO
GENERATE_MAN      = NO
GENERATE_RTF      = NO
OPTIMIZE_OUTPUT_JAVA = YES
INPUT             = pyexample.py
QUIET             = YES
JAVADOC_AUTOBRIEF = YES
SEARCHENGINE      = NO


https://docs.python-guide.org/writing/structure/#structure-of-the-repository