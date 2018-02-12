# Garrett Thompson
# https://github.com/Gleland

import json
from urllib.request import urlopen
import os

link = "https://blockchain.info/ticker"
raw_data = urlopen(link)
json_data = json.load(raw_data)
price = str(json_data["USD"]["last"])
print("$"+str(price))
