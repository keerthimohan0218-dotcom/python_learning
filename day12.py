#FOR LOOP PROBLEMS
#basic understanding

#1. print numbers from 1 to 10 in one line

# for i in range(1, 11):
#     print(i, end=" ")
# print()

#2. print even numbers from 5 to 30 in one line

# for i in range(5, 31):
#     if i % 2 == 0:
#         print(i, end=" ")

#3. print odd numbers from 5 to 30 in one line

# for i in range(5, 31):
#     if i % 2 != 0:
#         print(i, end=" ")

#4. print numbers divisible by 5 from 1 to 30 in one line

# for i in range(1, 31):
#     if i % 5 == 0:
#         print(i, end=" ")

#5. print numbers divisible by both 5 and 7 from 1 to 100 in one line

# for i in range (1, 101):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i, end=" ")

#6. sum of numbers from 10 to 25 

# sum = 0
# for i in range(10, 26):
#     sum = sum + i
# print(sum)

#7. sum of numbers in any list


# list = [10, 20, 30, 40, 50]
# sum = 0
# for i in list:
#     sum = sum + i
# print(sum)

#8. multiplication table of a number

# n = int(input("Enter a number  : "))
# for i in range(1, 11):
#     print(n, "x", i, " = ", n * i)



#interview problems
#9. factorial 

# n = int(input("enter a number : "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(f"factorial of {n} is {fact}")

#10. fibonacci 

# n = int(input("Enter a number : "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end = " ")
#     a, b = b, a + b

#11. reverse a string

# s = input("Enter a string : ")
# rev = ""
# for i in range (len(s)-1,-1,-1):
#     rev += s[i]
# print(f"reverse of {s} is {rev}")

# s = input("Enter a string : ")
# rev = "" 
# for i in s:
#     rev = i + rev
# print(f"reverse of {s} is {rev}")

#12. count vowels in a string

# string = input("Enter a string : ")
# vowels = 'aeiouAEIOU'
# count = 0
# for c in string:
#     if c in vowels:
#         count += 1
# print(f"Number of vowels in {string} is {count}")

#13. count z's and y's in a string

# string = input("Enter a string : ")
# Letters = 'xyXY'
# count = 0
# for c in string:
#     if c in Letters:
#         count += 1
# print(f"Number of letters in {string} is {count}")

#14. check whether a number is prime number or not 

# n = int(input("Enter a number : "))
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")



#WHILE LOOP PROBLEMS
#basic understanding


#print 1 to 10 with while loop

# a = 1
# while a < 11:
#     print (a,end=' ')
#     a += 1
# print()

#print even numbers from 1 to 10

# a = 1
# while a < 11:
#     if a % 2 == 0:
#       print (a,end=' ')
#     a += 1
# print()

#print numbers divisible by both 5 and 7 from 1 to 500
#  
# a = 1
# while a < 500:
#     if a % 5 == 0 and a % 7 == 0:
#       print (a,end=' ')
#     a += 1
# print()




#interview problems

#count digits

# n = int(input("enter a number : "))
# count = 0
# while n > 0:
#     n // 10
#     count += 1


# n = 1234
# count = 0
# while n > 0:
#     n // 10
#     count += 1
# print(count)


#reverse a number

# n = int(input("Enter a number : "))
# temp = abs(n)
# rev = 0
# while temp > 0:
#     last_digit = temp % 10
#     rev = rev * 10 + last_digit
#     temp //= 10
# print(rev)

#palindrome number

# word = input("Enter a word : ")
# reversed_word = word[ : : -1]
# if word == reversed_word:
#     print("palindrome number")
# else:
#     print("Not palindrome number")

#palindrome string (without slicing, built in function)

word = input("Enter a word : ")
reversed_word = ""
for character in word:
    reversed_word = character + reversed_word
if word == reversed_word:
     print("palindrome number")
else:
    print("Not palindrome number")

#armstrong number

