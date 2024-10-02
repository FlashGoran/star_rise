from archetypes import background_events, higher_education_events, career_events, mishaps
import random

def generate_background_events():
    backgrounds = list(background_events.keys())
    print("Choose Background:")
    for i, option in enumerate(backgrounds, 1):
        print(f"{i}. {option}")
    background_choice = int(input("Select a background (1-6): "))
    chosen_background = backgrounds[background_choice - 1]

    # Generate 2 random background events
    background_event_list = random.sample(background_events[chosen_background], 2)
    return chosen_background, background_event_list

def generate_higher_education_events():
    education_options = list(higher_education_events.keys())
    print("Choose Higher Education Path:")
    for i, option in enumerate(education_options, 1):
        print(f"{i}. {option}")
    education_choice = int(input("Select a higher education option (1-6): "))
    chosen_education = education_options[education_choice - 1]

    # Generate 2 random higher education events
    higher_education_event_list = random.sample(higher_education_events[chosen_education], 2)
    return chosen_education, higher_education_event_list

def generate_career_progression_events(higher_education_completed):
    career_paths = list(career_events.keys())
    
    if not higher_education_completed:
        # Filter out careers that require higher education
        career_paths = [career for career in career_paths if career != "Some Restricted Career"]
    
    print("Choose Career Path:")
    for i, option in enumerate(career_paths, 1):
        print(f"{i}. {option}")
    career_choice = int(input(f"Select a career path (1-{len(career_paths)}): "))
    chosen_career = career_paths[career_choice - 1]

    # Simulate 3 career events if no higher education was chosen, or 2 if it was
    num_career_events = 3 if not higher_education_completed else 2
    career_event_list = random.sample(career_events[chosen_career], num_career_events)

    return chosen_career, career_event_list
