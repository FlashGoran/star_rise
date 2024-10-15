def specialize_from_events(events):
    print("\n=== Step 4: Specializations ===")
    specializations = {
        "Close Combat": ["Blunt Combat Specialist", "Edge Combat Expert", "Explosives Expert"],
        "Heavy Machinery": ["FTL Drive", "Industrial", "Starship Eng", "Power Sys", "Enviromental Sys", "Weapon Sys"],
        "Stamina": ["Tactical Evasion", "Radiation Resistant", "Thermal Resistant", "Dehydration Training", "Nutritional Endurance"],
        "Mobility": ["Athletics", "Dexterity", "Stealth Movement", "Zero-G Movement"],
        "Piloting": ["Space", "Drone/remote Operation", "Navigation", "Land", "Sky", "Water"],
        "Ranged Combat": ["CQB Specialist", "Sniper", "Energy Weapons", "Automatic Weapons", "High-Tech Armament", "Cyber-Integrated Arms", "Precision Weapons"],
        "ComTech": ["Signal Intelligence", "AI Tech", "Robotics", "Computer Engineering", "Electronics Engineering"],
        "Observation": ["Systems Analysis", "Surveillance", "Tactical Analysis", "Sensor Specialist", "Forensics", "Tactical Analysis", "Strategic Analysis"],
        "Survival": ["Wilderness", "Urban", "Hazardous Environments", "First Aid", "Psychological Resistance", "Extreme Environments", "Primitive Tech"],
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
