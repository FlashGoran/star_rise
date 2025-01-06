from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Cluster:
    name: str
    type: str  # e.g., "Core", "Mid", "Rim"
    position: List[float]  # [x, y, z] in galactic space
    systems: List[StarSystem] = field(default_factory=list)
    key_features: List[str] = field(default_factory=list)  # e.g., "Nebula", "Dark Matter Field"
    controlling_entities: List[str] = field(default_factory=list)  # e.g., nation/corp IDs

@dataclass
class StarSystem:
    name: str
    coordinates: List[float]  # [x, y, z] within the cluster
    star_type: str  # e.g., "Main Sequence", "Red Dwarf", "White Dwarf"
    planets: int  # Number of planets in the system
    celestial_bodies: List[str] = field(default_factory=list)  # e.g., "Asteroid Belt", "Comet Cluster"
    resources: List[str] = field(default_factory=list)  # e.g., "Rare Metals", "Helium-3"
    controlling_entities: List[str] = field(default_factory=list)  # e.g., nation/corp IDs
    special_features: List[str] = field(default_factory=list)  # e.g., "Strategic Hub", "FTL Anomaly"

@dataclass
class Planet:
    name: str
    type: str  # e.g., "Terrestrial", "Gas Giant"
    atmosphere: Optional[str] = None  # e.g., "Breathable", "Toxic"
    resources: List[str] = field(default_factory=list)  # e.g., "Titanium", "Water Ice"
    population: Optional[int] = None  # Population, if colonized
    controlling_entities: List[str] = field(default_factory=list)  # e.g., nation/corp IDs
    special_features: List[str] = field(default_factory=list)  # e.g., "Research Station", "Military Base"
