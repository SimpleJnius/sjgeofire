from jnius import PythonJavaClass, java_method

__all__ = ("GeoQueryEventListener",)


class GeoQueryEventListener(PythonJavaClass):
    __javainterfaces__ = ["com/firebase/geofire/GeoQueryEventListener"]
    __javacontext__ = "app"

    def __init__(self, callback: dict):
        self.callback = callback

    def _callback(self, name, *args):
        func = self.callback.get(name)
        if func:
            return func(*args)

    @java_method("(Ljava/lang/String;Lcom/firebase/geofire/GeoLocation;)V")
    def onKeyEntered(self, key, location):
        self._callback("on_key_entered", key, location)

    @java_method("(Ljava/lang/String;)V")
    def onKeyExited(self, key):
        self._callback("on_key_exited", key)

    @java_method("(Ljava/lang/String;Lcom/firebase/geofire/GeoLocation;)V")
    def onKeyMoved(self, key, location):
        self._callback("on_data_moved", key, location)

    @java_method("()V")
    def onGeoQueryReady(self):
        self._callback("on_geoquery_ready")

    @java_method("(Lcom/google/firebase/database/DatabaseError;)V")
    def onGeoQuerryError(self, error):
        self._callback("on_geo_query_error", error)
