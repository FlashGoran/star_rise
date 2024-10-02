origins = {
    "Colonial Progeny": {
        "weight": 4,  # Common category
        "description": "You grew up on the edges of civilization, where danger and opportunity exist side by side.",
        "subclasses": {
            "Terraforming Colonist": {
                "weight": 5,  # More common subclass
                "description": "You grew up on a world still being made habitable, learning to survive in a harsh and often toxic environment.",
                "event_key": "terraforming_colonist_events",
                "bonuses": {
                    "higher_education": {
                        "Technical School": +40,
                        "Space Academy": +10,
                        "Scientist": +10,
                    },
                    "career": {
                        "Engineer": +30,
                        "Scientist": +10,
                        "Pilot": +5,
                        "Survivor": +10
                    }
                }
            },
            "Resistance Operative": {
                "weight": 3,  # Less common subclass
                "description": "Your colony was politically unstable, and you grew up siding with rebel factions fighting against corrupt leadership.",
                "event_key": "resistance_operative_events",
                "bonuses": {
                    "higher_education": {
                        "Criminal Networks": +30,
                        "Military Academy": +10,
                    },
                    "career": {
                        "Corporate agent": +20,
                        "Intelligence Operative": +30,
                        "Marine Corps": +10,
                        "Survivor": +20
                    }
                }
            },
            "Indentured Worker": {
                "weight": 4,
                "description": "Your family was constantly on the move, settling temporary camps and living off the land, avoiding conflicts and danger.",
                "event_key": "indentured_worker_events",
                "bonuses": {
                    "higher_education": {
                        "Space Academy": +10,
                        "Technical School": +5,
                        "Criminal Networks": 0,
                        "Military Academy": -5
                    },
                    "career": {
                        "Pilot": +20,
                        "Survivor": +30,
                        "Engineer": +5,
                        "Scientist": +5
                    }
                }
            },
            "Frontier Enforcer": {
                "weight": 2,  # Less common, more specialized role
                "description": "You were raised in a militarized colony where defending the frontier against raiders, xeno threats, and environmental dangers was your daily reality.",
                "event_key": "frontier_enforcer_events",
                "bonuses": {
                    "higher_education": {
                        "Military Academy": +30,
                        "Space Academy": +10,
                        "Technical School": +5,
                        "Criminal Networks": -10
                    },
                    "career": {
                        "Marine Corps": +40,
                        "Pilot": +10,
                        "Survivor": +20,
                        "Intelligence Operative": +10
                    }
                }
            },
            "Strip Miner": {
                "weight": 5,  # More common role on resource-heavy colonies
                "description": "Your colony was established to exploit natural resources, and you spent your early life in harsh environments extracting minerals, energy, and rare materials.",
                "event_key": "strip_miner_events",
                "bonuses": {
                    "higher_education": {
                        "Technical School": +20,
                        "Space Academy": 0,
                        "Military Academy": +10,
                        "Criminal Networks": -5
                    },
                    "career": {
                        "Engineer": +30,
                        "Marine Corps": +10,
                        "Scientist": +5,
                        "Survivor": +10
                    }
                }
            },
            "Pirate Apprentice": {
                "weight": 1,  # Rare role
                "description": "Your colony was known for harboring pirates, and you grew up learning the ropes of smuggling, raiding, and avoiding the law.",
                "event_key": "pirate_apprentice_events",
                "bonuses": {
                    "higher_education": {
                        "Criminal Networks": +40,
                        "Military Academy": -20,
                        "Technical School": 0,
                        "Space Academy": -10
                    },
                    "career": {
                        "Corporate agent": +10,
                        "Intelligence Operative": +10,
                        "Pilot": +10,
                        "Survivor": +10
                    }
                }
            },
            "Smuggler Kin": {
                "weight": 2,
                "description": "Raised by a smuggler family, you learned how to navigate the black market, move contraband, and evade authorities.",
                "event_key": "smugglers_kin_events",
                "bonuses": {
                    "higher_education": {
                        "Criminal Networks": +40,
                        "Space Academy": +5,
                        "Technical School": 0,
                        "Military Academy": -10
                    },
                    "career": {
                        "Corporate agent": +20,
                        "Intelligence Operative": +20,
                        "Pilot": +15,
                        "Survivor": +10
                    }
                }
            }
        }
    },
    "Militarized Youth": {
        "weight": 3,  # Common for those raised in military settings
        "description": "You were raised in a militarized environment, trained for a future in the armed forces, and prepared for life in service.",
        "subclasses": {
            "Officer’s Legacy": {
                "weight": 4,  # More common among militarized families
                "description": "You come from a family of military officers, groomed from a young age to follow in their footsteps as a leader in the armed forces.",
                "event_key": "officers_legacy_events",
                "bonuses": {
                    "higher_education": {
                        "Military Academy": +30,
                        "Space Academy": +20,
                        "Corporate Indoctrination": +10,
                        "Criminal Networks": -20
                    },
                    "career": {
                        "Marine Corps": +20,
                        "Intelligence Operative": +10,
                        "Pilot": +10,
                        "Corporate agent": 0
                    }
                }
            },
            "Conflict Zone Survivor": {
                "weight": 2,  # Less common, more dangerous background
                "description": "You grew up in a conflict zone, where surviving and learning to fight were a necessity rather than a choice.",
                "event_key": "conflict_zone_survivor_events",
                "bonuses": {
                    "higher_education": {
                        "Military Academy": +30,
                        "Criminal Networks": +10,
                        "Space Academy": 0,
                        "Technical School": 0
                    },
                    "career": {
                        "Marine Corps": +40,
                        "Survivor": +30,
                        "Intelligence Operative": +10,
                        "Corporate agent": 0
                    }
                }
            },
            "Cadet Recruit": {
                "weight": 5,  # Common for those who join military programs early
                "description": "You enlisted as a military cadet from a young age, seeking to escape your harsh upbringing through service.",
                "event_key": "cadet_recruit_events",
                "bonuses": {
                    "higher_education": {
                        "Military Academy": +20,
                        "Technical School": +10,
                        "Space Academy": 0,
                        "Criminal Networks": -10
                    },
                    "career": {
                        "Marine Corps": +30,
                        "Survivor": +10,
                        "Pilot": +10,
                        "Engineer": 0
                    }
                }
            },
            "Revolutionary Youth": {
                "weight": 3,  # Rebel backgrounds are less common
                "description": "You were involved in resistance movements from a young age, learning sabotage, covert operations, and guerilla tactics.",
                "event_key": "revolutionary_youth_events",
                "bonuses": {
                    "higher_education": {
                        "Criminal Networks": +30,
                        "Military Academy": +10,
                        "Corporate Indoctrination": -10,
                        "Space Academy": 0
                    },
                    "career": {
                        "Intelligence Operative": +40,
                        "Corporate agent": +20,
                        "Marine Corps": +10,
                        "Survivor": +10
                    }
                }
            },
            "Garrison-Bred": {
                "weight": 3,  # Common in militarized colonies
                "description": "Raised on a military base or within a militarized zone, you lived a disciplined, structured life surrounded by soldiers and war machines.",
                "event_key": "garrison_bred_events",
                "bonuses": {
                    "higher_education": {
                        "Military Academy": +20,
                        "Space Academy": +10,
                        "Technical School": +5,
                        "Criminal Networks": 0
                    },
                    "career": {
                        "Marine Corps": +30,
                        "Pilot": +20,
                        "Engineer": +10,
                        "Survivor": +10
                    }
                }
            }
        }
    },
    "Corporate Indoctrination": {
        "weight": 3,  # Represents common backgrounds within corporate-controlled environments
        "description": "You were raised within the corporate system, groomed to serve its interests and maintain control in various roles.",
        "subclasses": {
            "Colonial Overseer Trainee": {
                "weight": 4,  # More common
                "description": "You were trained to manage and control colonies on behalf of the corporation, maintaining order and profitability.",
                "event_key": "colonial_overseer_trainee_events",
                "bonuses": {
                    "higher_education": {
                        "Corporate Indoctrination": +30,
                        "Technical School": +10,
                        "Space Academy": 0,
                        "Criminal Networks": -20
                    },
                    "career": {
                        "Corporate agent": +20,
                        "Intelligence Operative": +10,
                        "Engineer": +5,
                        "Scientist": 0
                    }
                }
            },
            "Corporate Enforcer Trainee": {
                "weight": 3,  # Corporate security enforcement is common
                "description": "You were trained to use force and security measures to protect corporate assets and enforce corporate interests.",
                "event_key": "corporate_enforcer_trainee_events",
                "bonuses": {
                    "higher_education": {
                        "Military Academy": +30,
                        "Technical School": +10,
                        "Criminal Networks": 0,
                        "Corporate Indoctrination": +20
                    },
                    "career": {
                        "Marine Corps": +20,
                        "Intelligence Operative": +10,
                        "Survivor": +5,
                        "Pilot": 0
                    }
                }
            },
            "Test Subject": {
                "weight": 2,  # Rare, niche background
                "description": "You were part of corporate experiments, often without full consent, and now possess unique skills or conditions.",
                "event_key": "test_subject_events",
                "bonuses": {
                    "higher_education": {
                        "Corporate Indoctrination": +30,
                        "Technical School": +10,
                        "Medical School": +20,
                        "Criminal Networks": -10
                    },
                    "career": {
                        "Scientist": +30,
                        "Engineer": +10,
                        "Survivor": +20,
                        "Corporate agent": 0
                    }
                }
            },
            "Indoctrination Trainee": {
                "weight": 5,  # Very common role for those raised by corporate ideals
                "description": "You were deeply immersed in corporate philosophy and trained to carry out its will across different sectors.",
                "event_key": "indoctrination_trainee_events",
                "bonuses": {
                    "higher_education": {
                        "Corporate Indoctrination": +50,
                        "Space Academy": +10,
                        "Technical School": +5,
                        "Criminal Networks": -30
                    },
                    "career": {
                        "Corporate agent": +30,
                        "Intelligence Operative": +10,
                        "Scientist": +5,
                        "Engineer": 0
                    }
                }
            },
            "Corporate Operative Trainee": {
                "weight": 3,
                "description": "You were trained to oversee corporate operations, ensuring projects run smoothly and loyalties remain strong.",
                "event_key": "corporate_operative_trainee_events",
                "bonuses": {
                    "higher_education": {
                        "Corporate Indoctrination": +30,
                        "Military Academy": +10,
                        "Space Academy": 0,
                        "Criminal Networks": -10
                    },
                    "career": {
                        "Corporate agent": +20,
                        "Intelligence Operative": +10,
                        "Pilot": 0,
                        "Engineer": 0
                    }
                }
            }
        }
    },
    "Space-born": {
        "weight": 4,  # Space-born is a common background in the void
        "description": "You were raised in space, whether aboard stations, ships, or isolated outposts. Life in the void is all you've ever known.",
        "subclasses": {
            "Orbital Mechanic": {
                "weight": 4,  # Common among those raised in space infrastructure
                "description": "You grew up working with your hands, fixing and maintaining spacecraft and orbital infrastructure.",
                "event_key": "orbital_mechanic_events",
                "bonuses": {
                    "higher_education": {
                        "Technical School": +30,
                        "Space Academy": +15,
                        "Military Academy": +5,
                        "Corporate Indoctrination": +5
                    },
                    "career": {
                        "Engineer": +40,
                        "Pilot": +10,
                        "Survivor": +10,
                        "Scientist": +5
                    }
                }
            },
            "Spacer borne": {
                "weight": 3,  # Less common but key for spacefarer families
                "description": "You were born aboard a spacecraft and lived your entire life among the stars, traveling between far-flung systems.",
                "event_key": "spacers_child_events",
                "bonuses": {
                    "higher_education": {
                        "Space Academy": +40,
                        "Technical School": +15,
                        "Military Academy": +10,
                        "Corporate Indoctrination": +5,
                        "Criminal Networks": +10
                    },
                    "career": {
                        "Pilot": +30,
                        "Survivor": +20,
                        "Scientist": +10,
                        "Engineer": +10
                    }
                }
            },
            "Asteroid Miner Kid": {
                "weight": 4,  # Common among resource-extracting colonies
                "description": "You were raised on the rough edges of asteroid colonies, where your family mined resources and dealt with extreme conditions.",
                "event_key": "asteroid_miner_kid_events",
                "bonuses": {
                    "higher_education": {
                        "Technical School": +35,
                        "Space Academy": +10,
                        "Military Academy": +5,
                        "Corporate Indoctrination": +5
                    },
                    "career": {
                        "Engineer": +30,
                        "Survivor": +20,
                        "Pilot": +10,
                        "Marine Corps": +5
                    }
                }
            },
            "Shipboard Technician": {
                "weight": 3,  # Fairly common for those living aboard ships
                "description": "You spent your formative years as part of a ship's crew, learning to keep its systems running smoothly and efficiently.",
                "event_key": "shipboard_technician_events",
                "bonuses": {
                    "higher_education": {
                        "Technical School": +40,
                        "Space Academy": +15,
                        "Corporate Indoctrination": +10,
                        "Military Academy": +5
                    },
                    "career": {
                        "Engineer": +40,
                        "Pilot": +10,
                        "Survivor": +10,
                        "Scientist": +5
                    }
                }
            },
            "Void Serf": {
                "weight": 5,
                "description": "As a Void Serf, you and your family were tied to the endless corporate-driven cycles of space labor, drifting between mining stations, spaceports, and industrial starships. Often treated as mere cogs in the machine, you were shuffled from one isolated location to another, bound by long-term contracts and rarely allowed to settle. Life in the vast, cold void was your reality, and you became accustomed to harsh conditions, scarce resources, and the unyielding demands of your corporate masters.",
                "event_key": "void_serf_events",
                "bonuses": {
                    "higher_education": {
                        "Space Academy": +5,
                        "Technical School": +5,
                        "Military Academy": +5,
                        "Criminal Networks": +20,
                        "Corporate Indoctrination": +5
                    },
                    "career": {
                        "Pilot": +30,
                        "Survivor": +20,
                        "Corporate agent": +10,
                        "Marine Corps": +5
                    }
                }
            }
        }
    },
    "Urban Upbringing": {
        "weight": 5,  # Common background in densely populated urban environments
        "description": "You grew up in corporate-controlled colony cities or industrial hubs where survival depends on cunning, strength, or loyalty to the system. Whether from the lower streets or the mid-levels of society, you learned to navigate the corporate machine.",
        "subclasses": {
            "Gutter Runner": {
                "weight": 4,  # Lower class, common in colony cities
                "description": "You grew up in the industrial slums of a corporate colony, scavenging and surviving where law and order rarely exist.",
                "event_key": "gutter_runner_events",
                "bonuses": {
                    "higher_education": {
                        "Criminal Networks": +25,
                        "Military Academy": +15,
                        "Technical School": +10,
                        "Corporate Indoctrination": +5
                    },
                    "career": {
                        "Survivor": +30,
                        "Corporate agent": +10,
                        "Pilot": +10,
                        "Marine Corps": +15
                    }
                }
            },
            "Gang Affiliate": {
                "weight": 3,  # Lower class, organized crime affiliation
                "description": "You grew up connected to or part of an urban gang in the colony, surviving and thriving through violence, loyalty, and territorial control.",
                "event_key": "gang_affiliate_events",
                "bonuses": {
                    "higher_education": {
                        "Criminal Networks": +30,
                        "Military Academy": +20,
                        "Corporate Indoctrination": +10,
                        "Technical School": +10
                    },
                    "career": {
                        "Marine Corps": +25,
                        "Intelligence Operative": +20,
                        "Corporate agent": +15,
                        "Survivor": +20
                    }
                }
            },
            "Corporate Drone": {
                "weight": 5,  # Middle class, common among those working for corporations
                "description": "You were raised in a stable corporate job environment, where hard work and loyalty were rewarded with a paycheck and a place in the system.",
                "event_key": "corporate_drone_events",
                "bonuses": {
                    "higher_education": {
                        "Corporate Indoctrination": +30,
                        "Technical School": +20,
                        "Space Academy": +10,
                        "Military Academy": +10
                    },
                    "career": {
                        "Scientist": +25,
                        "Corporate agent": +20,
                        "Engineer": +15,
                        "Pilot": +10
                    }
                }
            },
            "Market Vendor": {
                "weight": 4,  # Middle to lower class, common street vendors or traders
                "description": "You were raised in the bustling markets of the colony, working in trade and learning how to deal with customers and suppliers alike.",
                "event_key": "market_vendor_events",
                "bonuses": {
                    "higher_education": {
                        "Corporate Indoctrination": +20,
                        "Technical School": +15,
                        "Criminal Networks": +15,
                        "Space Academy": +5
                    },
                    "career": {
                        "Corporate agent": +20,
                        "Pilot": +15,
                        "Scientist": +10,
                        "Survivor": +10
                    }
                }
            },
            "Security personel": {
                "weight": 3,  # Martial role, protecting the interests of corporations or urban authorities
                "description": "You were hired muscle or part of the colony security force, ensuring corporate interests were protected in the rough environments of the colony.",
                "event_key": "security_personel_events",
                "bonuses": {
                    "higher_education": {
                        "Military Academy": +30,
                        "Corporate Indoctrination": +15,
                        "Criminal Networks": +5,
                        "Technical School": +5
                    },
                    "career": {
                        "Marine Corps": +40,
                        "Pilot": +10,
                        "Survivor": +20,
                        "Intelligence Operative": +10
                    }
                }
            }
        }
    },
    "Crisis Survivor": {
        "weight": 1,
        "description": "You survived a major catastrophe that drastically shaped your outlook on life and your ability to endure hardship.",
        "subclasses": {
            "Warzone Survivor": {
                "weight": 5,
                "description": "You survived a large-scale war between rival nations or corporations, living through bombings, raids, and relentless fighting.",
                "event_key": "warzone_survivor_events",
                "bonuses": {
                    "higher_education": {
                        "Military Academy": +30,
                        "Technical School": +10,
                        "Criminal Networks": +5,
                        "Corporate Indoctrination": +5
                    },
                    "career": {
                        "Marine Corps": +40,
                        "Pilot": +10,
                        "Engineer": +5,
                        "Intelligence Operative": +10
                    }
                }
            },
            "Pandemic Survivor": {
                "weight": 3,
                "description": "You lived through a widespread and deadly pandemic, learning to survive amidst the collapse of healthcare and society.",
                "event_key": "pandemic_survivor_events",
                "bonuses": {
                    "higher_education": {
                        "Medical School": +40,
                        "Technical School": +10,
                        "Corporate Indoctrination": +5,
                        "Criminal Networks": +5
                    },
                    "career": {
                        "Scientist": +30,
                        "Pilot": +5,
                        "Marine Corps": +5,
                        "Intelligence Operative": +10
                    }
                }
            },
            "Environmental Collapse Refugee": {
                "weight": 4,
                "description": "You escaped the destruction of your home planet or colony due to environmental disaster, learning to adapt in the most hostile environments.",
                "event_key": "environmental_collapse_refugee_events",
                "bonuses": {
                    "higher_education": {
                        "Medical School": +20,
                        "Technical School": +20,
                        "Space Academy": +10,
                        "Corporate Indoctrination": +5,
                        "Criminal Networks": +10
                    },
                    "career": {
                        "Engineer": +20,
                        "Scientist": +10,
                        "Pilot": +5,
                        "Marine Corps": +5
                    }
                }
            },
            "Civil War Refugee": {
                "weight": 3,
                "description": "You fled from a nation or colony ripped apart by civil war, relying on your instincts and cunning to survive.",
                "event_key": "civil_war_refugee_events",
                "bonuses": {
                    "higher_education": {
                        "Military Academy": +30,
                        "Criminal Networks": +30,
                        "Technical School": +5,
                        "Corporate Indoctrination": +5
                    },
                    "career": {
                        "Marine Corps": +30,
                        "Intelligence Operative": +20,
                        "Corporate agent": +10,
                        "Pilot": +5
                    }
                }
            },
            "Rogue AI Rebellion Survivor": {
                "weight": 2,
                "description": "You lived through an uprising led by rogue AI systems.",
                "event_key": "ai_rebellion_survivor_events",
                "bonuses": {
                    "higher_education": {
                        "Technical School": +30,
                        "Space Academy": +20,
                        "Military Academy": +20,
                        "Corporate Indoctrination": +5
                    },
                    "career": {
                        "Engineer": +30,
                        "Scientist": +20,
                        "Intelligence Operative": +10,
                        "Marine Corps": +10
                    }
                }
            },
            "Colony Quarantine Survivor": {
                "weight": 3,
                "description": "You survived a dangerous biohazard or outbreak that led to your colony being quarantined, forcing you to live in isolation.",
                "event_key": "colony_quarantine_survivor_events",
                "bonuses": {
                    "higher_education": {
                        "Medical School": +30,
                        "Technical School": +20,
                        "Space Academy": +10,
                        "Corporate Indoctrination": +5
                    },
                    "career": {
                        "Scientist": +30,
                        "Marine Corps": +10,
                        "Pilot": +5,
                        "Intelligence Operative": +5
                    }
                }
            },
            "Space Station Disaster Survivor": {
                "weight": 3,
                "description": "You were one of the few survivors of a catastrophic event on a space station, such as a reactor failure or collision.",
                "event_key": "space_station_disaster_survivor_events",
                "bonuses": {
                    "higher_education": {
                        "Space Academy": +30,
                        "Technical School": +20,
                        "Military Academy": +10,
                        "Corporate Indoctrination": +5
                    },
                    "career": {
                        "Pilot": +30,
                        "Engineer": +20,
                        "Scientist": +10,
                        "Marine Corps": +5
                    }
                }
            },
            "Xeno Encounter Survivor": {
                "weight": 2,
                "description": "You survived a deadly encounter with alien species or bio-engineered organisms, leaving you scarred but alive.",
                "event_key": "xeno_encounter_survivor_events",
                "bonuses": {
                    "higher_education": {
                        "Military Academy": +30,
                        "Space Academy": +20,
                        "Medical School": +10,
                        "Corporate Indoctrination": +5
                    },
                    "career": {
                        "Marine Corps": +40,
                        "Scientist": +20,
                        "Intelligence Operative": +10,
                        "Pilot": +5
                    }
                }
            }
        }
    }
}

higher_education = {
    "Military Academy": {
        "weight": 3,
        "subclasses": {
            "Fleet Command": [],
            "Tactical Operations": [],
            "Logistics and Strategy": [],
            "Special Forces Training": [],
            "Covert Operations": []
        }
    },
    "Corporate Indoctrination": {
        "weight": 3,
        "subclasses": {
            "Corporate Aristocrat": [],
            "Market Strategist": [],
            "Internal Security": [],
            "Corporate Lawyer": [],
            "PR Specialist": []
        }
    },
    "Technical School": {
        "weight": 4,
        "subclasses": {
            "Starship Engineering": [],
            "Robotics Specialist": [],
            "Advanced AI Systems": [],
            "Weapon Systems Engineer": [],
            "Infrastructure Specialist": []
        }
    },
    "Space Academy": {
        "weight": 3,
        "subclasses": {
            "Astrogator": [],
            "Flight Cadet": [],
            "Combat Pilot": [],
            "Space Exploration": [],
            "Spaceborne Engineer": []
        }
    },
    "University": {
        "weight": 3,
        "subclasses": {
            "Trauma Surgeon": [],
            "Xeno-Biologist": [],
            "Stasis Tech": [],
            "Biotech Specialist": [],
            "Quarantine Specialist": []
        }
    },
    "Criminal Networks": {
        "weight": 4,
        "subclasses": {
            "Smuggler’s Apprentice": [],
            "Info Broker": [],
            "Counterfeiter": [],
            "Gang Enforcer": [],
            "Assassin": []
        }
    }
}

career = {
    "Marine Corps": {
        "weight": 4,
        "subclasses": {
            "Star Trooper": [],
            "Colonial Guard": [],
            "Engineer Forces": [],
            "Fleet Marine": [],
            "Tactical Sniper": []
        }
    },
    "Intelligence Operative": {
        "weight": 3,
        "subclasses": {
            "Field Agent": [],
            "Psychological Warfare Specialist": [],
            "Infiltration Expert": [],
            "Signals Intelligence": [],
            "Counter-Intelligence Operative": []
        }
    },
    "Corporate agent": {
        "weight": 3,
        "subclasses": {
            "Deep Cover Agent": [],
            "Blackmail Specialist": [],
            "Tech Saboteur": [],
            "Asset Extraction Expert": [],
            "Double Agent": []
        }
    },
    "Engineer": {
        "weight": 4,
        "subclasses": {
            "Starship Engineer": [],
            "Colonial Infrastructure Engineer": [],
            "Robotics Engineer": [],
            "Weapons Specialist": [],
            "Terraforming Engineer": []
        }
    },
    "Scientist": {
        "weight": 3,
        "subclasses": {
            "Xeno-Studies Expert": [],
            "Medical Scientist": [],
            "Terraforming Biologist": [],
            "Astrophysicist": [],
            "Cryostasis Specialist": []
        }
    },
    "Pilot": {
        "weight": 4,
        "subclasses": {
            "Commercial Transport Pilot": [],
            "Military Fighter Pilot": [],
            "Exploration Pilot": [],
            "Freighter Captain": [],
            "Smuggler Pilot": []
        }
    },
}
