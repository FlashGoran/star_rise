import random

def assign_expanded_gear():
    print("\n=== Step 7: Gear and Plot Hooks ===")
    weapons = ["Plasma Rifle", "Vibro-Knife", "EMP Grenade"]
    gear = ["Portable Hacking Kit", "Med-Pack with Stims", "Advanced Tactical Suit"]
    plot_items = ["Encrypted Data Drive", "Alien Artifact", "Forged Identity Documents"]

    selected_weapon = random.choice(weapons)
    selected_gear = random.sample(gear, 2)
    selected_plot_item = random.choice(plot_items)

    return {
        "weapon": selected_weapon,
        "gear": selected_gear,
        "plot_item": selected_plot_item
    }
