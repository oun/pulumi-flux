import * as pulumi from "@pulumi/pulumi";
import * as tls from "@pulumi/tls";
import * as github from "@pulumi/github";
import * as flux from "@worawat/flux";

// Require Github configurations
// export GITHUB_TOKEN=your-github-personal-access-token
// export GITHUB_OWNER=your-github-owner

const repoName = "pulumi-flux-sample";
const branch = "main";
const path = "clusters/dev";
const githubOwner = "oun";

const key = new tls.PrivateKey("key", {
  algorithm: "ECDSA",
  ecdsaCurve: "P256",
});

const repo = new github.Repository("repo", {
  name: repoName,
  visibility: "private",
  autoInit: true,
});

new github.BranchDefault("default", {
  repository: repo.name,
  branch: branch,
});

const deployKey = new github.RepositoryDeployKey("key", {
  title: "fluxcd",
  repository: repo.name,
  key: key.publicKeyOpenssh,
  readOnly: false,
});

const provider = new flux.Provider("flux", {
  kubernetes: {
    configPath: "~/.kube/config",
  },
  git: {
    url: `ssh://git@github.com/${githubOwner}/${repoName}.git`,
    branch: branch,
    ssh: {
      username: "git",
      privateKey: key.privateKeyPem,
    },
  },
});

const resource = new flux.FluxBootstrapGit(
  "flux",
  {
    path: path,
  },
  {
    provider: provider,
    dependsOn: deployKey,
  }
);

