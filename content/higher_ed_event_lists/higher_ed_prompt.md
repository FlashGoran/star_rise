Main Purpose:
to create events in a backstory during a characters adult education in a grimdark, corporate dystopia, alienesque without aliens or other copywrited material. so theme is mainly the one in alien or aliens but a parallell dimenzion that dont use copywrited material.

details of Theme and Setting:
sci-fi Grimdark corporate dystopia
political cutthrought environment with extreme profit oriented megacorp agendas intermixed in nation interests.
nations and factions in delicate interactions going from mutual interests, cold war, and to warm war.
Settings varies from megacities, large colonies, outback rimworlds, etc but mainly prospecting in frontiers (without the xeno from the movie or anything else copywrited)
Ethical and moral dilemmas in mixed technology settings as budget cuts for profits are a huge driver.

Events & Output Structure:
    Create 10 events “success” or 10 “failure.” events depending on whats asked. be creative with the event creation details.- 
Success vs. Failure
    Success Events:
        Depict moments of victory, personal achievement, or clever problem-solving.
        Show how the character’s skills or decisions led to these successes.
    Failure Events:
        Focus on errors, miscalculations, or external forces leading to defeat or setback.
        These failures should still foster character growth, reflection, or open new narrative paths.

In each event, include 5 skill weights (values 1–5):
  3 primary skills relevant to the subclass, typically weighted 3–5. Each subclass comes with a main_attr that is associated to some primary skills.
  Consult the subclass name/description to decide which skills are also relevant and reasonable.
  2 additional/secondary skills with lower weights, usually 1–3. These skills could be less or semi relevant and to some degree relevant only the the event itself that would benefit the characters background.
Example: for combat oriented characters who are based on str then close combat is a skill under strenght and is relevant. but ranged combat that is a part of agi is also higly relevant of course.
engineers based on str will also have example piloting and science as relevant as could be a interesting event.
on the other hand:
A heavy machinery operator might occasionally receive Science such as Quantum Mechanics if the event justifies it, but that should remain rare (10% off-topic).

Sample Skill Block:
"skills": {
  "Close Combat": 4,
  "Stamina": 5,
  "Ranged Combat": 3,
  "ComTech": 2,
  "Manipulation": 1
}

Event Descriptions and Purpose
Write intricate synopses (e.g., 5 sentences) that feel like pivotal moments, chapter highlights, or dramatic scenes in a story.
Each event should showcase a key milestone in the character’s journey, be creative. preferably the events should be from character pov and oriented around the character, side characters in events should be usable storypoints or not mentioned.

Output to be in JSON-Like Output Structure. Return the events in two categories, success and failure, example:
{
  "success": [
    {
      "description": "A short but intricate narrative highlighting a major success or growth moment.",
      "skills": {
        "SkillName1": Weight,
        "SkillName2": Weight,
        "...": ...
      }
    },
    ...
  ],
  "failure": [
    {
      "description": "A short but intricate narrative highlighting a major setback or failure.",
      "skills": {
        "SkillName1": Weight,
        "SkillName2": Weight,
        "...": ...
      }
    },
    ...
  ]
}


Tone and Narrative Hooks

Infuse each event with cinematic or literary flair, ensuring they can serve as story seeds or dramatic backstory elements.
Keep the overall tone consistent with the chosen theme (e.g., gritty, horrific, morally complex).
the events should be framed to the character who can be any gender, race etc etc.
avoid exotic sci fi such as magic, warp, aliens, etc. but put the alienesque them from fox media alien but do not use copywrited material. 

Attributes and Skills Reference, due note that parentesis does not contains skills but clarifications to the usage of the skill:
Strength:
  Close Combat (example ingame usage that is a part of the skill: Blunt, Edge, Special, Explosives)
  Heavy Machinery (example ingame usage that is a part of the skill: Propulsion, Industrial, Structural Eng., Power Sys. Enviromental Sys., Weapon Sys.)
  Stamina (example ingame usage that is a part of the skill: Psychological Res., Hazardous Env., Extreme Env., First Aid, Survival)

Agility:
  Mobility (example ingame usage that is a part of the skill: Athletics, Stealth Movement, Dexterity, Zero-G Movement)
  Piloting (example ingame usage that is a part of the skill: Land, Air, Water, Space, Navigation, Remote Control)
  Ranged Combat (example ingame usage that is a part of the skill: CQB Weapons, Automatic Weapons, Energy Weapons, High-Tech Armament, Cyber-Integrated Arms, Precision Weapons)

Intelligence:
  ComTech (example ingame usage that is a part of the skill: Computer Eng., Signal Intelligence, Electronics Eng., Robotics, AI Tech)
  Science (example ingame usage that is a part of the skill: Astrogation, Linguistics, Biology, Chemistry, Cybernetics, Xenology, Psycology, Physics, Economics, Medical Science, Environmental Science, Nanotechnology, Quantum Mechanics, Advanced Engineering)

Wisdom:
  Command (example ingame usage that is a part of the skill: Leadership, Tactical Operations, Strategic Planning, Crisis Management, Operational Planning)
  Manipulation (example ingame usage that is a part of the skill: PsyOps, Negotiator, Interrogation, Public Relations, Social Engineering, Forgery)
  Observation (example ingame usage that is a part of the skill: Systems Analytics, Sensors, Forensics, Tactical Analytics, Strategic Analytics)

please create the json list for 10  success events for:
    "Space Academy": {
      "description": "Training for navigation, piloting, and ship operations.",
      "event_list": "space_academy_events",
      "subclasses": {
        "Navigation Training": {
          "description": "Specializes in stellar navigation and course plotting.",
          "main_attr": "int",