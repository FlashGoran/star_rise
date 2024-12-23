def specialize_from_events(events):
    print("\n=== Step 4: Specializations ===")
    specializations = { # need updates
        "Close Combat": ["Blunt Combat Specialist", "Edge Combat Expert", "Explosives Expert"],
        "Heavy Machinery": ["Propulsion", "Industrial", "Starship Eng", "Power Sys", "Enviromental Sys", "Weapon Sys"],
        "Stamina": ["Tactical Evasion", "Radiation Resistant", "Thermal Resistant", "Dehydration Training", "Nutritional Endurance"],
        "Mobility": ["Athletics", "Dexterity", "Stealth Movement", "Zero-G Movement"],
        "Piloting": ["Space", "Remote Control", "Navigation", "Land", "Air", "Water"],
        "Ranged Combat": ["CQB Specialist", "Sniper", "Energy Weapons", "Automatic Weapons", "High-Tech Armament", "Cyber-Integrated Arms", "Precision Weapons"],
        "ComTech": ["Signal Intelligence", "AI Tech", "Robotics", "Computer Eng.", "Electronics Eng."],
        "Observation": ["Systems Analytics", "Surveillance", "Tactical Analytics", "Sensors", "Forensics", "Tactical Analytics", "Strategic Analytics"],
        "Command": ["Tactical Operations", "Leadership", "Strategic Planning", "Crisis Management", "Operational Planning"],
        "Manipulation": ["Negotiator", "Public Relations", "Social Engineering", "Cybernetics Expert", "PsyOps", "Interrogation", "Public Relations", "Social Engineering", "Forgery"],
        "Science": ["Geneticist", "Cybernetics Expert", "Astrogation", "Linguistics", "Biology", "Chemistry", "Cybernetics", "Xenology", "Psycology", "Physics", "Economics", "Medical Science". "Environmental Science", "Nanotechnology", "Quantum Mechanics", "Advanced Engineering"]
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
