import sys
sys.path.append("E:\Start Python\GEN64")
import json

from Week01.HeadDate import *
Heading("LP06")

from Lp06_fuction import *
persondict = {}
get_info_dict(persondict)
evaluation(persondict)

x = json.dumps(persondict)
print("JSON =",x)