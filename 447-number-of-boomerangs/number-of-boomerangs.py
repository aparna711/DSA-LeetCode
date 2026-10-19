class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 148 Aparna Hari Nair
        count = 0

        for i in range(len(points)):
            distances = {}

            for j in range(len(points)):
                if i == j:
                    continue

                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]

                dist = dx * dx + dy * dy

                distances[dist] = distances.get(dist, 0) + 1

            for freq in distances.values():
                count += freq * (freq - 1)

        return count
