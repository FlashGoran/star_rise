def establish_expanded_agendas(events):
    print("\n=== Step 8: Expanded Agendas ===")
    personal_agenda = input("Enter personal agenda (short and long-term goals): ")
    corporate_agenda = input("Enter corporate agenda: ")
    national_agenda = input("Enter national agenda: ")

    return {
        "personal_agenda": personal_agenda,
        "corporate_agenda": corporate_agenda,
        "national_agenda": national_agenda
    }
