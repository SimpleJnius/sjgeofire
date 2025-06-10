from typing import Union

from sjfirebase.tools.mixin import DatabaseMixin
from sjgeofire.jclass.geofire import GeoFire
from sjgeofire.jclass.geolocation import GeoLocation
from sjgeofire.jinterface.geoquerydata import GeoQueryDataEventListener
from sjgeofire.tools.serialize import serialize


class GeofireMixin:
    geofire_listeners = {}
    geo_queries = {}

    @staticmethod
    def __process_data_snapshot(snapshot):
        if (data := snapshot.getValue()) is None:
            return None
        if not isinstance(serialized_data := serialize(data), dict):
            return serialized_data
        return {"key": snapshot.getKey(), **serialized_data}

    def __process_listener(self, snapshot, location, listener):
        if not listener:
            return
        if snapshot:
            snapshot = self.__process_data_snapshot(snapshot)
        if location:
            location = location.latitude, location.longitude
        listener(snapshot, location)

    def __construct_geo_query_data_event_listener(self, listener):
        callback = GeoQueryDataEventListener(
            {
                "on_data_entered": lambda snapshot, location: self.__process_listener(
                    snapshot, location, listener.get("on_data_entered")
                ),
                "on_data_exited": lambda snapshot: self.__process_listener(
                    snapshot, None, listener.get("on_data_exited")
                ),
                "on_data_moved": lambda snapshot, location: self.__process_listener(
                    snapshot, location, listener.get("on_data_moved")
                ),
                "on_data_changed": lambda snapshot, location: self.__process_listener(
                    snapshot, location, listener.get("on_data_changed")
                ),
                "on_geo_query_ready": lambda:
                    None if not (ready_listener := listener.get("on_geo_query_ready"))
                    else ready_listener(),
                "on_geo_query_error": lambda error:
                    None if not (error_listener := listener.get("on_geo_query_error"))
                    else error_listener(error.getMessage())
            }
        )
        return callback

    def add_geo_query_data_event_listener(
            self, rtdb_path: str,
            listener_key: str,
            coordinates: Union[tuple[float, float], list[float, float]],
            radius: float,
            callback: dict
    ):
        ref = DatabaseMixin().get_reference(rtdb_path)
        geoquery = GeoFire(ref).queryAtLocation(GeoLocation(*coordinates), radius)
        listener = self.__construct_geo_query_data_event_listener(callback)
        geoquery.addGeoQueryDataEventListener(listener)
        self.geofire_listeners[listener_key] = listener
        self.geo_queries[listener_key] = geoquery

    def remove_geo_query_event_listener(self, listener_key: str):
        listener = self.geofire_listeners.pop(listener_key)
        geo_query = self.geo_queries.pop(listener_key)
        geo_query.removeGeoQueryEventListener(listener)

