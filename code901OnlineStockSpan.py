"""
901 Online Stock Span

Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.
 

Note:

Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
There will be at most 10000 calls to StockSpanner.next per test case.
There will be at most 150000 calls to StockSpanner.next across all test cases.
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.
"""
# my own solution by storing each price's span, and accumulate span by searching the corresponding previous price
class StockSpanner:

    def __init__(self):
        self.S = []  # store the tuple (price, span)

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        if self.S:
            i = len(self.S) - 1 # searching from the last price
            while i > -1 and self.S[i][0] <= price: # if the price self.S[i][0] <= price, this means all span prices <= price, just skip them
                span += self.S[i][1]
                i = i - self.S[i][1]    # search the next price

        self.S.append((price, span))

        return span

A = list(range(1,10000))
obj = StockSpanner()
for i, p in enumerate(A):
    assert(obj.next(p)==i+1)

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)