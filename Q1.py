# Assignment 1 Question 1
# Done By: Natasha Heng Jeng Yee
# UOW ID Number: 6959684


# Set multiple_ten and prime_counter to default value 0
multiple_ten = 0
prime_counter = 0

while True:
    # Get user input for number
    number = int(input("Enter a positive number or negative to exit:"))
    
    # Negative number exit loop
    if (number < 0):
        print("Program ends")
        break
        
    # Find number of multiple of ten
    if (number%10 == 0):
        multiple_ten = multiple_ten + 1
    else:
        multiple_ten = multiple_ten
    
    # Check if not prime integer
    for i in range(2, number):
        if (number % i == 0):
            prime_counter = 0
            
    # If divisible by 1 and itself, prime_counter increases by 1
    prime_counter = prime_counter + 1
        
    # Print output
    print("{0:<15}{1}".format("Multiple Ten","Prime"))
    print("{0:^11}{1:^14}".format(multiple_ten, prime_counter))


