from urllib import request

from google.transit import gtfs_realtime_pb2

import config


def get_jz_feed():
    return __call_gtfs('/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz')


def __call_gtfs(endpoint: str):
    feed = gtfs_realtime_pb2.FeedMessage()
    req = request.Request(
        f'https://api-endpoint.mta.info{endpoint}',
        headers={
            'x-api-key': config.Config.MTA_API_KEY,
        }
    )
    response = request.urlopen(req)
    feed.ParseFromString(response.read())
    return feed
