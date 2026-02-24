# grouping - set of testcases run together - issue fix in that module

import pytest

# testcases 1
def testcase1():
    print("Testcase1 is executed ")

# testcases 2
@pytest.mark.sanity
def testcase2():
    print("Testcase2 is executed ")

# testcases 3
@pytest.mark.regression
@pytest.mark.sanity
def test_case3():
    print("Testcase3 is executed ")
