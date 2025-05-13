maze = [
    ['s', '_', '#', '#', '_', '_', '_', '_', '_', '_', '_', '_', '_', '#', '#', '#'],
    ['#', '_', '#', '#', '_', '#', '#', '#', '#', '#', '_', '#', '#', '_', '#', '_'],
    ['#', '_', '_', '_', '_', '#', '_', '_', '_', '#', '_', '_', '_', '_', '#', '_'],
    ['#', '#', '#', '#', '_', '#', '#', '_', '#', '#', '#', '_', '#', '#', '#', '_'],
    ['#', '_', '_', '_', '_', '_', '#', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['#', '#', '_', '#', '#', '#', '#', '#', '#', '#', '#', '_', '_', '#', '_', '_'],
    ['#', '_', '_', '_', '#', '_', '_', '_', '#', '_', '_', '_', '#', '_', '_', '_'],
    ['#', '#', '#', '#', '_', '#', '#', '_', '#', '#', '#', '_', '#', '#', '#', '#'],
    ['#', '_', '_', '_', '#', '_', '_', '_', '#', '_', '_', '_', '#', '_', '_', '_'],
    ['#', '_', '#', '#', '_', '#', '#', '#', '#', '#', '#', '_', '#', '#', '_', '_'],
    ['#', '_', '#', '#', '_', '_', '_', '_', '_', '_', '_', '_', '#', '#', '_', '_'],
    ['#', '#', '#', '#', '_', '#', '#', '#', '#', '#', '_', '#', '#', '#', '#', '_'],
    ['#', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '#', '_', '_', '#', '_'],
    ['#', '#', '_', '#', '#', '#', '#', '#', '#', '#', '#', '#', '_', '_', '_', '_'],
    ['#', '_', '_', '_', '_', '_', '_', '_', '#', '_', '_', '_', '_', '_', '_', '_'],
    ['#', '#', '#', '#', '_', '#', '#', '_', '_', '_', '#', '_', '#', '#', '#', '#'],
]


maze[-1][-1] = 'o'


moves = [[+1,0],[0,1],[0,-1],[-1,0]]

visited = set()
path=[]
path.append([0,0])

def dps(maze,x,y):
	if not (0<=x<len(maze) and 0<=y<len(maze)):
		return False

	if maze[x][y] == "#" or (x,y) in visited:
		return False

	if maze[x][y] == "o":
		print('Path Found')
		return True

	maze[x][y] = '!'
	visited.add((x,y))
	path.append([x,y])

	for move in moves:
		if dps(maze,x+move[0],y+move[1]):
			return True


	path.pop()
	# maze[x][y] ='_'
	return False
			

dps(maze,0,0)
for row in maze:
	print(row)

#Sum of array using recursion
arr = [1,2,3,4,5,6,7]

def sum_arr(arr):
	if len(arr)==0:
		return 0
	print(arr[-1])
	return arr[-1] + sum_arr(arr[:-1])

print(sum_arr(arr))

#Count down from n to 1

n=20

def count_n(n):
	if n<=0:
		return None
	print(n)
	count_n(n-1)

count_n(n)

#factorial of a number

n = 10

def factorial(n):
	if n==0:
		return 1
	return n*factorial(n-1)

print(factorial(n))

#Binary Search

arr=[1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20]
search=13

def binary_search(arr,search,left,right):
	mid=(left+right)//2
	
	if arr[mid] == search:
		return mid

	if arr[left]==arr[right]:
		return None

	if search>arr[mid]:
		return binary_search(arr,search,mid+1,right)

	if search<arr[mid]:
		return binary_search(arr,search,left,mid)

print(binary_search(arr,search,0,len(arr)-1))

#Palindrome Check

string = "nnaann"

def check_palindrome(string):
	if len(string)<=1:
		return True

	if string[0] != string[-1]:
		return False
			
	return check_palindrome(string[1:-1])

print(check_palindrome(string))
