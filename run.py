#!/usr/bin/python3

from kavenegar import APIException
import shodan
import os

KEY = ""

api = shodan.Shodan(KEY)

host = api.host("")

print("ip address: {}".format(host['ip_str']))

print("org: {}".format(host['org']))

print("os: {}".format(host['os']))

for item in host['data']:
    print(item['port'])
    print("country: {}".format(item['location']['country_name']))
    print("country code: {}".format(item['location']['country_code']))
    print("city: {}".format(item['location']['city']))
    print("region code: {}".format(item['location']['region_code']))
    print("latitude: {}".format(item['location']['latitude']))
    print("longitude: {}".format(item['location']['longitude']))
    print(item['location'])