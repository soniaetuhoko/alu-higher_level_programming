def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):  # Loop through the range up to x
        try:
            print(my_list[i], end=' ')  # Print the element without a newline
            count += 1  # Increment the count for each printed element
        except IndexError:
            break  # Exit the loop if the index is out of range
    print()  # Print a newline after the loop
    return count  # Return the number of elements printed

