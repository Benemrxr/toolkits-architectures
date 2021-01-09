import io
import numpy as np


def serializer(data):
    memfile = io.BytesIO()
    np.save(memfile, data)
    memfile.seek(0)
    serialized = memfile.read()

    return serialized

def deserializer(data):
    memfile = io.BytesIO()
    memfile.write(data)
    memfile.seek(0)
    deserialized = np.load(memfile)

    return deserialized