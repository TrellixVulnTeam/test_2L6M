import hashlib
import base64
event_id = "LIMCMeasurementEvent"
event_time = "2021-03-02T23:01:00.633765+0900"
#event_time = "2021-03-02T14:01:00.633765+0000"

#r = hashlib.md5((event_id + "" + event_time).encode()).digest()
r = hashlib.md5((event_id + "_" + event_time + "___").encode()).digest()
print(r)

r2 = base64.b64encode(r)

print(r2)
