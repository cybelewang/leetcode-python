"""
904 Fruit Into Baskets

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
 
Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
"""
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        fruits, left = set(), 0   # fruits is a set containing unique fruits, left is the left boundary of the two-fruit segment
        last, cnt = -1, 0   # last fruit type and its continuous count
        ans = 0 # final answer
        for i, t in enumerate(tree):
            if len(fruits) < 2 or t in fruits:
                cnt = 1 + cnt if t == last else 1
            else:   # a third type fruit is seen
                left = i - cnt    # use the last fruit's continuous count to update left boundary index
                fruits.clear()
                fruits.add(last)
                cnt = 1
            fruits.add(t)   # add this fruit to set
            last = t    # update last fruit
            ans = max(ans, i - left + 1)    # update final answer

        return ans

tree = [1,2,2,2,3,2,2] # expected 6
#tree =[3,3,3,1,2,1,1,2,3,3,4]
obj = Solution()
print(obj.totalFruit(tree))