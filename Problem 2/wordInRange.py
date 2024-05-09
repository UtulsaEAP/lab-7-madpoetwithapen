def wordInRange():
    
    file_name = input()
    lower_bound = input()
    upper_bound = input()

    # Read file contents
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Iterate over each line and check if it falls within the range
    for line in lines:
        word = line.strip()
        if lower_bound <= word <= upper_bound:
            print(word + " - in range")
        else:
            print(word + " - not in range")

    # Print a newline to end the output
    print()


    return
if __name__ == '__main__':
    wordInRange()