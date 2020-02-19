# geojson structure

# object (type)
class Object(object):
    def __init__(self, type=None):
        self.type = type

# object (type) -> geometry (coordinates)
class Geometry(Object):
    def __init__(self,type=None,coordinates=None):
        super(). __init__(type)
        self.coordinates=coordinates

# object (type) -> geometry (coordinates) -> point
class Point(Geometry):
    def __init__(self, x,y,z=None):
        if z is not None:
            super().__init__("Point",[x,y,z])
        else:
            super().__init__("Point", [x, y])

# object (type) -> geometry (coordinates) -> linestring
class LineString(Geometry):
    def __init__(self, type=None, coordinates=None):
        super().__init__(type,coordinates)


# object (type) -> feature (geometry,properties,id)
class Feature(Object):
    def __init__(self,geometry=None,properties=None,id=None):
        super().__init__("Feature")
        # je objekt istanic tridy?
        if not isinstance(geometry, Geometry):
            raise ValueError ("Attempted to insert A non Geometry as a geometry")
        self.geometry = geometry
        self.properties = properties
        self.id = id


# object (type) -> featurecollection (features)
class FeatureCollection(Object):
    def __init__(self,type=None,features=None):
        super().__init__(type)
        self.features = features

p=Point(10,10)