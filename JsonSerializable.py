import json


class JsonSerializable:
    """Base class to provide JSON serialization and deserialization methods."""

    def toJSON(self):
        """Convert the object to a JSON string."""
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @classmethod
    def fromJSON(cls, json_data):
        """Create an object from JSON data."""
        return cls(**json_data)
