#DO EVERYTHING ON YOUR OWN
#right angle triangle
# *
# **
# ***
# ****
# *****
# n = 5
# for i in range(1, n+1):
#     print(i * "*")
print()

# right angle triangle with spaces
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# n = 5
# for i in range(1, n+1):
#     print(i * "* ")

#print
# *       *     * 
#   *     *   *   
#     *   * *     
#       * *       
# * * * * * * * * 
#     *   * *     
#   *     *   *   
# *       *     * 
# n = 8
# for row in range (n):
#     for col in range (n):
#         if row == col or col == n - row - 1 or row == n // 2 or col == n //2:
#             print("*", end=" ")
#         else :
#             print(" ", end=" ")           
#     print()

# ******
#  *****
#   ****
#    ***
#     **
#      *
# n= 6
# for i in range(n):
#     print(i*" " + (n-i)*"*")
# * * * * * * 
# *         * 
# *         * 
# *         * 
# *         * 
# * * * * * * 
# n = 6
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n - 1 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#      *
#     **
#    ***
#   ****
#  *****
# ******
# n= 6
# for i in range(n, -1, -1):
#     print(i*" " + (n-i)*"*")
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# n = 5
# for i in range(1, n + 1):
#     print((n - i) * " " + i * "* ")