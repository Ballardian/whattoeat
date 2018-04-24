import sweet
import savoury
import kitchencontents
import recipes

check = input("Are you hungry or just bored?\n").lower().strip()
while True:
    if check == "hungry":
        choice = input("Sweet or savoury_options?\n").lower().strip()
        if choice == "sweet_options":
            sweet.sweet_options()
        elif choice == "savoury_options":
            savoury.savoury_options()
        else:
            print("Please enter 'sweet_options' or 'savoury_options'.")
            choice = input("Sweet or savoury_options?\n").lower().strip()

    elif check == "bored":
        print("Stop this right now you hog, go and watch a cartoon with a glass of gin.")
        break
    else:
        print("Please enter 'hungry' or 'bored'.\n")
        check = input("Are you hungry or just bored?\n").lower().strip()


