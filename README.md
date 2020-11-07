### Installation
1 Pre-condition: Download python 3.8.6 (https://www.python.org/downloads/)
2. Install libraries in requirements.txt file by command "python install -r requirements.txt"


### Execution
**Run single testcase:**
Run command (at root): python3 -m unittest Testcases\{testcase_name}.py
**Run a testsuite:**
Run command (at root): python3 Testsuite\testsuite.py

### Framework coverage
1. Run testcases on Chrome, Firefox, Opera
2. Perform running in parallel
3.Get Test Data from JSON file
4. Generate html report on specific folder Reports name file: **SeleniumPythonTestSummary.html**

### Guideline
#### Testdata: \Testdata
add/edit data for specific testcase
#### Testcases: \Testcases 
add/edit a single testcase
#### Testsuites
add/edit Testcase for running
running a test scenario here
#### Drivers: \Drivers
add/edit browserdriver
Browser supported: Firefox, Chrome, Opera, Safari
To run a specific browser, arguments syntax should be
Chrome => chrome
Firefox => firefox,ff
Safari => safari
Opera => opera
#### Objects
Account class objects
Product class object
####Utils
Read .json file 
Math calculation