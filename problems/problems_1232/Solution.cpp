//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {

    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	vector<vector<int>> coordinates = json::parse(inputArray.at(0));
	return solution.checkStraightLine(coordinates);
}