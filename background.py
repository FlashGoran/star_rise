import json
import random
import os

def load_json(file_path):
    """Load a JSON file and return its content."""
    with open(file_path, 'r') as f:
        return json.load(f)

def weighted_random_choice(options):
    """Select a random option based on weights."""
    total_weight = sum(option["weight"] for option in options)
    random_choice = random.uniform(0, total_weight)
    current = 0
    for option in options:
        current += option["weight"]
        if random_choice <= current:
            return option

def get_random_event(event_key, events_folder):
    """
    Load the corresponding event file based on the event_key.
    Randomly select one event from each stage (early, mid, late).
    """
    event_file_path = os.path.join(events_folder, f"{event_key}.json")
    if not os.path.exists(event_file_path):
        raise FileNotFoundError(f"Event file not found: {event_file_path}")

    events = load_json(event_file_path)

    selected_events = {
        "early": random.choice(events["early"]),
        "mid": random.choice(events["mid"]),
        "late": random.choice(events["late"]),
    }

    return selected_events

def calculate_aggregated_attributes(events, key_attribute, attributes=["STR", "AGI", "INT", "WIS"], total_points=11):
    """
    Aggregate attribute modifiers from events, enforce caps, and distribute overflow points.
    - key_attribute can have a max cap of 5.
    - All other attributes have a max cap of 4.
    - Ensure every attribute has at least 1 point.
    """
    # Step 1: Initialize attributes and sum event modifiers
    aggregated_attributes = {attribute: 0 for attribute in attributes}

    for stage in events.values():  # Sum all attributes from events
        for attribute, value in stage["attributes"].items():
            aggregated_attributes[attribute] += value

    # Step 2: Ensure all attributes have at least 1 point
    for attribute in attributes:
        if aggregated_attributes[attribute] < 1:
            aggregated_attributes[attribute] = 1

    # Step 3: Calculate overflow points and enforce caps
    overflow_pool = 0
    for attribute, value in aggregated_attributes.items():
        max_cap = 5 if attribute == key_attribute else 4
        if value > max_cap:
            overflow_pool += value - max_cap
            aggregated_attributes[attribute] = max_cap

    # Step 4: Distribute remaining points (including the overflow pool)
    remaining_points = total_points - sum(aggregated_attributes.values()) + overflow_pool

    while remaining_points > 0:
        eligible_attributes = [
            attr for attr, val in aggregated_attributes.items()
            if (attr == key_attribute and val < 5) or (attr != key_attribute and val < 4)
        ]

        if not eligible_attributes:
            break  # No attributes left to distribute points to

        chosen_attribute = random.choice(eligible_attributes)
        aggregated_attributes[chosen_attribute] += 1
        remaining_points -= 1

    return aggregated_attributes

def get_random_origin(origins_file, events_folder):
    """
    Randomly select an archetype and subclass based on weights.
    Use the event_key to locate and load the corresponding event file.
    Aggregate attributes from the selected events.
    Return the selected archetype, subclass, their details, selected events, and aggregated attributes.
    """
    origins_data = load_json(origins_file)["Origins"]

    # Flatten archetypes into a weighted list
    archetype_choices = [
        {"name": archetype, "weight": data["weight"], "data": data}
        for archetype, data in origins_data.items()
    ]

    # Select a random archetype based on weight
    selected_archetype = weighted_random_choice(archetype_choices)
    archetype_name = selected_archetype["name"]
    archetype_data = selected_archetype["data"]

    # Flatten subclasses into a weighted list
    subclass_choices = [
        {"name": subclass, "weight": data["weight"], "data": data}
        for subclass, data in archetype_data["subclasses"].items()
    ]

    # Select a random subclass based on weight
    selected_subclass = weighted_random_choice(subclass_choices)
    subclass_name = selected_subclass["name"]
    subclass_data = selected_subclass["data"]
    subclass_key_attribute = subclass_data["key_attribute"]

    # Get events using the event_key
    event_key = subclass_data["event_key"]
    selected_events = get_random_event(event_key, events_folder)

    # Aggregate attributes from selected events
    aggregated_attributes = calculate_aggregated_attributes(selected_events, subclass_key_attribute)

    return {
        "archetype": archetype_name,
        "archetype_description": archetype_data["description"],
        "subclass": subclass_name,
        "subclass_description": subclass_data["description"],
        "event_key": event_key,
        "selected_events": selected_events,
        "aggregated_attributes": aggregated_attributes,
        "key_attribute": subclass_key_attribute
    }
