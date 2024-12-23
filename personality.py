import random

def define_personality():
    personality_descriptors = {
        "Diplomatic - Confrontational": None,
        "Passive - Provocative": None,
        "Cautious - Daring": None,
        "Selfless - Self-Interested": None,
        "Trusting - Wary": None,
        "Rational - Emotional": None,
        "Hopeful - Realistic": None,
        "Sociable - Reserved": None,
        "Organized - Disorganized": None,
        "Assertive - Hesitant": None,
        "Efficient - Easygoing": None
    }

    print("\nRate your character's tendencies on a scale from 1 to 5:")
    print("- 1: Strongly towards the characteristic on the left.")
    print("- 3: Neutral.")
    print("- 5: Strongly towards the characteristic on the right.")
    print('- Or enter "r" to randomize all values.\n')

    while True:
        choice = input("Enter 'r' to randomize all values or press Enter to proceed manually: ").strip().lower()
        if choice == "r":
            for descriptor in personality_descriptors:
                personality_descriptors[descriptor] = random.randint(1, 5)
            print("\nRandomized personality values:")
            for descriptor, value in personality_descriptors.items():
                print(f"- {descriptor}: {value}")
            return personality_descriptors
        elif choice == "":
            break
        else:
            print("Invalid input. Enter 'r' to randomize all values or press Enter to proceed manually.")

    for descriptor in personality_descriptors:
        while True:
            try:
                value = int(input(f"{descriptor}: "))
                if 1 <= value <= 5:
                    personality_descriptors[descriptor] = value
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 5.")

    print("\nYour character's chosen tendencies:")
    for descriptor, value in personality_descriptors.items():
        print(f"- {descriptor}: {value}")

    return personality_descriptors
