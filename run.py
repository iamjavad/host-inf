#!/usr/bin/python3

import shodan
import os
import json
from banner import banner

KEY = "NDciAIz4884Y2EaFjDVzBmHMXer4sTbC"

api = shodan.Shodan(KEY)

host = api.host("185.202.113.3")

os.system("clear")

banner()

print("ip address: {}".format(host['ip_str']))

print("org: {}".format(host['org']))

print("os: {}".format(host['os']))

print("asn: {}".format(host['asn']))

for item in host['data']:
    print(item['port'])
    print("country: {}".format(item['location']['country_name']))
    print("country code: {}".format(item['location']['country_code']))
    print("city: {}".format(item['location']['city']))
    print("region code: {}".format(item['location']['region_code']))
    print("latitude: {}".format(item['location']['latitude']))
    print("longitude: {}".format(item['location']['longitude']))
    #print(item['location'])

#print(json.dumps(host, indent=2))