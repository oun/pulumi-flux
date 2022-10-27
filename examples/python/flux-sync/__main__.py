"""A Python Pulumi program"""
import pulumi
import pulumi_flux as flux
import pulumi_github as github
import pulumi_tls as tls
import pulumi_kubernetes as k8s

# Require Github configurations
# export GITHUB_TOKEN=your-github-personal-access-token
# export GITHUB_OWNER=your-github-owner
branch = "main"
target_path = "clusters/my-cluster"
repository_name = "flux-sample"
github_owner = "oun"
known_hosts = "github.com ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEmKSENjQEezOmxkZMy7opKgwFB9nkt5YRrYMjNuG5N87uRgg6CLrbo5wAdT/y6v0mKV0U2w0WZ2YB/++Tpockg="

ssh_key = tls.PrivateKey("key", algorithm="ECDSA", ecdsa_curve="P256")

# Create Github repository
repository = github.Repository(
    "flux", name=repository_name, visibility="private", auto_init=True
)
github.BranchDefault("default", repository=repository.name, branch=branch)
github.RepositoryDeployKey(
    "flux-key",
    title="flux",
    repository=repository.name,
    key=ssh_key.public_key_openssh,
    read_only=True,
)

flux_install = flux.get_flux_install(target_path=target_path)
flux_sync = flux.get_flux_sync(
    target_path=target_path,
    url=f"ssh://git@github.com/{github_owner}/{repository_name}.git",
    branch=branch,
)

# Create kubernetes resource from generated manifests
install = k8s.yaml.ConfigGroup("flux-install", yaml=[flux_install.content])
sync = k8s.yaml.ConfigGroup("flux-sync", yaml=[flux_sync.content])

k8s.core.v1.Secret(
    "flux",
    metadata=k8s.meta.v1.ObjectMetaArgs(
        name=flux_sync.secret, namespace=flux_sync.namespace
    ),
    string_data={
        "identity": ssh_key.private_key_pem,
        "identity.pub": ssh_key.public_key_pem,
        "known_hosts": known_hosts,
    },
    opts=pulumi.ResourceOptions(depends_on=install)
)

# Commit files to Github
github.RepositoryFile(
    "install",
    repository=repository.name,
    file=flux_install.path,
    content=flux_install.content,
    branch=branch,
    opts=pulumi.ResourceOptions(depends_on=install)
)
github.RepositoryFile(
    "sync",
    repository=repository.name,
    file=flux_sync.path,
    content=flux_sync.content,
    branch=branch,
    opts=pulumi.ResourceOptions(depends_on=install)
)
github.RepositoryFile(
    "kustomize",
    repository=repository.name,
    file=flux_sync.kustomize_path,
    content=flux_sync.kustomize_content,
    branch=branch,
    opts=pulumi.ResourceOptions(depends_on=install)
)
