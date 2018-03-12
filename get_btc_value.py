# Garrett Thompson
# https://github.com/Gleland/btc_tracker

import json
from urllib.request import urlopen

link = "https://blockchain.info/ticker"
raw_data = urlopen(link)
json_data = json.load(raw_data)
price = str(json_data["USD"]["last"])
print("$"+price)
