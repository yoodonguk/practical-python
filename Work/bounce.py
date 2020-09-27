# bounce.py
#
# Exercise 1.5
# GitHub Test

height = 100
bounce = 0.6

for i in range(10):
    height = round(height * bounce, 4)
    print(i+1, height)
