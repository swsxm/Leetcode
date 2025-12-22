from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        visiting = set()  
        completed = set() 

        def check(course):
            if course in visiting:
                return False
            
            if course in completed:
                return True

            visiting.add(course)
            
            for prereq in pre_map[course]:
                if not check(prereq):
                    return False
            
            visiting.remove(course)
            completed.add(course)
            return True

        for i in range(numCourses):
            if not check(i):
                return False
        
        return True