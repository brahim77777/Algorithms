from BinarySearch import BinarySearch_Recursion


def main():
	test_BinarySearch_Recursion()



def test_BinarySearch_Recursion():
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],11) == False
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],-1) == False
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],10) == True
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],1) == True
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],2) == True
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],3) == True
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],4) == True
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],5) == True
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],6) == True
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],7) == True
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],8) == True
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],9) == True
	assert BinarySearch_Recursion([1,2,3,4,5,6,7,8,9,10],10) == True
def test_NegativeValues():
	
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],-10) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],-9) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],-8) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],-7) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],-6) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],-5) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],-4) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],-3) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],-2) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],-1) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],0) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],1) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],3) == True
	assert BinarySearch_Recursion([-10 , -9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3],5) == False

if __name__ == "__main__":
	main()
