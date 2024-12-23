import json
import random
import os


def load_json(file_path):
    """Load a JSON file and return its content."""
    with open(file_path, 'r') as f:
        return json.load(f)


def calculate_success_chance(main_attrs, character_data, key_attribute=None):
    """Calculates success chance based on character's attributes."""
    if not main_attrs:
        return 50  # Default base chance if no main attributes are defined

    success_chances = []
    for attr in main_attrs:
        attr_value = character_data["aggregated_attributes"].get(attr.upper(), 0)
        base_chance = 50 + attr_value * 5

        # Add key attribute bonus if applicable
        if key_attribute and key_attribute.upper() == attr.upper():
            base_chance += 10  # Add a 10% bonus

        success_chances.append(base_chance)

    # Average success chances across all attributes
    average_chance = sum(success_chances) / len(success_chances)

    return min(average_chance, 100)  # Cap at 100%


def categorize_education_options(higher_ed_data, character_data):
    """Categorizes higher education options into High, Medium, and Low success chances."""
    categorized_options = {"High": [], "Medium": [], "Low": []}
    LOW_THRESHOLD = 60
    MEDIUM_THRESHOLD = 65
    HIGH_THRESHOLD = 75

    key_attribute = character_data.get("key_attribute", "").upper()

    for key, value in higher_ed_data.items():
        subclasses = value.get("subclasses", {})
        main_attrs = [sub.get("main_attr") for sub in subclasses.values() if "main_attr" in sub]

        # Calculate success chance using the new function
        success_chance = calculate_success_chance(main_attrs, character_data, key_attribute)

        if success_chance >= HIGH_THRESHOLD:
            categorized_options["High"].append((key, value, success_chance))
        elif success_chance >= MEDIUM_THRESHOLD:
            categorized_options["Medium"].append((key, value, success_chance))
        else:
            categorized_options["Low"].append((key, value, success_chance))

    return categorized_options


def present_subclass_options(subclasses, character_data, key_attribute):
    """Present subclass options and calculate success chances."""
    subclass_options = []
    print("\nAvailable Subclasses:")
    for idx, (name, details) in enumerate(subclasses.items(), start=1):
        main_attr = details["main_attr"]
        success_chance = calculate_success_chance([main_attr], character_data, key_attribute)
        print(f"{idx}. {name}: {details['description']} (Success Chance: {success_chance:.2f}%)")
        subclass_options.append((name, details, success_chance))
    return subclass_options


def process_success(character_data, subclass, success):
    """
    Process success or failure outcomes for an education path.
    """
    main_attr = subclass["main_attr"].upper()
    attr_points = 1
    skill_points = 4 if success else 3  # Distribute skill points based on success or failure
    debt_increase = 1
    specialization = None

    # Check for specialization cap
    max_cap = 5 if character_data["key_attribute"].upper() == main_attr else 4
    if character_data["aggregated_attributes"].get(main_attr, 0) + attr_points > max_cap:
        specialization = main_attr

    # Update character attributes
    character_data["aggregated_attributes"][main_attr] += attr_points
    character_data["debt"] = character_data.get("debt", 0) + debt_increase

    # Return the results
    return {
        "success": success,
        "title": subclass["title"] if success else None,
        "attr_points": attr_points,
        "skill_points": skill_points,
        "specialization": specialization,
        "debt_increase": debt_increase,
    }


def higher_education_step(character_data):
    """Runs the higher education selection and resolution process for a character."""

    # Load higher education data
    with open("content/higher_ed.json", "r") as file:
        higher_ed_data = json.load(file)["higher_education"]

    # Categorize education options
    categorized_options = categorize_education_options(higher_ed_data, character_data)

    # Present categorized options with unique numbering
    print("\nAvailable Higher Education Options:")
    all_options = []  # Flat list for numbering
    option_counter = 1  # Unique numbering across categories

    for category, options in categorized_options.items():
        print(f"\n{category} Success Chance:")
        for key, value, chance in options:
            print(f"{option_counter}. {key}: {value['description']} (Success Chance: {chance:.2f}%)")
            all_options.append((option_counter, key, value, chance))
            option_counter += 1

    # Get user choice by number
    while True:
        try:
            choice_num = int(input("Choose your university by number: ").strip())
            chosen_option = next((opt for opt in all_options if opt[0] == choice_num), None)
            if chosen_option:
                _, choice, education, success_chance = chosen_option
                break
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nYou selected: {choice}")

    # Present subclasses for the chosen university
    subclasses = education.get("subclasses", {})
    subclass_options = present_subclass_options(subclasses, character_data, character_data.get("key_attribute", "").upper())

    # Get user choice of subclass
    while True:
        try:
            subclass_choice_num = int(input("Choose your education path by number: ").strip())
            if 1 <= subclass_choice_num <= len(subclass_options):
                subclass_name, subclass_data, subclass_success = subclass_options[subclass_choice_num - 1]
                break
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nYou selected: {subclass_name}")

    # Roll for success
    roll = random.randint(1, 100)
    success = roll <= subclass_success

    # Process outcomes
    outcome = process_success(character_data, subclass_data, success)

    # Display results
    print("\nEducation Results:")
    print(f"- Success: {outcome['success']}")
    print(f"- Title: {outcome['title']}")
    print(f"- Attribute Points: +{outcome['attr_points']} to {subclass_data['main_attr']}")
    print(f"- Skill Points Distributed: {outcome['skill_points']}")
    print(f"- Specialization Gained: {outcome['specialization'] if outcome['specialization'] else 'None'}")
    print(f"- Corporate Debt Increased by: {outcome['debt_increase']}")

    return character_data
