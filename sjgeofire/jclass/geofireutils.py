from jnius import JavaClass, MetaJavaClass, JavaMultipleMethod, JavaStaticMethod

__all__ = ("GeoFireUtils",)


class GeoFireUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = 'com/firebase/geofire/GeoFireUtils'

    getGeoHashForLocation = JavaMultipleMethod([
        (
            '(Lcom/firebase/geofire/GeoLocation;)Ljava/lang/String;',
            True, False
        ),
        (
            '(Lcom/firebase/geofire/GeoLocation;I)Ljava/lang/String;',
            True, False
        )
    ])

    getDistanceBetweens = JavaStaticMethod("(Lcom/firebase/geofire/GeoLocation;Lcom/firebase/geofire/GeoLocation;)D")

    getGeoHashQueryBounds = JavaStaticMethod("(Lcom/firebase/geofire/GeoLocation;D)Ljava/util/List;")
