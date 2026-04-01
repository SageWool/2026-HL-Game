# checks users enter yes (y) or no (n)

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no / y /
        if response =="yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

To begin, choose the number of rounds and either customise 
the game parameters or go with the default game (where the
secret number will be between 1 and 100).

Then you must choose how many rounds you'd like to play, 
select <enter> for infinite mode.

Your end goal is to try to guess the 🔐secret🔐 number 
without running out of guesses.

Good luck player 

    """)
# checks for int more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer more than 1."

        to_check = input(question)

        # check for inf mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check if response more than 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine Starts Here

# initialize game variables
mode = "regular"
rounds_played = 0


print("⬆️⬆️⬆️ Welcome to the Higher Lower Game ⬇️⬇️⬇️")
print()

want_instructions = yes_no("Do you want to see the instructions? ")

# checks user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds? Or, push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    # HEADINGS
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n🎲🎲🎲 Round {rounds_played + 1} of {num_rounds} 🎲🎲🎲"

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# game loop ends here

# game history / stats area

# auto testing
to_test = [
    ('xlii', 'invalid'),
    ('0.5', 'invalid'),
    ('0', 'invalid'),
    (1, 1),
    (2, 2),
    ('', 'infinite'),
]

# run test
for i in to_test:
    # retrieve test case
    case = i[0]
    expected = i[1]

    #  get actual value
    actual = int_check(case)

    # comparing
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
