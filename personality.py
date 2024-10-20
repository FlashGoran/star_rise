def choose_characteristics():
    characteristics = {
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
    
    print("Rate your character's tendency on a scale from 1-5:")
    print("1 means strongly towards the characteristic on the left, 3 is neutral, and 5 means strongly towards the characteristic on the right.")
    
    for characteristic_pair in characteristics:
        while True:
            try:
                choice = int(input(f"{characteristic_pair}: "))
                if choice in range(1, 6):
                    characteristics[characteristic_pair] = choice
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
    
    print("\nYour character's chosen tendencies:")
    for characteristic, value in characteristics.items():
        print(f"{characteristic}: {value}")

    return characteristics

# Call the function to test
choose_characteristics()
