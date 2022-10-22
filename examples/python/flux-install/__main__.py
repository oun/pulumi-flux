"""A Python Pulumi program"""

import pulumi_flux as flux
from pulumi_kubernetes.yaml import ConfigGroup

manifests = flux.get_flux_install(
    target_path="clusters/my-cluster", network_policy=False
)

# Create kubernetes resource from generated manifests
ConfigGroup("flux-install", yaml=[manifests.content])
