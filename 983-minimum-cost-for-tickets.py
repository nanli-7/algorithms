""" 983. Minimum Cost For Tickets - Medium
# dynamic programming

In a country popular for train travel, you have planned some train travelling
one year in advance.  The days of the year that you will travel is given as an
array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a
7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given
list of days.

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.


Note:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000 """

# Approach 1: Dynamic Programming (Day Variant)

# For each day, if you don't have to travel today, then it's strictly better to
# wait to buy a pass. If you have to travel today, you have up to 3 choices: you
# must buy either a 1-day, 7-day, or 30-day pass.

# We can express those choices as a recursion and use dynamic programming. Let's
# say dp(i) is the cost to fulfill your travel plan from day i to the end of the
# plan. Then, if you have to travel today, your cost is:

# dp(i)=min(dp(i+1)+costs[0],dp(i+7)+costs[1],dp(i+30)+costs[2])


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dayset = set(days)
        durations = [1, 7, 30]

        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c for d, c in zip(durations, costs))
            else:
                return dp(i + 1)

        return dp(1)


if __name__ == "__main__":
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    res = Solution().mincostTickets(days=days, costs=costs)
    print(res)