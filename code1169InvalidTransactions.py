"""
1169 Invalid Transactions

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]

Constraints:
transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        t = [trans.split(',') for trans in transactions]
        t.sort(key = lambda x: [x[0], int(x[1])])
        invalid = set()
        for i in range(len(t)):
            j = i + 1
            duplicate = False
            while j < len(t) and t[j][0] == t[i][0] and int(t[j][1]) - int(t[i][1]) <= 60:
                if t[j][3] != t[i][3]:
                    duplicate = True
                j += 1
            
            if duplicate:
                for k in range(i, j): invalid.add(k)
            elif int(t[i][2]) > 1000:
                invalid.add(i)
        
        return [','.join(t[i]) for i in invalid]