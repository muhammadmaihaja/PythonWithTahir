# Handling Exceptions

# Make a code to get user input and perform operations on it.

while True:
    try:
        new_user_age = int(input("Enter your age to verify entry:\n"))
        clubbing_allowable_age = new_user_age / 22

        if clubbing_allowable_age >= 1.81:
            print("This is exclusively for the young lads. \n STEP OUT PLEASE")
        elif clubbing_allowable_age >= 1:
            print("ACCESS GRANTED. \n GET IN AND ROCK DEAR CLUBEE!!!")

        else:
            print("ACCESS DENIED \nYOU ARE TOO YOUNG BRUV! GERARA HIA \n         HAHAHAHA")
        break

    except ValueError:
        print("This is not a valid input. Please enter your age in digits...")
    except ZeroDivisionError: # This doesnt work here. For instructional purposes
        print("Please enter a number greater than zero")
    except:
        break
    finally:
        print("The club check has ended.")
