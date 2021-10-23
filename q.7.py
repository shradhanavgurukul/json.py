# # Text file data ko json file data mai convert karo,jaise ki neeche diya hai?

import json
a={"Name":"Abhishek","Designation":"CEO of navgurukul","Age":6}
y=json.dumps(a)
file=open("name.json","w")
json.dump(a,file)