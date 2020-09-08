"""
1429 First Unique Number

You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]
Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
Example 2:

Input: 
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output: 
[null,-1,null,null,null,null,null,17]
Explanation: 
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17
Example 3:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output: 
[null,809,null,-1]
Explanation: 
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1
 
Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.
"""
# my own union find solution
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.data = [] # holds the input unique value in first-add order
        self.root = {} # self.data index of the value where to look for unique integer, if key is the first unique integer, then the value is the key's index in self.data
        for num in nums: self.add(num) # bug fixed: forget to call self.add(num)
            
    def showFirstUnique(self) -> int:
        # union find the first unique integer
        i = 0
        while i < len(self.data):
            val = self.data[i]
            if self.root[val] == i:
                break
            else:
                i = self.root[val]
        # save this result for fast search in next call
        if self.data:
            self.root[self.data[0]] = i
        
        if i < len(self.data):
            return self.data[i]
        else:
            return -1

    def add(self, value: int) -> None:
        if value in self.root:
            i = self.root[value]
            # check if root of value is its index in self.data
            # bug fixed: forget to check index range of i
            if i < len(self.data) and self.data[i] == value:
                self.root[value] = i + 1 # point to next data
        else:
            self.root[value] = len(self.data)
            self.data.append(value)
            
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)