import hashlib
import base64

event_id = ""
event_time = ""

r = hashlib.md5((event_id + "_" + event_time + "___").encode()).digest()
print(r)

r2 = base64.b64encode(r)
print(r2)
