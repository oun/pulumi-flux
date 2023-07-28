# Flux Bootstrap Git Example

This example deploy Flux into a Kubernetes cluster and configure it to synchroize from a Github repository.

If you don't have a Kuberentes cluster, create one using Kind:

```shell
kind create cluster --name pulumi-fluxcd-nodejs
```

Generate a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) (PAT) with repo permissions, make sure to copy the generated token.

Configure Github personal access token and repository owner:

```shell
export GITHUB_TOKEN=<your-github-personal-access-token>
export GITHUB_OWNER=<your-github-owner>
```

Update `repo_name` and `github_owner` variables in __main__.py.

```python
repo_name = "your-deployment-repository"
github_owner = "your-github-owner"
```

Run `pulumi up`.