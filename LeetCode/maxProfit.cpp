class Solution {
public:
    int maxProfit(vector<int>& prices) {
        /*
        Second attempt (with research)
        Pseudo-code:
        1. If length array < 2, return 0
        2. Set profit = 0, set buyPrice = prices[0]
        3. Iterate from index 1 to end of the array
        4. If element < buyPrice
         buyPrice = element
        5. Else
         if (element - buyPrice) > profit
          profit = element - buyPrice
        6. Return profit
        */
        size_t  n = prices.size();
        if (n < 2) {
            return 0;
        }
        int profit = 0;
        int buyPrice = prices[0];
        for (int i = 1; i<n; i++) {
            if (prices[i] < buyPrice) {
                buyPrice = prices[i];
            }
            else {
                if ((prices[i] - buyPrice) > profit) {
                    profit = prices[i] - buyPrice;
                }
            }
        }
        return profit;
    }

    int maxProfit2(vector<int>& prices) {
        /*
        First attempt: timeout
        Pseudo-code:
        1. Initialize the profit = 0
        2. Parse the array with index i = 0
        3. Parse the array with index j = i+1
        4. Compare the profit from day price j - price i with the current profit
        5. If the profit j - i is bigger than profit, update profit
        */
        int profit = 0;
        size_t  n = prices.size();
        for (int i = 0; i<n; i++) {
            for (int j = i+1;j<n; j++) {
                int profit_i = prices[j] - prices[i];
                if (profit_i > profit) {
                    profit = profit_i;
                }
            }
        }
        return profit;
    }
};