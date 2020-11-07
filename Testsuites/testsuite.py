import os
import sys

sys.path.append(".")
from Utils.HTMLTestRunner import *
from Testcases.test_login import Login
from Testcases.test_02 import Test02

# get the directory path to output report file
dir = os.getcwd()

# get all tests from Login class
login1 = unittest.TestLoader().loadTestsFromTestCase(Login)
test02 = unittest.TestLoader().loadTestsFromTestCase(Test02)

# create a test suite
test_suite = unittest.TestSuite([login1, test02])

# open the report file
outfile = open(dir + '\\Reports\\SeleniumPythonTestSummary.html', 'w', encoding='utf-8')
print(dir + '\\SeleniumPythonTestSummary.html')

# configure HTMLTestRunner options
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)
outfile.close()
