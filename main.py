from concept import get_concept_and_background
from personality import choose_characteristics
from background import generate_background_events, generate_higher_education_events, generate_career_progression_events
from specializations import specialize_from_events
from gear import assign_expanded_gear
from agendas import establish_expanded_agendas
from character_sheet import compile_character_sheet

def main():
    # Step 1: Concept and Background
    # name, homeworld, affiliation
    concept = get_concept_and_background()
    
    # Step 2: Personality descriptors
    personality = choose_characteristics()

    # Step 3: Higher Education (Optional)
    higher_education_choice = input("Do you want to go through Higher Education? (Y/N): ").lower()
    if higher_education_choice == 'y':
        higher_education, higher_education_events = generate_higher_education_events()
    else:
        higher_education_events = []

    # Step 4: Career Progression (User Chooses Career Path)
    career_path, career_events = generate_career_progression_events(higher_education_choice)

    # Step 5: Combine all events from background, higher education, and career
    events = background_events + higher_education_events + career_events

    # Step 6: Specializations from Events
    specializations = specialize_from_events(events)

    # Step 7: Distribute Attributes through Background
    #attributes = distribute_attributes_via_background()

    # Step 8: Expanded Gear Assignment
    gear = assign_expanded_gear()

    # Step 9: Establish Agendas
    agendas = establish_expanded_agendas(events)

    # Step 10: Compile Character Sheet
    compile_character_sheet(concept, attributes, events, specializations, gear, agendas)

if __name__ == "__main__":
    main()
