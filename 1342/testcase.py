from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=14, Output=6))
        self.testcases.append(case(Input=8, Output=4))
        self.testcases.append(case(Input=123, Output=12))

    def get_testcases(self):
        return self.testcases
