import numpy as np

class ImageProcessor:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def rotate(self):
        self.matrix = np.rot90(self.matrix, -1)   # 順時針 90 度

    def transpose(self):
        self.matrix = self.matrix.T

    def multiply(self, x):
        self.matrix = self.matrix * x

    def process_command(self, command):
        parts = command.split()
        if parts[0] == "ROTATE":
            self.rotate()
        elif parts[0] == "TRANSPOSE":
            self.transpose()
        elif parts[0] == "MULTIPLY":
            self.multiply(int(parts[1]))

r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]

processor = ImageProcessor(matrix)

k = int(input())
for _ in range(k):
    command = input().strip()
    processor.process_command(command)

final_r, final_c = processor.matrix.shape
print(final_r, final_c)
for row in processor.matrix:
    print(*row)