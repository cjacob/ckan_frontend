import requests
import pandas as pd
import pprint
#url = "https://datenregister.berlin.de/api/3/action/package_show?id=los_4_2018-berlin"
url = "https://datenregister.berlin.de/api/3/action/package_list?creator_user_id=362f8c11-82e1-4491-8807-aa6fca8716ab"
r = requests.get(url)
data = r.json()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
