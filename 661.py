from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        smooth_img = [[0] * len(img[0]) for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                devisor = 0
                sum_ = 0
                for y in range(-1, 2):
                    y_cord = i + y
                    for x in range(-1, 2):
                        x_cord = j + x
                        if (0 <= y_cord < len(img)) and (0 <= x_cord < len(img[0])):
                            devisor += 1
                            sum_ += img[y_cord][x_cord]
                smooth_img[i][j] = sum_ // devisor
        return smooth_img
