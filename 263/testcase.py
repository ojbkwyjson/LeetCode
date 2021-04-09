from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=6, Output=True))
        self.testcases.append(case(Input=8, Output=True))
        self.testcases.append(case(Input=14, Output=False))
        self.testcases.append(case(Input=1, Output=True))

    def get_testcases(self):
        return self.testcases
