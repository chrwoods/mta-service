import collections
from datetime import datetime
from zoneinfo import ZoneInfo

from app.mta.external import gtfs_api
from app.mta.services import gtfs_service


def get_southbound_jz_stop_times() -> dict:
    stops = gtfs_service.load_stops()
    feed = gtfs_api.get_jz_feed()

    found_stop_times = collections.defaultdict(list)
    for entity in feed.entity:
        if entity.HasField('trip_update'):
            trip = entity.trip_update.trip

            # skip unimportant routes
            if 'J..S' not in trip.trip_id:
                continue

            for stop_time in entity.trip_update.stop_time_update:
                stop = stops[stop_time.stop_id]
                arrival_time = datetime.fromtimestamp(stop_time.arrival.time, tz=ZoneInfo('US/Eastern'))
                departure_time = datetime.fromtimestamp(stop_time.departure.time, tz=ZoneInfo('US/Eastern'))

                stop_time = {
                    'stop_id': stop.id,
                    'stop_name': stop.name,
                    'arrival_time': arrival_time,
                    'departure_time': departure_time,
                }
                found_stop_times[stop.id].append(stop_time)

    return found_stop_times
