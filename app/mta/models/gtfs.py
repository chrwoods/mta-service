from dataclasses import dataclass


@dataclass
class Stop:
    id: str
    code: str
    name: str
    description: str
    latitude: float
    longitude: float
    zone_id: str
    url: str
    location_type: int
    parent_station: str

    @staticmethod
    def from_csv(raw_line):
        return Stop(*raw_line.strip().split(','))
