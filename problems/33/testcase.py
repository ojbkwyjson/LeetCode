from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 5, 6, 7, 0, 1, 2], 0], Output=4))
		self.testcases.append(case(Input=[[4, 5, 6, 7, 0, 1, 2], 3], Output=-1))
		self.testcases.append(case(Input=[[1], 0], Output=-1))

	def get_testcases(self):
		return self.testcases
