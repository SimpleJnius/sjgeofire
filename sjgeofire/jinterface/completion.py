from jnius import PythonJavaClass, java_method

__all__ = ("CompletionListener",)


class CompletionListener(PythonJavaClass):
    __javainterfaces__ = ["com/firebase/geofire/GeoFire$CompletionListener"]
    __javacontext__ = "app"

    def __init__(self, on_complete):
        self.callback = on_complete

    @java_method("(Ljava/lang/String;Lcom/google/firebase/database/DatabaseError;)V")
    def onComplete(self, key, error):
        self.callback(key, error)
