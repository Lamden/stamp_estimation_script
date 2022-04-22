from contracting.db.driver import Driver
from contracting.db.encoder import encode, decode
import pymongo

class BlockserviceDriver(Driver):
    # conn_str see https://www.mongodb.com/docs/manual/reference/connection-string/
    def __init__(self, conn_str="mongodb://localhost:27017", db='lamden', collection='currentState'):
        self.client = pymongo.MongoClient(conn_str)
        self.db = self.client[db][collection]

    def get(self, item: str):
        v = self.db.find_one({'rawKey': item})
        if v is None:
            return None

        if isinstance(v['value'], dict):
            return decode(encode(v['value']))
        
        if decode(v['value']) is None:
            return v['value']

        return decode(v['value'])

    def set(self, key, value):
        # Do nothing to keep readonly.
        pass

    def iter(self, prefix: str, length=0):
        cur = self.db.find({'rawKey': {'$regex': f'^{prefix}'}})

        keys = []
        for entry in cur:
            keys.append(entry['rawKey'])
            if 0 < length <= len(keys):
                break

        keys.sort()
        return keys

    def keys(self):
        k = []
        for entry in self.db.find({}):
            k.append(entry['rawKey'])
        k.sort()
        return k

    def __delitem__(self, key: str):
        # Do nothing to keep readonly.
        pass
    
    def flush(self):
        # Do nothing to keep readonly.
        pass
