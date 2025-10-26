class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        account_value=[]
        for row_idx , row in enumerate(accounts):
            customer_wealth = 0
            for col_idx, element in enumerate(row):
                customer_wealth = customer_wealth + element
            account_value.append(customer_wealth)
        max_wealth = max(account_value)
        return max_wealth
