from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(1, 2, 0, 0), Output=[[0, 0], [0, 1]]))
        self.testcases.append(case(Input=(2, 2, 0, 1), Output=[[0, 1], [0, 0], [1, 1], [1, 0]]))
        self.testcases.append(case(Input=(2, 3, 1, 2), Output=[[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]))

    def get_testcases(self):
        return self.testcases
