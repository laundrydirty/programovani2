import json
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
    def to_json(self):
        return {"type":"Point", "coordinates": self.coordinates}

        # return '{{"type":"Point","coordinates":{}}}'.format(self.coordinates)

# object (type) -> geometry (coordinates) -> linestring
class LineString(Geometry):
    def __init__(self, type=None, coordinates=None):
        super().__init__("LineString",coordinates)

    def to_json(self):
        return {"type": "LineString", "coordinates": self.coordinates}


# object (type) -> feature (geometry,properties,id)
class Feature(Object):
    def __init__(self,geometry=None,properties=None,id=None):
        super().__init__("Feature")
        # je objekt istanic tridy?
        if not isinstance(geometry, Geometry):
            raise ValueError ("Attempted to insert A non Geometry as a geometry")
        self.geometry = geometry
        if id:
            self.id = id
        self.properties = properties

    def to_json(self):
        return {"type": "Feature", "geometry": self.geometry.to_json(),
                "properties": self.properties}

# object (type) -> featurecollection (features)
class FeatureCollection(Object):
    def __init__(self,features=None):
        super().__init__("FeatureCollection")
        self.features = features

    def to_json(self):
        features = [f.to_json() for f in self.features]
        return {"type": "FeatureCollection", "features": features}


p = Point(10,10)
print(json.dumps(p.to_json()))
f = Feature(p,{"test":"value"})
print(json.dumps(f.to_json()))
print(f.geometry.coordinates)