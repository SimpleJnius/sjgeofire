from jnius import PythonJavaClass, java_method

__all__ = ("GeoQueryDataEventListener",)


class GeoQueryDataEventListener(PythonJavaClass):
    __javainterfaces__ = ["com/firebase/geofire/GeoQueryDataEventListener"]
    __javacontext__ = "app"

    def __init__(self, callback: dict):
        self.callback = callback

    def _callback(self, name, *args):
        func = self.callback.get(name)
        if func:
            return func(*args)

    @java_method("(Lcom/google/firebase/database/DataSnapshot;Lcom/firebase/geofire/GeoLocation;)V")
    def onDataEntered(self, snapshot, location):
        self._callback("on_data_entered", snapshot, location)

    @java_method("(Lcom/google/firebase/database/DataSnapshot;)V")
    def onDataExited(self, snapshot):
        self._callback("on_data_exited", snapshot)

    @java_method("(Lcom/google/firebase/database/DataSnapshot;Lcom/firebase/geofire/GeoLocation;)V")
    def onDataMoved(self, snapshot, location):
        self._callback("on_data_moved", snapshot, location)

    @java_method("(Lcom/google/firebase/database/DataSnapshot;Lcom/firebase/geofire/GeoLocation;)V")
    def onDataChanged(self, snapshot, location):
        self._callback("on_data_changed", snapshot, location)

    @java_method("()V")
    def onGeoQueryReady(self):
        self._callback("on_geo_query_ready")

    @java_method("(Lcom/google/firebase/database/DatabaseError;)V")
    def onGeoQuerryError(self, error):
        self._callback("on_geo_query_error", error)
