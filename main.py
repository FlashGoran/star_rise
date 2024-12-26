from general_citizen_data import basic_profile
from personality import define_personality
from background import get_random_origin
from higher_education import higher_education_step
import pprint
#from specializations import specialize_from_events
#from agendas import establish_expanded_agendas
#from character_sheet import compile_character_sheet

def main():
    # Step 1: Concept and Background
    # name, homeworld, affiliation
    
    general_citizen_data = basic_profile()
    
    # Step 2: Personality descriptors
    personality = define_personality()

    # Step 3: Origin and Events
    origins_file = "./content/origins.json"
    origin_events_folder = "./content/origin_event_lists"

    character_data = get_random_origin(origins_file, origin_events_folder)
    print(f"Selected origin:")
    pprint.pprint(character_data)

    # todo need to fix the success rate for educations and event lists
    # base 50 % + 5% * attribute value
    # Step 4: Educations

    # Ask if the user wants to pursue higher education
    pursue_higher_ed = input("\nDo you want to pursue higher education?\nDo observe pursuing higher education is hard even for the best student -  (yes/no): ").strip().lower()
    if pursue_higher_ed == "yes" or pursue_higher_ed == "y":
        character_data = higher_education_step(character_data)
    else:
        print("Skipping higher education step.")

    # Step 6: Specializations from Events4
    #specializations = specialize_from_events(events)

    # Step 9: Establish Agendas
    #agendas = establish_expanded_agendas(events)

    # Step 10: Compile Character Sheet
    #compile_character_sheet(general_citizen_data, attributes, origin, specializations, agendas)

if __name__ == "__main__":
    main()
