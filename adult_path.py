import json
import random
import pprint

# === Utility Functions ===
MASTER_BASE_CHANCE = 30


def load_json(file_path):
    """Load a JSON file and return its content."""
    with open(file_path, "r") as file:
        return json.load(file)


def calculate_success_chance(base_chance, main_attrs, character_data, key_attribute=None):
    """Calculates success chance based on character's attributes."""
    if not main_attrs:
        return base_chance

    success_chances = [
        base_chance + character_data["aggregated_attributes"].get(attr.upper(), 0) * 5
        + (10 if key_attribute and key_attribute.upper() == attr.upper() else 0)
        for attr in main_attrs
    ]
    return min(sum(success_chances) / len(success_chances), 100)


def get_user_choice(options, prompt):
    """Prompt the user to select an option."""
    while True:
        try:
            choice = int(input(prompt).strip())
            for opt in options:
                if opt[0] == choice:
                    return opt
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


# === Categorization and Display ===
def categorize_and_display_options(higher_ed_data, character_data, base_chance=50):
    """Categorizes and displays education options."""
    categorized = {"High": [], "Medium": [], "Low": []}
    thresholds = {"Low": 60, "Medium": 65, "High": 75}
    key_attr = character_data.get("key_attribute", "").upper()

    for key, value in higher_ed_data.items():
        main_attrs = [sub.get("main_attr") for sub in value.get("subclasses", {}).values() if "main_attr" in sub]
        success_chance = calculate_success_chance(base_chance, main_attrs, character_data, key_attr)
        category = (
            "High" if success_chance >= thresholds["High"] else
            "Medium" if success_chance >= thresholds["Medium"] else
            "Low"
        )
        categorized[category].append((key, value, success_chance))

    all_options = []
    print("\nAvailable Higher Education Options:")
    option_number = 1
    for category, options in categorized.items():
        print(f"\n{category} Success Chance:")
        for key, value, chance in options:
            print(f"{option_number}. {key}: {value['description']} (Success Chance: {chance:.2f}%)")
            all_options.append((option_number, key, value, chance))
            option_number += 1
    return all_options


def display_and_select_subclass(subclasses, character_data, key_attribute, base_chance=50):
    """Displays subclasses and allows the user to select one."""
    subclass_options = []
    print("\nAvailable Subclasses:")
    for idx, (name, details) in enumerate(subclasses.items(), start=1):
        success_chance = calculate_success_chance(base_chance, [details["main_attr"]], character_data, key_attribute)
        print(f"{idx}. {name}: {details['description']} (Success Chance: {success_chance:.2f}%)")
        subclass_options.append((idx, name, details, success_chance))
    return get_user_choice(subclass_options, "Choose your education path by number: ")


# === Processing Outcomes ===
def process_outcome(character_data, attr, skill_points, debt, title=None):
    """Update character attributes and debt after an outcome."""
    attr = attr.upper()
    character_data["aggregated_attributes"][attr] += 1  # Add attribute point
    character_data["debt"] = character_data.get("debt", 0) + debt
    return {
        "title": title,
        "attr_points": 1,
        "skill_points": skill_points,
        "debt_increase": debt,
    }


def roll_success(success_chance):
    """Roll for success and return the outcome."""
    roll = random.randint(1, 100)
    return roll <= success_chance, roll


# === Higher Education Flow ===
def process_education(character_data, subclass_data, success_chance):
    """Process the education selection and outcomes."""
    key_attr = character_data.get("key_attribute", "").upper()
    subclass_index, subclass_name, subclass_details, subclass_success = subclass_data

    print(f"\nYou selected: {subclass_name}")
    success, roll = roll_success(subclass_success)
    print(f"Roll: {roll} {'(Success)' if success else '(Failure)'}")

    # Process outcome, conditionally adding debt
    debt = subclass_details.get("debt_value", 0)  # Check for debt in regular education
    outcome = process_outcome(
        character_data,
        subclass_details["main_attr"],
        skill_points=4 if success else 3,
        debt=debt,
        title=subclass_details["title"] if success else None,
    )
    print(f"\nEducation Results: {outcome}")

    # Integrate chosen higher education into character data
    if "education" not in character_data:
        character_data["education"] = []  # Initialize if not already present

    education_entry = {
        "university": subclass_name,
        "success": success,
        "title": subclass_details["title"] if success else "Incomplete",
        "main_attr": subclass_details["main_attr"],
        "debt": debt,
    }
    character_data["education"].append(education_entry)

    return success, subclass_details



def process_master_education(character_data, subclass_name):
    """Handle the master's degree process if eligible."""
    # Load higher education data to find the master details for the subclass
    higher_ed_data = load_json("content/higher_ed.json")["higher_education"]
    master_data = None

    # Locate the master data based on the subclass name
    for university, details in higher_ed_data.items():
        subclasses = details.get("subclasses", {})
        if subclass_name in subclasses:
            master_data = subclasses[subclass_name].get("master")
            break

    if not master_data:
        print(f"\nNo master's degree data found for subclass: {subclass_name}")
        return False

    print(f"\nCongratulations! You qualify for a Master's.")
    print(f"Master's Title: {master_data['title']}")
    if "debt_value" in master_data:
        print(f"(Additional Debt: {master_data['debt_value']})")

    # Ask if the user wants to pursue the master's degree
    decision = get_user_choice([(1, "yes"), (2, "no")], "Would you like to pursue the master's degree? 1 for Yes, 2 for No: ")
    if decision[1] == "yes":
        # Calculate success chance for the master's degree
        master_success_chance = calculate_success_chance(
            30,  # Master's base chance
            [higher_ed_data[university]["subclasses"][subclass_name]["main_attr"]],
            character_data,
            character_data.get("key_attribute", "").upper(),
        )
        success, roll = roll_success(master_success_chance)
        print(f"Master's Success Chance: {master_success_chance:.2f}%")
        print(f"Roll: {roll} {'(Success)' if success else '(Failure)'}")

        if success:
            outcome = process_outcome(
                character_data,
                higher_ed_data[university]["subclasses"][subclass_name]["main_attr"],
                skill_points=5,
                debt=master_data.get("debt_value", 0),
                title=master_data["title"],
            )
            print(f"\nMaster's Education Results: {outcome}")
            character_data["education"].append({
                "university": university,
                "success": True,
                "title": master_data["title"],
                "main_attr": higher_ed_data[university]["subclasses"][subclass_name]["main_attr"],
                "debt": master_data.get("debt_value", 0),
            })
            return True
        else:
            print("\nYou failed to complete the master's degree.")
    return False


def offer_academic_careers(character_data, subclass_name):
    """Offer academic career options based on the subclass name."""
    academic_careers_data = load_json("content/academic_careers.json")

    # Locate academic careers based on the subclass name
    available_careers = None
    for university, details in academic_careers_data.items():
        if subclass_name in details:
            available_careers = details[subclass_name]
            break

    if not available_careers:
        print("\nNo specific academic careers were found for this path.")
        print("You will be redirected to a common career path.\n")
        career_options = [(1, "common")]
    else:
        print("\nCongratulations on completing your education!")
        print("You are now eligible for the following academic careers:\n")
        career_options = []
        option_number = 1

        for career in available_careers:
            print(f"{option_number}. {career['title']}: {career['description']}")
            career_options.append((option_number, career))
            option_number += 1

        # Add an option for common careers
        print(f"{option_number}. Choose a common career path")
        career_options.append((option_number, "common"))

    # Get user choice
    chosen_career = get_user_choice(career_options, "Choose your academic career by number: ")

    if chosen_career[1] == "common":
        print("\nYou chose a common career path. Details will be specified later.")
    else:
        career = chosen_career[1]
        print(f"\nYou selected: {career['title']}")
        character_data["academic_career"] = career

    pprint.pprint(character_data)
    return character_data


# === Main Flow ===
def adult_path(character_data):
    """Run the higher education selection and resolution process."""
    higher_ed_data = load_json("content/higher_ed.json")["higher_education"]

    # Categorize and select higher education option
    all_options = categorize_and_display_options(higher_ed_data, character_data)
    _, university, education, success_chance = get_user_choice(all_options, "Choose your university by number: ")

    # Select subclass and process education
    subclass_data = display_and_select_subclass(
        education.get("subclasses", {}),
        character_data,
        character_data.get("key_attribute", "").upper(),
    )
    subclass_name = subclass_data[1]  # Extract the name of the subclass
    success, subclass_details = process_education(character_data, subclass_data, success_chance)

    # Process master's degree if eligible
    if success and "master" in subclass_details:
        master_success = process_master_education(character_data, subclass_name)
        if master_success:
            offer_academic_careers(character_data, subclass_name)

    return character_data

