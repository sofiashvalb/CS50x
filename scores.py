from cs50 import get_int

scores = []
for i in range(4):
    score = get_int("score: ")
    scores.append(score)
print(f"scores:", scores)
