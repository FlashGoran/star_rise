import random

# Step 1: Concept and Background
def get_concept_and_background():
    print("=== Step 1: Concept and Background ===")

    # 1. Name and Profession
    name = input("Enter character name: ")
    role = choose_role()

    # 2. Generate Affiliation based on life choices or background events
    affiliation = generate_affiliation()

    # 3. Homeworld Generation (Core, Mid, Outer Sectors)
    homeworld = generate_homeworld()

    # 4. Backstory
    backstory = input("Enter significant backstory elements: ")

    return {
        "name": name,
        "role": role,
        "affiliation": affiliation,
        "homeworld": homeworld,
        "backstory": backstory
    }

# Function to choose role/profession for the character
def choose_role():
    roles = [
        "Captain/Officer/pilot", "Corporate Agent", "Pilot", 
        "Mechanical Engineer (Roughneck)", "Electronic Engineer", 
        "marine/pilot/engineer", "medical science office", "Security Officer"
    ]
    
    print("\nChoose a role/profession for your character:")
    for i, role in enumerate(roles, 1):
        print(f"{i}. {role}")
    
    choice = int(input(f"Select a role (1-{len(roles)}): "))
    return roles[choice - 1]

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
