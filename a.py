import numpy as np

class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = np.array(scores)

    def max_per_student(self):
        return np.max(self.scores, axis=1)

    def avg_per_subject(self):
        return np.mean(self.scores, axis=0)


# 讀輸入
N, M = map(int, input().split())
scores = []

for _ in range(N):
    row = list(map(int, input().split()))
    scores.append(row)

# 建立物件
analyzer = ScoreAnalyzer(scores)

# 計算
max_scores = analyzer.max_per_student()
avg_scores = analyzer.avg_per_subject()

# 輸出
print(*max_scores)
print(*[f"{x:.1f}" for x in avg_scores])