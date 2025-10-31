from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # table1: {menu1: , menu2: ...}, table2: ...
        tables = {}
        menus = set()
        nums = set()
        for order in orders:
            _, num, menu = order
            if not tables.get(num):
                tables[num] = defaultdict(int)
            tables[num][menu] += 1
            menus.add(menu)
            nums.add(int(num))
        
        menus = sorted(menus)
        nums = sorted(nums)

        answer = [["Table"] + menus]
        for num in nums:
            tmp = [str(num)]
            for menu in menus:
                tmp.append(str(tables[str(num)][menu]))
            answer.append(tmp)

        return answer