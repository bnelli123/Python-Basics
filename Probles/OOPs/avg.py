'''
Input : arr[] = {1, 2, 3, 4, 5}
Output : 3
Sum of the elements is 1+2+3+4+5 = 15 
and total number of elements is 5.
So average is 15/5 = 3

Input : arr[] = {5, 3, 6, 7, 5, 3}
Output : 4.83333
Sum of the elements is 5+3+6+7+5+3 = 29
and total number of elements is 6.
So average is 29/6 = 4.83333.
'''
def avgOfNums(l1):
    summ_of_nums = 0
    for n in l1:
        summ_of_nums = summ_of_nums + n
    return  summ_of_nums / len(l1)

if __name__ == "__main__":
    arr = [10, 2, 3, 4, 5, 6, 7, 8, 9]
    result = avgOfNums(arr)
    print(result)