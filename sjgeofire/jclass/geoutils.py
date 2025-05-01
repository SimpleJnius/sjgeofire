from jnius import JavaClass, MetaJavaClass, JavaMultipleMethod, JavaStaticMethod

__all__ = ("GeoUtils",)


class GeoUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = 'com/firebase/geofire/util/GeoUtils'

    distance = JavaMultipleMethod([
        (
            '(Lcom/firebase/geofire/GeoLocation;'
            'Lcom/firebase/geofire/GeoLocation;)D;',
            True, False
        ),
        (
            '(DDDD)D',
            True, False
        )
    ])

    distanceToLatitudeDegrees = JavaMultipleMethod("(D)D")

    distanceToLongitudeDegrees = JavaMultipleMethod("(DD)D")

    wrapLongitude = JavaStaticMethod("(D)D")

    capRadius = JavaStaticMethod("(D)D")
