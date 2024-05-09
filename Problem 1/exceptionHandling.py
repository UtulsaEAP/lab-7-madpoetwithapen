def exceptionHandling():
    # Split input into 2 parts: name and age
    parts = input().split()
    name = parts[0]
    while name != '-1':
        # FIXME: The following line will throw ValueError exception.
        #        Insert try/except blocks to catch the exception.

        try:
            # Try to convert the second element to an integer and add 1 to it
            age = int(parts[1]) + 1
            print(f'{name} {age}')
        #except block to catch the exception when converting string to integer 
        except ValueError:
            # If the conversion fails, set age to 0 and print the name and age
            age = 0
            print(f'{name} {age}')
        
        
        # Get next line
        parts = input().split()
        name = parts[0]

if __name__ == '__main__':
    exceptionHandling()