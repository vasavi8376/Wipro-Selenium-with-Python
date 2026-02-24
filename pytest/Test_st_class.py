# used inside the class
# it will run for every class definition 0nce  it will run starting and  at ending of the class

class Testclass1:


    def setup_class(cls):
        print("API Authorization needed with username and password")

    def teardown_class(cls):
        print("API Authorization closed")

    def setup_method(method):
        print("opening the browser")

    def teardown_method(method):
        print("closing the browser")

    # testcases 1
    def testcase1(self):
        print("Testcase1 is executed")

    # testcase2
    def testcase2(self):
        print("Testcase2 is executed")

    # testcase3
    def testcase3(self):
        print("Testcase3 is executed")

class Testclass2:
    # testcases 1
    def testcase1(self):
        print("Testcase1 is executed")

    # testcase2
    def testcase2(self):
        print("Testcase2 is executed")

    # testcase3
    def testcase3(self):
        print("Testcase3 is executed")



