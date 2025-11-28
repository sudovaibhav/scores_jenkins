import sys

if len(sys.argv) > 1:
    scores = [float(x) for x in sys.argv[1:]] 
else:
    scores = [50, 60, 70, 80, 90]
    print(f"No input given, using default scores: {scores}")

total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
min = min(scores)
max = max(scores)
print(f"Minimum: {min}\nMaximum: {max}")