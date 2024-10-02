def distribute_attributes_via_background():
    print("\n=== Step 2: Attributes (Earned Through Background) ===")
    attributes = {
        "Strength": 0,
        "Agility": 0,
        "Intelligence (Wits)": 0,
        "Wisdom (Empathy)": 0
    }
    earned_points = 0

    # Points are earned via background events
    background_events = [
        ("Strength", "You survived a physically taxing event", 1),
        ("Agility", "Your time on the run has sharpened your reflexes", 1),
        ("Intelligence (Wits)", "You developed critical problem-solving skills", 2),
        ("Wisdom (Empathy)", "You learned to connect with others in crisis", 1)
    ]

    for event in background_events:
        print(f"\nEvent: {event[1]}")
        choice = input(f"Would you like to gain +{event[2]} to {event[0]}? (Y/N): ").strip().upper()
        if choice == "Y":
            attributes[event[0]] += event[2]
            earned_points += event[2]
            print(f"Points Earned: {earned_points}")

    return attributes
