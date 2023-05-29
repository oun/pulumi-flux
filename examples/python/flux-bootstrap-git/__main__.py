"""A Python Pulumi program"""
import pulumi
import pulumi_flux as flux
import pulumi_github as github
import pulumi_tls as tls

# Require Github configurations
# export GITHUB_TOKEN=your-github-personal-access-token
# export GITHUB_OWNER=your-github-owner

branch = "main"
target_path = "clusters/dev"
repo_name = "pulumi-flux-python-sample"
github_owner = "oun"

ssh_key = tls.PrivateKey("key", algorithm="ECDSA", ecdsa_curve="P256")

repository = github.Repository(
    "flux", name=repo_name, visibility="private", auto_init=True
)

github.BranchDefault("default", repository=repository.name, branch=branch)

deploy_key = github.RepositoryDeployKey(
    "flux-key",
    title="flux",
    repository=repository.name,
    key=ssh_key.public_key_openssh,
    read_only=False,
)

provider = flux.Provider(
    "flux",
    kubernetes=flux.ProviderKubernetesArgs(config_path="~/.kube/config"),
    git=flux.ProviderGitArgs(
        url=f"ssh://git@github.com/{github_owner}/{repo_name}.git",
        branch=branch,
        ssh=flux.ProviderGitSshArgs(username="git", private_key=ssh_key.private_key_pem)
    )
)

resource = flux.FluxBootstrapGit(
    "flux",
    path=target_path,
    opts=pulumi.ResourceOptions(provider=provider, depends_on=deploy_key)
)