import pytest
#setup at function level
def setup_function(function):
    print("opening the browser")


def teardown_function(function):
    print("closing the browser")


#testcases 1
@pytest.mark.sanity
def testcase1():
    print("Testcase1 is executed")

#testcase2
@pytest.mark.regression
def testcase2():
    print("Testcase2 is executed")

#testcase3

def testcase3():
    print("Testcase3 is executed")
