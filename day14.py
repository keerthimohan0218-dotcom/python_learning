#NUMBER AND ALPHABET PATTERNS
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 n = 6
# for r in range(1, n+1):
#     for c in range(1, r+1):
#         print(c, end=" ")
#     print()
# print()


# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 
# 6 5 4 3 2 1 
# n = 6
# for r in range(1,n+1):
#     for c in range(r,0,-1):
#         print(c, end=" ")
#     print()
# print()

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 6 6 
# n = 6
# for r in range(1,n+1):
#     for c in range(r):
#         print(r, end=" ")
#     print()
# print()

# 1
# 1 1 
# 1 1 1 
# 1 1 1 1 
# 1 1 1 1 1 
# 1 1 1 1 1 1 
# n = 6
# for r in range(1,n+1):
#     for c in range(r):
#         print(1, end=" ")
#     print()
# print()

#           1 
#         1 2 
#       1 2 3 
#     1 2 3 4 
#   1 2 3 4 5 
# 1 2 3 4 5 6 

# n = 6
# for r in range(1, n+1):
#     for c in range(n-r):
#         print(" ", end=" ")
#     for c in range(1, r+1):
#         print(c, end=" ")
#     print()
# print()

#      1 
#     1 2 
#    1 2 3 
#   1 2 3 4 
#  1 2 3 4 5 
# 1 2 3 4 5 6 
# n = 6
# for r in range(1, n+1):
#     for c in range(n-r):
#         print("", end=" ")
#     for c in range(1, r+1):
#         print(c, end=" ")
#     print()
# print()

# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
# A B C D E F 
# n = 6
# for r in range(1, n+1):
#     for c in range(1, r+1):
#         print(chr(c+64), end=" ")
#     print()
# print()

# A 
# B A 
# C B A 
# D C B A 
# E D C B A 
# F E D C B A 
# n = 6
# for r in range(1, n+1):
#     for c in range(r, 0, -1):
#         print(chr(c+64), end=" ")
#     print()
# print()

# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
# A B C D E F 
# n = 6
# for r in range(1,n+1):
#     for c in range(1, r+1):
#         print(chr(c+64), end=" ")
#     print()
# print()

# A 
# A A 
# A A A 
# A A A A 
# A A A A A 
# A A A A A A 
# n = 6
# for r in range(1,n+1):
#     for c in range(1, r+1):
#         print(chr(65), end=" ")
#     print()
# print()

#           A 
#         A B 
#       A B C 
#     A B C D 
#   A B C D E 
# A B C D E F 
# n = 6
# for r in range(1, n+1):
#     for c in range(n-r):
#         print(" ", end=" ")
#     for c in range(1, r+1):
#         print(chr(c+64), end=" ")
#     print()
# print()
print()
#      A 
#     A B 
#    A B C 
#   A B C D 
#  A B C D E 
# A B C D E F 
# n = 6
# for r in range(1, n+1):
#     for c in range(n-r):
#         print("", end=" ")
#     for c in range(1, r+1):
#         print(chr(c+64), end=" ")
#     print()
# print()