from jnius import JavaClass, MetaJavaClass, JavaMultipleMethod, JavaStaticMethod, JavaMethod

__all__ = ("GeoFire",)


class GeoFire(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = 'com/firebase/geofire/GeoFire'
    __javaconstructor__ = [("(Lcom/google/firebase/database/DatabaseReference;)V", False)]

    getLocationValue = JavaStaticMethod(
        "(Lcom/google/firebase/database/DataSnapshot;)"
        "Lcom/firebase/geofire/GeoLocation;"
    )

    getDatabaseReference = JavaMethod(
        "()Lcom/google/firebase/database/DatabaseReference;"
    )

    getDatabaseRefForKey = JavaMethod(
        "(Ljava/lang/String;)"
        "Lcom/google/firebase/database/DatabaseReference;"
    )

    setLocation = JavaMultipleMethod([
        (
            "(Ljava/lang/String;Lcom/firebase/geofire/GeoLocation;)V",
            False, False
        ),
        (
            "(Ljava/lang/String;Lcom/firebase/geofire/GeoLocation;"
            "Lcom/firebase/geofire/GeoFire$CompletionListener;)V",
            False, False
        )
    ])

    removeLocation = JavaMultipleMethod([
        (
            "(Ljava/lang/String;)V",
            False, False
        ),
        (
            "(Ljava/lang/String;Lcom/firebase/geofire/GeoFire$CompletionListener;)V",
            False, False
        )
    ])

    getLocation = JavaMethod(
        "(Ljava/lang/String;Lcom/firebase/geofire/LocationCallback;)V"
    )

    queryAtLocation = JavaMethod(
        "(Lcom/firebase/geofire/GeoLocation;D)Lcom/firebase/geofire/GeoQuery;"
    )

    raiseEvent = JavaMethod("(Ljava/lang/Runnable;)V")
