import argparse
import meraki
import json
import os
import urllib.parse
from pprint import pprint
from datetime import datetime
from key import MERAKI_API_KEY

dashboard = meraki.DashboardAPI(
    MERAKI_API_KEY,
    output_log=False
    )


parser = argparse.ArgumentParser(description='Generate a CSV file of current topology for a specific network.')
parser.add_argument('-org', help='Organization name to get the network from.')
parser.add_argument('-network', help='Network you want the topology of.')
args = parser.parse_args()
orgs = dashboard.organizations.getOrganizations("Devnet Sandbox")
org_id = orgs[0]['id']


networks = dashboard.organizations.getOrganizationNetworks(org_id, name="CCNP")
network_id = networks[0]['id']
print(network_id)


topology = dashboard.networks.getNetworkTopologyLinkLayer(network_id)
wan_stats = dashboard.appliance.getOrganizationApplianceUplinkStatuses(org_id, network_id)
pprint(wan_stats[3]['uplinks'])
