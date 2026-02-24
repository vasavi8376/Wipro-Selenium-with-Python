# module level - runs once per module (file)
# use module level set up and tear down when you want to execute the set up and tear down once in the current file
# eg open the db connection execute all the testcases and at alst close the db connection
import pytest

def setup_module(module):
    print("Open the db connection")

def teardown_module(module):
    print("closing the db connection")

#testcases 1
def test_read():
    print("Reading the db")

#testcase2
def test_write():
    print("writting the db")

#testcase3
def test_updating():
    print("updating the db")

