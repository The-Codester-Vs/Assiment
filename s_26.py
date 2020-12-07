num = [1,4,2,6,8,9,5,10,13]
def sum_even(lst):
    even = 0
    for i in lst:
        if i%2 == 0:
            even += i
    return even

def sum_odd(lst):
    odd = 0
    for i in lst:
        if i%2 != 0:
            odd += i
    return odd

result_odd = sum_odd(num)
result_even = sum_even(num)
print("The sum of even numbers in the list", result_even)
print( "The sum odd numbers in the list ",result_odd)
