from app.mta import mta
from app.mta.orchestrators import gtfs_orchestrator


@mta.route('/')
def index():
    return '🚆'


@mta.route('/jz/southbound_stops')
def get_jz_southbound_stops():
    results = gtfs_orchestrator.get_southbound_jz_stop_times()
    return {
        'result': results
    }
