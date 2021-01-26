def sumOfNumbers(new_input, current_sum):
    numbers_list_str = new_input.strip().split(" ")
    numbers_ints = [int(val) for val in numbers_list_str]
    new_sum = sum(numbers_ints)
    return new_sum + current_sum

total_sum = 0


new_input = input("Please enter numbers or symbol:\n")


while new_input != 'q':

    total_sum = sumOfNumbers(new_input, total_sum)
    new_input = input("Please enter numbers or symbol, to exit press 'q'\n")


print(f"your sum is {total_sum}")