from pydantic import BaseModel


class Exobiology(BaseModel):
    id: int
    completed: bool
    system_name: str
    body_name: str
    body_subtype: str
    distance_to_arrival: float
    landmark_subtype: str
    value: int
    count: int
    jumps: int


class Riches(BaseModel):
    id: int
    completed: bool
    system_name: str
    body_name: str
    body_subtype: str
    is_terraformable: bool
    distance_to_arrival: float
    estimated_scan_value: int
    estimated_mapping_value: int
    jumps: int
