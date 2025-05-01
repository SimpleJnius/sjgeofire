from jnius import PythonJavaClass, java_method

__all__ = ("LocationCallback",)


class LocationCallback(PythonJavaClass):
    __javainterfaces__ = ["com/firebase/geofire/util/GeoFire"]
    __javacontext__ = "app"

    def __init__(self, on_location_result, on_cancelled):
        self.on_location_result = on_location_result
        self.on_cancelled = on_cancelled

    @java_method("(Ljava/lang/String;Lcom/firebase/geofire/GeoLocation;)V")
    def onLocationResult(self, key, location):
        self.on_location_result(key, location)

    @java_method("(Lcom/google/firebase/database/DatabaseError;)V")
    def onCancelled(self, error):
        self.on_cancelled(error)
