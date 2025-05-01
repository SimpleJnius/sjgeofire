from jnius import JavaClass, MetaJavaClass, JavaField, JavaStaticMethod, JavaMethod

__all__ = ("GeoLocation",)


class GeoLocation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = 'com/firebase/geofire/GeoLocation'
    __javaconstructor__ = [("(DD)V", False)]

    latitude = JavaField("D")
    longitude = JavaField("D")
    coordinatesValid = JavaStaticMethod("(DD)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
