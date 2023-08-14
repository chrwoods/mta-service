from typing import Dict

from app.mta.models.gtfs import Stop


STOPS_CACHE: Dict[str, Stop] = {}


def load_stops() -> Dict[str, Stop]:
    global STOPS_CACHE
    if STOPS_CACHE:
        return STOPS_CACHE

    stops = {}
    with open('app/mta/models/constants/gtfs/stops.txt') as stops_file:
        # skip first line of header text
        stops_file.readline()
        for raw_stop in stops_file.readlines():
            stop = Stop.from_csv(raw_stop)
            stops[stop.id] = stop

    STOPS_CACHE = stops
    return STOPS_CACHE
