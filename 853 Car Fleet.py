#There are n cars going to the same destination along a one-lane road. The destination is target miles away.
#You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).
#A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).
#A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.
#If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
#Return the number of car fleets that will arrive at the destination.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        closest = max(position)
        fleets  = 0
        last_time = 0

        for p, s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            if last_time < time:
                fleets += 1
                last_time = time
        
        return fleets
