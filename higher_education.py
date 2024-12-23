import json
import random


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


def present_education_paths(subclasses, character_data, key_attribute):
    """Presents available subclasses (education paths) with success chances."""
    print("\nAvailable Education Paths:")
    subclass_options = []
    for idx, (key, value) in enumerate(subclasses.items(), start=1):
        main_attr = value.get("main_attr", "").upper()
        success_chance = calculate_success_chance([main_attr], character_data, key_attribute)
        print(f"{idx}. {key}: {value['description']} (Success Chance: {success_chance:.2f}%)")
        subclass_options.append((key, value, success_chance))
    return subclass_options


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


def higher_education_step(character_data):
    """Runs the higher education selection and resolution process for a character."""

    # Load higher education data
    with open("content/higher_ed.json", "r") as file:
        higher_ed_data = json.load(file)["higher_education"]

    # Categorize education options
    categorized_options = categorize_education_options(higher_ed_data, character_data)

    # Present categorized options with unique numbering
    print("\nAvailable Higher Education Options:\nDo observe the success chance is based on an average of the available educations inside the Universities!")
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

    # Present education paths (subclasses) for the selected university
    subclasses = education.get("subclasses", {})
    subclass_options = present_education_paths(subclasses, character_data, character_data.get("key_attribute", "").upper())

    # Get user choice of subclass
    while True:
        try:
            subclass_choice_num = int(input("Choose your education path by number: ").strip())
            if 1 <= subclass_choice_num <= len(subclass_options):
                subclass, subclass_data, subclass_success = subclass_options[subclass_choice_num - 1]
                break
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Roll for success
    roll = random.randint(1, 100)
    success = roll <= subclass_success

    # Award based on success or failure
    if success:
        print(f"\nSuccess! You succeeded in the {subclass}.")
        skill_points = 4  # 2 + 2 skill points
        attr_points = 1
    else:
        print(f"\nFailure. You struggled through the {subclass}.")
        skill_points = 4  # 1 + 1 + 2 skill points
        attr_points = 1

    # Allocate skill points randomly based on weights
    skill_weights = {}
    for skill, details in subclass_data["skills"].items():
        skill_weights[skill] = details["weight"]

    skill_distribution = random.choices(
        population=list(skill_weights.keys()),
        weights=list(skill_weights.values()),
        k=skill_points
    )

    for skill in skill_distribution:
        character_data.setdefault("skills", {})[skill] = character_data["skills"].get(skill, 0) + 1

    # Update attributes
    main_attr = subclass_data.get("main_attr", "").upper()
    if main_attr:
        character_data["aggregated_attributes"][main_attr] += attr_points

    # Update debt
    character_data["debt"] = character_data.get("debt", 0) + subclass_data.get("debt_value", 0)

    # Add education to selected events
    character_data.setdefault("selected_events", {})["higher_education"] = {
        "university": choice,
        "subclass": subclass,
        "success": success,
        "skills_gained": skill_distribution,
        "attribute_gained": {main_attr: attr_points} if main_attr else {},
        "debt_incurred": subclass_data.get("debt_value", 0),
    }

    # Display results
    print(f"\nEducation Results:")
    print(f"- Attribute Points: +{attr_points} to {main_attr}")
    print(f"- Skill Points Distributed: {skill_distribution}")
    print(f"- Corporate Debt Increased by: {subclass_data.get('debt_value', 0)}")

    return character_data
