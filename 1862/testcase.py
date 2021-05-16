from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 5, 9], Output=10))
        self.testcases.append(case(Input=[7, 7, 7, 7, 7, 7, 7], Output=49))

    def get_testcases(self):
        return self.testcases
