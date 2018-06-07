#!/usr//bin/env python

'''

Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

'''

__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"
from python_client.api.network_device_api import NetworkDeviceApi
from python_client.api.misc_api import MiscApi
from python_client.configuration import Configuration
from python_client.api_client import ApiClient
from python_client.models.generate_token_request import GenerateTokenRequest
import json
import argparse
import socket
import getpass
import urllib3

# Quick check if the entered ip address is a valid one
def valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def main():

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['network'], type=str,
                        help='command = "network" for retrieving network count ' \
                             'and a list of network devices')
    parser.add_argument('-i', '--ipaddress', type=str, help='DNA Center cluster ip address')
    parser.add_argument('-u', '--uname', type=str, default='admin', help='DNA Center login username')
    args = parser.parse_args()

    if valid_ip(args.ipaddress) == False:
        print ('You need to provide a valid ipaddress')
        sys.exit('Invalid ipaddress')
    if args.uname == '':
        print ('You need to provide a valid DNAC login username')
        sys.exit('Invalid username')

    # Prompt for password
    dnacPwd = getpass.getpass(
        "\nPlease enter the DNA Center \'{}\' user password for the {} cluster : ".format(args.uname,
                                                                                              args.ipaddress))
    #Set up configuration
    config = Configuration()
    config.host = args.ipaddress
    config.username = args.uname
    config.password = dnacPwd
    config.verify_ssl = False
    config.debug = False

    #Get Basic Auth of credentials
    config.api_key = config.get_basic_auth_token()
    #Create client by passing the config params
    apic = ApiClient(configuration=config, header_name = 'Authorization', header_value = config.api_key)
    #Get the auth token
    tokenRequest = GenerateTokenRequest()
    auth_instance = MiscApi(apic)
    auth_response = auth_instance.post_auth_token(request=tokenRequest,authorization=config.api_key)
    token = auth_response.token
    # Set X-AUTH-TOKEN
    apic.set_default_header("X-AUTH-TOKEN",token)

    # Call the APIs
    api_instance = NetworkDeviceApi(apic)
    print("\nGetting device count\n")
    count_response = api_instance.get_network_device_count()
    print(count_response.response)
    print("\n")
    print("Getting devices\n")
    template = '{:<20} {:<25} {:<6}'
    table_headers = ['PlatformId', 'Hostname', 'Serial']
    table_ul = ['--------', '----------', '------']
    dev_response = api_instance.get_network_device()
    print(template.format(*table_headers))
    print(template.format(*table_ul))
    for dev in dev_response.response:
        dev_dict = dev.to_dict()
        print(template.format(dev_dict["platform_id"],dev_dict["hostname"],dev_dict["serial_number"]))
    print("\n")



if __name__ == '__main__':
    main()
