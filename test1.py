import argparse
import meraki
import json
import os
import sys
import urllib.parse
from pprint import pprint
from datetime import datetime
from key import MERAKI_API_KEY

dashboard = meraki.DashboardAPI(
        MERAKI_API_KEY,
        print_console=True,
        output_log=False,
    )

def get_org_id(org):
    orgs = dashboard.organizations.getOrganizations(org)
    org_id = orgs[0]['id']
    return org_id

def get_network_id(network, org_id):
    networks = dashboard.organizations.getOrganizationNetworks(org_id, name=network)
    network_id = networks[0]['id']
    return network_id

def main(org_name, network_name):
    org_id = get_org_id(org_name)
    network_id = get_network_id(network_name, org_id)

    topology = dashboard.networks.getNetworkTopologyLinkLayer(networkId=network_id)
    pprint(topology)
    wan_stats = dashboard.appliance.getOrganizationApplianceUplinkStatuses(organizationId=org_id, networkId=network_id)
    pprint(wan_stats)
    
       

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a CSV file of current topology for a specific network.')
    parser.add_argument('-org', help='Organization name to get the network from.')
    parser.add_argument('-network', help='Network you want the topology of.')
    args = parser.parse_args()
    print("About to gather network: " + args.network + "'s topology.")
    

    start_time = datetime.now()
    main(args.org, args.network)
    end_time = datetime.now()
    print(f'\nScript complete, total runtime {end_time - start_time}')