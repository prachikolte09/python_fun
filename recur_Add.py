def sellandbuystock(prices: [int]):
     low , high = 0,1
     res = 0
     while low < len(prices) and high <len(prices):
         currr_profit = prices[high] - prices[low]
         #print(currr_profit)
         res = max(res, currr_profit)
         if currr_profit < 0:
             low = high
         high +=1
     return res


prices = [7,1,5,3,6,4]
print(sellandbuystock(prices))


def lengthOfLongestSubstring(self, s: str) -> int:
    slow , fast = 0, 1
    if s:
        sub_str = 1
        while fast < len(s):
            if s[slow]!= s[fast]:
                sub_str += 1
            else:
                slow = fast
            fast += 1
        return sub_str