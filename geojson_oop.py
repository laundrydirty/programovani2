import json
# geojson structure


# object (type)
class Object(object):
    def __init__(self, type=None):
        self.type = type

    def to_json(self):
        return {"type":self.type}

# object (type) -> geometry (coordinates)
class Geometry(Object):
    def __init__(self,type=None,coordinates=None):
        super(). __init__(type)
        self.coordinates=coordinates

    def to_json(self):
        dict=super().to_json()
        dict["coordinates"] = self.coordinates
        return dict

# object (type) -> geometry (coordinates) -> point
class Point(Geometry):
    def __init__(self, x,y,z=None):
        if z is not None:
            super().__init__("Point",[x,y,z])
        else:
            super().__init__("Point", [x, y])


# object (type) -> geometry (coordinates) -> linestring
class LineString(Geometry):
    def __init__(self, coordinates=None):
        super().__init__("LineString",coordinates)


# object (type) -> feature (geometry,properties,id)
class Feature(Object):
    @classmethod
    def from_json(cls,adict):
        properties = adict["properties"]
        geometry=Geometry.from_json(adict["geometry"])

        feature_objs = []
        for fdict in adict ["features"]:
            fobj=Feature.from_json(fdict)
            feature_objs.append(fobj)

        obj=cls(geometry,properties) #ekvivalentni FeatureCollection(feature_objs)
        return obj



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
        dict=super().to_json()
        dict["geometry"] = self.geometry.to_json()
        dict["properties"]= self.properties
        return dict

# object (type) -> featurecollection (features)
class FeatureCollection(Object):
    @classmethod
    def from_json(cls,adict):
        feature_objs = []
        for fdict in adict ["features"]:
            fobj=Feature.from_json(fdict)
            feature_objs.append(fobj)
        obj=cls(feature_objs) #ekvivalentni FeatureCollection(feature_objs)
        return obj

    def __init__(self,features=None):
        super().__init__("FeatureCollection")
        self.features = features

    def to_json(self):
        dict=super().to_json()
        dict["features"] = self.features.to_json()
        return dict


p = Point(10,10)
print(json.dumps(p.to_json()))
f = Feature(p,{"test":"value"})
print(json.dumps(f.to_json()))
print(f.geometry.coordinates)


def form_json(adict):
    if adict["type"] == "FeatureCollection":
        FeatureCollection.from_json(addict)
    elif adict["type"] == "Feature":
        Feature.from_json(addict)
    elif adict["type"] == "Point":
       Point.from_json(addict)
    else:
        print("Unknown type {}".format(adict["type"]))

    #zjisti co je to zac
    #vytvori objektovou hierchii
    #vrati korenovy element {feature/featurecollection/geometery)

with open("mpp.json") as f:
    adict=json.load(f)
    print(adict)
