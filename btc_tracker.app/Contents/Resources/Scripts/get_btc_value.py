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
#os.system('osascript btc.app {}'.format(price))
# os.system('open ./btc.app --args {}'.format(price))
#os.system("""osascript -e 'display notification {} with title "BTC Tracker"subtitle (current date) as string'""".format(price,"btc.icns"))
#os.system('open -e btc.app {}'.format(price))


#os.system('osascript -e "display dialog {} with title {} with icon POSIX file {}"'.format(price,"BTC Tracker","BTC.png"))
