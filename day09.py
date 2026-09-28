Link : https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5: 
        print("Not Weird")
    elif 6 <= n <= 20:
         print("Weird")
    else:
        print("Not Weird")









link : https://www.hackerrank.com/challenges/write-a-function/copy-from/483695726
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True 
    else:
        return False
       
year = int(input())