import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";
import * as flux from "@worawat/flux";

const fluxInstall = await flux.getFluxInstall({
  targetPath: "clusters/my-cluster",
});

// Create kubernetes resource from generated manifests
const install = new k8s.yaml.ConfigGroup("flux-install", {
  yaml: fluxInstall.content,
});