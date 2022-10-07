---
title: FluxCD
meta_desc: The Flux Provider lets you manage FluxCD resources.
layout: overview
---

This Pulumi provider wrap the Terraform provider for [Flux v2](https://fluxcd.io/). 
The provider allows you to install Flux on Kubernetes and configure it to reconcile the cluster state from a Git repository.

## Example

{{< chooser language "python" >}}
{{% choosable language python %}}

```typescript
import pulumi_flux as flux
from pulumi_kubernetes.yaml import ConfigGroup

manifests = flux.get_flux_install(
    target_path="clusters/my-cluster", network_policy=False
)

# Create kubernetes resource from generated manifests
ConfigGroup("flux-install", yaml=[manifests.content])
```
{{% /choosable %}}
{{< /chooser >}}