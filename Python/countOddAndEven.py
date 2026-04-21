'''
Input: arr = [2, 3, 4, 5, 6]
Output: 2 3 
Explanation: There are two odds[3, 5] and three even[2, 4, 6] present in the array.
'''
input = [2,3,4,5,6,2,4,3,5]

result_even = []
result_odd = []
for num in input:
    if num % 2 == 0:
        result_even.append(num)
    if num % 2 == 1:
        result_odd.append(num)

print(len(result_even), len(result_odd))

#%%
input = [2,3,4,5,6,2,4,3,5]
even_count = 0
odd_count = 0

for n in input:
    if n % 2 == 0:
        even_count = even_count + 1
    if n % 2 == 1:
        odd_count = odd_count + 1

print(even_count, odd_count)

#%%
def printEvenOddCount(l1):
    even_num_count = 0
    odd_num_count = 0
    for n in l1:
        if n % 2 == 0:
            even_num_count += 1
        if n % 2 == 1:
            odd_num_count += 1
    return even_num_count, odd_num_count

if __name__ == "__main__":
    input = [2,3,4,5,6,2,4,3,5]
    result = printEvenOddCount(input)
    print(result[0], result[1])