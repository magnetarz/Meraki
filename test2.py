import argparse
import meraki
import json
import os
import urllib.parse
from datetime import datetime
from key import MERAKI_API_KEY

dashboard = meraki.DashboardAPI(
    MERAKI_API_KEY,
    output_log=False
    )

orgs = dashboard.organizations.getOrganizations("Devnet Sandbox")
org_id = orgs[0]['id']


networks = dashboard.organizations.getOrganizationNetworks(org_id, name="CCNP")
network_id = networks[0]['id']


topology = dashboard.networks.getNetworkTopologyLinkLayer(network_id)
wan_stats = dashboard.appliance.getOrganizationApplianceUplinkStatuses(org_id, network_id)
print(wan_stats)
