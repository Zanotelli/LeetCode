class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def remove_until_ok(lista, next_num: int, curr_cost: int):
            count = 0
            for a in range(len(lista)):
                count += lista[a]
                if maxCost <= curr_cost-count or count > next_num:
                    return lista[a+1:]
            return []
        cost_list = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        cost_str = []
        max_size = 0
        for j in cost_list:
            cost_str.append(j)
            current = sum(cost_str)
            if current > maxCost:
                curr_size = len(cost_str)
                if curr_size < 2:
                    cost_str.pop(0)
                elif current > maxCost:
                    max_size = max(max_size, curr_size-1)
                    cost_str = remove_until_ok(cost_str[:], j, current)
        return max(max_size, len(cost_str))


print(Solution().equalSubstring('krpgjbjjznpzdfy', 'nxargkbydxmsgby', 14))