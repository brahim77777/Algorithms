import random
def main():

	while True:
		print("number:")
		numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
		print(numbers)
		print("value : ")
		value = int(input("search for:")) 
		if BinarySearch_Recursion(numbers , value):
			print(f"+++++++++ {value}  ==>Found! ++++++++++++")
		else : 
			print(f"--------- {value}   ==>not Found ----------")
		
		if value in numbers:
			print("Python says ==> Found!")
		else : 
			print("Python says ==> Not found!")	
# Complexity is "Olog(n)"
# List must be Sorted.


def BinarySearch(number):
	# Linear search is dead simple searh algorithm
	a = 1
	# [1,2,3,4,5,6,7,8]
	# [1]
def BinarySearch_Recursion(numbers, value):
	middle = 0
	# if list is empty return Fslse
	if len(numbers) == 0:
		return False
	# if list is two or less elements , pick the first as the middle
	if len(numbers) <= 2 :
		middle = 0
	# if list is 3 or more , [1,2,3]: pick the length(3) /2 = 1.5 , and keep only the  integer value 
	# 		       , [1,2,3,4] : pick length(4) /2  = 2   , 
	else : 
		middle = int(len(numbers)/2)
	
	# [1,2,3,4,5] , value = 2 
	if numbers[middle] == value : 
		return True
	if value > numbers[middle]:	
		return BinarySearch_Recursion(numbers[middle+1:], value)
	if value < numbers[middle]:
		return BinarySearch_Recursion(numbers[:middle], value)
	elif len(numbers) == 1 :
		return False
		

def GenerateList():
	numbers = []
	for _ in range(10):
		numbers.append(random.randint(0,1000))
	return sorted(numbers)


if __name__ == "__main__":
	main()


