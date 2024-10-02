def compile_character_sheet(concept, attributes, events, specializations, gear, agendas):
    print("\n=== Final Character Sheet ===")
    print(f"Name: {concept['name']}")
    print(f"Role: {concept['role']}")
    print(f"Affiliation: {concept['affiliation']}")
    print(f"Homeworld: {concept['homeworld']}")
    print(f"Personality Traits: {concept['personality_traits']}")
    print(f"Backstory: {concept['backstory']}")

    print("\n--- Attributes ---")
    for attr, value in attributes.items():
        print(f"{attr}: {value}")

    print("\n--- Events ---")
    for event in events:
        print(f"Event: {event['description']}")
        print(f"  Bonus: +{event['bonus'][2]} to {event['bonus'][1]}")
        print(f"  Penalty: -{event['penalty'][2]} to {event['penalty'][1]}")

    print("\n--- Specializations ---")
    print(f"Specializations: {', '.join(specializations)}")

    print("\n--- Gear ---")
    print(f"Weapon: {gear['weapon']}")
    print(f"Gear: {', '.join(gear['gear'])}")
    print(f"Plot Item: {gear['plot_item']}")

    print("\n--- Agendas ---")
    print(f"Personal Agenda: {agendas['personal_agenda']}")
    print(f"Corporate Agenda: {agendas['corporate_agenda']}")
    print(f"National Agenda: {agendas['national_agenda']}")
