from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(12,3), Output=3))
        self.testcases.append(case(Input=(7,2), Output=7))
        self.testcases.append(case(Input=(4,4), Output=-1))
        self.testcases.append(case(Input=(1,1), Output=1))
        self.testcases.append(case(Input=(1000,3), Output=4))

    def get_testcases(self):
        return self.testcases
