from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda i: i[0])
        i = 0
        max_boundary = 0
        counter = 0
        while i < len(clips) and max_boundary < time:
            curr_boundary = 0
            if max_boundary < clips[i][0]:
                return -1 
            while i < len(clips) and clips[i][0] <= max_boundary:
                curr_boundary = max(curr_boundary, clips[i][1])
                i+=1
            max_boundary = curr_boundary
            counter += 1
        return -1 if max_boundary < time else counter 

sol = Solution()
clips = [[0,1],[1,2]]
time = 5 
print(sol.videoStitching(clips, time))
                

