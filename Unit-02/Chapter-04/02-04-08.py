s1 = int(input())
s2 = int(input())
s3 = int(input()) 

if not(s1 + s2 > s3) or s1 == 0 or s2 == 0 or s3 == 0:
    print("not a triangle")
elif s1 != s2 and s2 != s3 and s3 != s1:
    print("scalene")
elif s1 == s2 == s3:
    print("equilateral")
else:
    print("isosceles")