package problem2779

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumBeauty(nums []int, k int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maximumBeauty(nums, k)
}