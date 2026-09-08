class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # nlogn
        position, speed = zip(*sorted(zip(position,speed), key=lambda x: x[0]))

        timeNeeded = []
        for i in range(len(speed)):
            timeNeeded.append((target - position[i]) / speed[i])
        
        nStuck = [timeNeeded[0]]
        for t in timeNeeded[1:]:
            # current one gets "stuck" in fleet jam
            while len(nStuck) > 0 and t >= nStuck[-1]:
                nStuck.pop(-1)
            nStuck.append(t)

        # print(position)
        # print(speed)
        # print(nStuck)
        return len(nStuck)