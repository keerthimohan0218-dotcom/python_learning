#Arithmetic 

# # + : 
# a = 45 + 4.5
# b = True + False 
# c = 4+5j + 6+7j
# # d = None + 5 
# e = [1,2,3] + [4,5,6]
# f = (1,2,3) + (4,5,6)
# g = 'rak' + 'esh'
# #h = range(1,4) + range(4,7)
# i = {1,2,3} + {4,5,5}
# j = {1:'a', 2:'b'} + {3:'c', 4:'d'}
# # k = [1,2,3] + (1,2,3)
# # l = [1,2,3] + 'rak'
# print(a)        #49.5
# print(b)        #1
# print(c)        #(10+12j)
# # print(d)        #TypeError
# print(e)        #[1, 2, 3, 4, 5, 6]
# print(f)        #(1, 2, 3, 4, 5, 6)
# print(g)        #rakesh
# # print(h)        #range(1, 7)
# print(i)        #{1, 2, 3, 4, 5}
# print(j)       #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# # print(k)        #error
# # print(l)        #error

# # - : 
# a = 45 - 5.5
# b = 4+5j - 3+2j 
# c = True - False 
# # d = [1,2,3] - [2,3]
# e = (1,2,3) - (2,3)
# f = {1,2,3,4} - {2,1}
# g = {1:'a', 2:'b', 3:'c'} - {2:'b', 3:'c'}
# print(a)       #39.5
# print(b)       #(1+3j)
# print(c)       #1
# # print(d)       #[1] error
# print(e)       #(1, 2)
# print(f)       #{3, 4}
# print(g)       #{1: 'a'}

#* : 
# a = 4 * 5.4
# b = True * False 
# c = (4+5j) * (3+2j)
# # d = [1,2,3] * (2,3)
# e = [1,2,3] * 3 
# # f = [1,2,3] * 3.0
# g = (1,2,3) * 3 
# h = 'rakesh' * 3 
# # i = {1,2,3} * 3 
# # j = {1:'a', 2:'b', 3:'c'} * 3
# k = [1,2,3]
# l = range(1,2,3)
# m = (4,5,6)
# print(a)      #21.6
# print(b)       #0
# print(c)       #(2+27j)
# # print(d)
# print(e)       #[1, 2, 3, 1, 2, 3, 1, 2, 3]
# # print(f)
# print(g)  #(1, 2, 3, 1, 2, 3, 1, 2, 3)
# print(h)   #rakeshrakeshrakesh
# # print(i)
# # print(j)
# print(*k)   #1 2 3
# print(*l)    #1
# print(*m)   #4 5 6

# # ** : power 
# a = 5 ** 2 
# b = 3 ** 2.3
# c = (3+4j) ** (1+2j)
# print(a)   #value
# print(b) #value
# print(c)  #value

# # / :
# a = 5 / 2     
# print(a)   #2.5

# # // : 
# a = 5 // 2     
# print(a)    #2
# a = 5.5 // 2    
# print(a)      #2.0

# % : 
# a = 5 % 2 
# print(a)  #1


# # #Relational Operators 
# print(5 == 6.5)
# print(1 == True)
# print(2 == None)
# print(4+5j == 4+6j)
# print(5 > 6.5)
# print(1 > True)
# print(2 > None)
# print(4+5j > 3+2j)
# print([1,2,3] == [1,2,4])
# print([1,2,3] > [1,3,4])
# print((1,2,3) > (1,3,4))
# print({1,2,3} > {1,2}) 
# # print({1:2, 2:3} > {3:4, 4:5})
# print({1:2, 2:3} == {1:2, 2:3})
# print([1,2,3] == (1,2,3))
# print([1,2,3] > (1,2,3))  

# # #True or False
# print(bool(0))    #False
# print(bool(4.5))  #True
# print(bool(''))   #False
# print(bool('r'))  #True
# print(bool([]))   #False
# print(bool([1]))  #True
# print(bool(None)) 

# print()
# print()
# # #Logical Operators
# print( 4 and 0 and 6 )   #0
# print( 4 and 1 and 6 )   #6
# print( 4 or 0 or 6)      #4
# print(0 or '' or [])     #[]
# #mixed
# print(4 or 0 and 6)   
# #not reverse the bool value
# print(not False) 
# print(not True) 

# #Assignment operators
# a = 10 
# a += 20
# a -= 10
# a *= 2 
# a **= 2
# a /= 2 
# a //= 3
# a %= 3
# print(a)

# #Identity Operators 
# a = 34 
# b = 34 
# print(a is b) 
# a = 3+4j 
# b = 3+4j 
# print(a is b) 
# a = [1,2,3]
# b = [1,2,3]
# print(a is b)
# a = 'rakesh'
# b = 'rakesh'
# print(a is b)
# a = range(1,4)
# b = range(1,4)
# print(a is b)
# a = (1,2,3)
# b = (1,2,3)
# print(a is b)
# a = {1,2,3}
# b = {1,2,3}
# print(a is b)
# print()
# print()

# #Membership 
# a = [1,2,3,4]
# b = {1,2,3,4}
# c = 'rakesh'
# d = (1,2,3,4)
# e = {1:'a', 2:'b', 3:'c'}
# f = range(1,4)
# print(5 in a)
# print(3 in b)
# print('r' in c)
# print(4 in d)
# print('b' in e)
# print(3 in e)
# print(4 in f)

# #Walrus operator
# # print(a = 4)
# print(a := 4)
# print(a)

# #ternary operator 
# a = 5 if 10 > 20 else 6 
# print(a)
# a = [1,2,3] if 5 < 10 else (1,2,3)
# print(a)
