"""
A simple program that generates birthday dates.
It can generate for the amount of people you want
and it can run a certain amount of times.
"""

import random, datetime

NUMBER_OF_SIMULATIONS = 100_000

def get_birthdays(number_of_birthdays):
    """The function that will generate the random birthdays."""
    birthdays = []
    start_of_year = datetime.date(2002, 1, 1)

    for _ in range(0, number_of_birthdays):
        number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + number_of_days
        birthdays.append(birthday)
    return birthdays

def get_match(list_of_birthdays):
    """The function that will compute if 
    there are two birthdays at the same date.
    It returns the first matching birthday.

    In linear time O(n)."""
    set_birthdays = set()

    for birthday in list_of_birthdays:
        if birthday in set_birthdays:
            return birthday
        else:
            set_birthdays.add(birthday)
    return None

def main():
    """The main function. Here starts the program."""
    # A tuple of months in order for display purposes.
    months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    while True:
        prompt = "How many birthdays shall I generate? (Max 100)\n> "
        answer = input(prompt)
        if answer.isdecimal() and int(answer) <= 100:
            num_birthdays = int(answer)
            break

    birthdays_list = get_birthdays(num_birthdays)
    

    # Print all birthdays generated
    for birthday in birthdays_list:
        print(f"{months[birthday.month - 1]} {birthday.day}, ", end='')
    print() # Print a newline
    
    # Compute if there are any matching birthdays
    matching = get_match(birthdays_list)
    if matching != None:
        date = f"{months[matching.month - 1]} {matching.day}"
        print(f"In this simulation multiple people have a birthday on {date}")
    else:
        print("In this simulation no people have their birthdays at the same time.")

    # Call the function that will do the loop of simulations
    matching_birthdays = loop_simulation(NUMBER_OF_SIMULATIONS, num_birthdays)
    # Call the function that will print the results
    print_result(matching_birthdays, num_birthdays)

def loop_simulation(number_of_times, number_of_birthdays):
    """A function that will run a simulation the 
    specified amount of times."""
    # Ask the user if he wants to run the simulation.
    prompt = f"Do you want to do {NUMBER_OF_SIMULATIONS} simulations?\n"
    prompt += "Press q to quit or any key to continue.\n> "
    answer = input(prompt)

    # If the user wants to quit, return from the function.
    if answer.lower() == 'q':
        return print("Thanks for coming to our simulator!")
    
    # A variable that holds the number of times a matching birthday was found.
    match_num = 0
    i = 1
    while i <= number_of_times:
        # Each 10_000 iterations print a message.
        if i % 10_000 == 0:
            print(f"{i} simulations done...")

        birthdays_list = get_birthdays(number_of_birthdays)
        matching = get_match(birthdays_list)
        if matching != None:
            match_num += 1
        
        i += 1
    return match_num

def print_result(num_matching_birthdays, number_of_birthdays):
    """Function that prints the result and computes the probability
    for the experiment we have done."""
    # Compute the probability of having matching birthdays.
    probability_matching = round((num_matching_birthdays / NUMBER_OF_SIMULATIONS) * 100, 2)

    # The message to print
    message = f"Out of {NUMBER_OF_SIMULATIONS} simulations of {number_of_birthdays} people, "
    message += f"there was a matching birthday in that group {num_matching_birthdays} times.\n"
    message += f"This means that {number_of_birthdays} people have {probability_matching}% "
    message += "chance of having a matching birthday in their group!\n"
    message += "That's probably more than you would think!"

    return print(message)

if __name__ == '__main__':
    main()