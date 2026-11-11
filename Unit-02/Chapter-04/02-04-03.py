A = int(input())
B = int(input())
C = int(input())

tallest = A


if B > tallest:
    tallest = B


if C > tallest:
    tallest = C

print(tallest)
