import pytest
import sys
@pytest.mark.xfail(reason="Known bug in the third-pary library")
def test_function_with_bug():
    assert (1 + 1) == 3

@pytest.mark.sanity
def testcase1():
    print("Testcase1 is executed")

#testcase2
@pytest.mark.regression
def testcase2():
    print("Testcase2 is executed")

#testcase3
@pytest.mark.db
def testcase3():
    print("Testcase3 is executed")


# xfail with a condition
@pytest.mark.xfail(sys.platform == "win32", reason="Bug on windows")
def test():
    print("test on windows")

# this xfail will fail only on windows

# strict=True XFAIL FAILED Fails the test suite
@pytest.mark.xfail(strict=True, reason="Bug #1234 is not fixed yet")
def test_function():
    assert True

# the testcase should fail mandatorily