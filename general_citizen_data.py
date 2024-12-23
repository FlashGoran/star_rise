import random

# Step 1: Concept and Background
def basic_profile():
    print("=== Step 1: Concept and Background ===")

    #Name and Profession
    name = input("Enter character name: ")

    age_min = 24
    age_max = 65
    while True:
        try:
            age = int(input(f"Enter character age between {age_min} and {age_max} years: "))
            if age_min <= age <= age_max:
                print(f"Character age set to {age}.")
                break
            else:
                print(f"Age must be between {age_min} and {age_max} years. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    sex = input("Enter your sex: ")

    #Generate Affiliation based on life choices or background events
    affiliation = generate_affiliation()

    #Homeworld Generation (Core, Mid, Outer Sectors)
    homeworld = generate_homeworld()

    return {
        "name": name,
        "age": age,
        "sex": sex,
        "affiliation": affiliation,
        "homeworld": homeworld,
    }

# Function to generate an affiliation based on background choices
def generate_affiliation():
    affiliations = [
        {"name": "Helios Corporation", "type": "Major corporation focused on deep space mining and exploration"},
        {"name": "NovaTech Systems", "type": "Cutting-edge technology firm specializing in AI and robotics"},
        {"name": "Outer Reach Coalition", "type": "Independent group governing outer rim colonies"},
        {"name": "Interstellar Trade Syndicate", "type": "Powerful trade organization controlling transport routes"},
        {"name": "Unified Planetary Alliance (UPA)", "type": "Coalition of mid-sector planets focused on military dominance"},
        {"name": "Deep Horizon Research", "type": "Scientific organization focused on alien lifeforms and new technologies"}
    ]
    
    print("\nYour character's affiliation is tied to their background. Here are some possible affiliations:")
    for i, affiliation in enumerate(affiliations, 1):
        print(f"{i}. {affiliation['name']} - {affiliation['type']}")
    
    # Affiliation will be chosen or rolled later based on background events, for now we'll assign one
    random_affiliation = random.choice(affiliations)
    print(f"Assigned Affiliation: {random_affiliation['name']}")
    return random_affiliation['name']

# Function to generate homeworld and sector
def generate_homeworld():
    sectors = ["Core Sector", "Mid Sector", "Outer Sector"]
    core_worlds = ["Elysium", "Valkoria", "Primus"]
    mid_worlds = ["Haven IV", "Nimbus", "Drexis"]
    outer_worlds = ["Xion", "Brimstone", "Hades-9"]
    
    # Randomly assign sector and world
    sector = random.choice(sectors)
    if sector == "Core Sector":
        world = random.choice(core_worlds)
    elif sector == "Mid Sector":
        world = random.choice(mid_worlds)
    else:
        world = random.choice(outer_worlds)

    print(f"\nHomeworld assigned: {world} in the {sector}")
    return f"{world} ({sector})"
