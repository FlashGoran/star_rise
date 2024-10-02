def specialize_from_events(events):
    print("\n=== Step 4: Specializations ===")
    specializations = {
        "Close Combat": ["Blunt Combat Specialist", "Edge Combat Expert", "Explosives Expert"],
        "Ranged Combat": ["CQB Specialist", "Sniper", "Energy Weapons Specialist"],
        "ComTech": ["Signal Intelligence", "AI Specialist", "Robotics"],
        "Science": ["Xeno-Biologist", "Geneticist", "Cybernetics Expert"]
    }

    selected_specializations = []

    for event in events:
        print(f"Event: {event['description']}")
        if event['bonus'][0] in specializations:
            print(f"Choose a specialization for {event['bonus'][0]}:")
            available_specializations = specializations[event['bonus'][0]]
            for i, spec in enumerate(available_specializations, 1):
                print(f"{i}. {spec}")
            choice = int(input("Select a specialization: "))
            selected_specializations.append(available_specializations[choice - 1])

    return selected_specializations
