import json
import datetime


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.time):
            return obj.isoformat()
        return super().default(obj)


def obj2pretty_json(obj):
    return json.dumps(obj, cls=DateTimeEncoder, ensure_ascii=False, indent=4)
