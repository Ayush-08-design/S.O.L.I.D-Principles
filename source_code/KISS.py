# KISS - Keep it Simple , Stupid
# Write simple , clear , and easy to understand code
# Overengineering leads to bugs , harder debugging and low readability


## Complex Version [Without KISS]
def sum_complex(numbers : list[int]):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total


## Simple Version [With KISS]
def sum_simple(numbers : list[int]):
    return sum(numbers)

## Usage
nums = [10 , 45 , 67 , 34]

print(f'Complex One - {sum_complex(nums)}')
print(f'Simple One - {sum_simple(nums)}')