class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        rest = []
        for i in range(len(restaurants)):
            if veganFriendly:
                if restaurants[i][2] != veganFriendly:
                    continue
            
            if restaurants[i][3] > maxPrice:
                continue
            
            if restaurants[i][4] > maxDistance:
                continue
            
            rest.append((restaurants[i][0], restaurants[i][1]))
        
        return [x[0] for x in sorted(rest, key = lambda x: (-x[1], -x[0]))]