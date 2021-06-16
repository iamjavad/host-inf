#!/usr/bin/python3

from kavenegar import APIException
import shodan
import os

KEY = "NDciAIz4884Y2EaFjDVzBmHMXer4sTbC"

api = shodan.Shodan(KEY)

host = api.host("185.190.39.234")

print(host['ip_str'])

print(host['org'])

print(host['os'])

for item in host['data']:
    print(item['port'])
    print(item['location']['city'])