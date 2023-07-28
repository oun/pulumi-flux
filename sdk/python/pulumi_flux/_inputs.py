# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'FluxBootstrapGitTimeoutsArgs',
    'ProviderGitArgs',
    'ProviderGitHttpArgs',
    'ProviderGitSshArgs',
    'ProviderKubernetesArgs',
    'ProviderKubernetesExecArgs',
]

@pulumi.input_type
class FluxBootstrapGitTimeoutsArgs:
    def __init__(__self__, *,
                 create: Optional[pulumi.Input[str]] = None,
                 delete: Optional[pulumi.Input[str]] = None,
                 read: Optional[pulumi.Input[str]] = None,
                 update: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] create: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        :param pulumi.Input[str] delete: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Setting a timeout for a Delete operation is only applicable if changes are saved into state before the destroy operation occurs.
        :param pulumi.Input[str] read: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        :param pulumi.Input[str] update: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        if create is not None:
            pulumi.set(__self__, "create", create)
        if delete is not None:
            pulumi.set(__self__, "delete", delete)
        if read is not None:
            pulumi.set(__self__, "read", read)
        if update is not None:
            pulumi.set(__self__, "update", update)

    @property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[str]]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        return pulumi.get(self, "create")

    @create.setter
    def create(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create", value)

    @property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[str]]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Setting a timeout for a Delete operation is only applicable if changes are saved into state before the destroy operation occurs.
        """
        return pulumi.get(self, "delete")

    @delete.setter
    def delete(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delete", value)

    @property
    @pulumi.getter
    def read(self) -> Optional[pulumi.Input[str]]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        """
        return pulumi.get(self, "read")

    @read.setter
    def read(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "read", value)

    @property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[str]]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        return pulumi.get(self, "update")

    @update.setter
    def update(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update", value)


@pulumi.input_type
class ProviderGitArgs:
    def __init__(__self__, *,
                 url: pulumi.Input[str],
                 author_email: Optional[pulumi.Input[str]] = None,
                 author_name: Optional[pulumi.Input[str]] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 commit_message_appendix: Optional[pulumi.Input[str]] = None,
                 gpg_key_id: Optional[pulumi.Input[str]] = None,
                 gpg_key_ring: Optional[pulumi.Input[str]] = None,
                 gpg_passphrase: Optional[pulumi.Input[str]] = None,
                 http: Optional[pulumi.Input['ProviderGitHttpArgs']] = None,
                 ssh: Optional[pulumi.Input['ProviderGitSshArgs']] = None):
        pulumi.set(__self__, "url", url)
        if author_email is not None:
            pulumi.set(__self__, "author_email", author_email)
        if author_name is not None:
            pulumi.set(__self__, "author_name", author_name)
        if branch is not None:
            pulumi.set(__self__, "branch", branch)
        if commit_message_appendix is not None:
            pulumi.set(__self__, "commit_message_appendix", commit_message_appendix)
        if gpg_key_id is not None:
            pulumi.set(__self__, "gpg_key_id", gpg_key_id)
        if gpg_key_ring is not None:
            pulumi.set(__self__, "gpg_key_ring", gpg_key_ring)
        if gpg_passphrase is not None:
            pulumi.set(__self__, "gpg_passphrase", gpg_passphrase)
        if http is not None:
            pulumi.set(__self__, "http", http)
        if ssh is not None:
            pulumi.set(__self__, "ssh", ssh)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="authorEmail")
    def author_email(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "author_email")

    @author_email.setter
    def author_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "author_email", value)

    @property
    @pulumi.getter(name="authorName")
    def author_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "author_name")

    @author_name.setter
    def author_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "author_name", value)

    @property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter(name="commitMessageAppendix")
    def commit_message_appendix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "commit_message_appendix")

    @commit_message_appendix.setter
    def commit_message_appendix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "commit_message_appendix", value)

    @property
    @pulumi.getter(name="gpgKeyId")
    def gpg_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "gpg_key_id")

    @gpg_key_id.setter
    def gpg_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gpg_key_id", value)

    @property
    @pulumi.getter(name="gpgKeyRing")
    def gpg_key_ring(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "gpg_key_ring")

    @gpg_key_ring.setter
    def gpg_key_ring(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gpg_key_ring", value)

    @property
    @pulumi.getter(name="gpgPassphrase")
    def gpg_passphrase(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "gpg_passphrase")

    @gpg_passphrase.setter
    def gpg_passphrase(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gpg_passphrase", value)

    @property
    @pulumi.getter
    def http(self) -> Optional[pulumi.Input['ProviderGitHttpArgs']]:
        return pulumi.get(self, "http")

    @http.setter
    def http(self, value: Optional[pulumi.Input['ProviderGitHttpArgs']]):
        pulumi.set(self, "http", value)

    @property
    @pulumi.getter
    def ssh(self) -> Optional[pulumi.Input['ProviderGitSshArgs']]:
        return pulumi.get(self, "ssh")

    @ssh.setter
    def ssh(self, value: Optional[pulumi.Input['ProviderGitSshArgs']]):
        pulumi.set(self, "ssh", value)


@pulumi.input_type
class ProviderGitHttpArgs:
    def __init__(__self__, *,
                 allow_insecure_http: Optional[pulumi.Input[bool]] = None,
                 certificate_authority: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        if allow_insecure_http is not None:
            pulumi.set(__self__, "allow_insecure_http", allow_insecure_http)
        if certificate_authority is not None:
            pulumi.set(__self__, "certificate_authority", certificate_authority)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="allowInsecureHttp")
    def allow_insecure_http(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_insecure_http")

    @allow_insecure_http.setter
    def allow_insecure_http(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_insecure_http", value)

    @property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "certificate_authority")

    @certificate_authority.setter
    def certificate_authority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_authority", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class ProviderGitSshArgs:
    def __init__(__self__, *,
                 password: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        if password is not None:
            pulumi.set(__self__, "password", password)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class ProviderKubernetesArgs:
    def __init__(__self__, *,
                 client_certificate: Optional[pulumi.Input[str]] = None,
                 client_key: Optional[pulumi.Input[str]] = None,
                 cluster_ca_certificate: Optional[pulumi.Input[str]] = None,
                 config_context: Optional[pulumi.Input[str]] = None,
                 config_context_auth_info: Optional[pulumi.Input[str]] = None,
                 config_context_cluster: Optional[pulumi.Input[str]] = None,
                 config_path: Optional[pulumi.Input[str]] = None,
                 config_paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 exec_: Optional[pulumi.Input['ProviderKubernetesExecArgs']] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 proxy_url: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        if client_certificate is not None:
            pulumi.set(__self__, "client_certificate", client_certificate)
        if client_key is not None:
            pulumi.set(__self__, "client_key", client_key)
        if cluster_ca_certificate is not None:
            pulumi.set(__self__, "cluster_ca_certificate", cluster_ca_certificate)
        if config_context is not None:
            pulumi.set(__self__, "config_context", config_context)
        if config_context_auth_info is not None:
            pulumi.set(__self__, "config_context_auth_info", config_context_auth_info)
        if config_context_cluster is not None:
            pulumi.set(__self__, "config_context_cluster", config_context_cluster)
        if config_path is not None:
            pulumi.set(__self__, "config_path", config_path)
        if config_paths is not None:
            pulumi.set(__self__, "config_paths", config_paths)
        if exec_ is not None:
            pulumi.set(__self__, "exec_", exec_)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if insecure is not None:
            pulumi.set(__self__, "insecure", insecure)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if proxy_url is not None:
            pulumi.set(__self__, "proxy_url", proxy_url)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "client_certificate")

    @client_certificate.setter
    def client_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_certificate", value)

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "client_key")

    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_key", value)

    @property
    @pulumi.getter(name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_ca_certificate")

    @cluster_ca_certificate.setter
    def cluster_ca_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_ca_certificate", value)

    @property
    @pulumi.getter(name="configContext")
    def config_context(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "config_context")

    @config_context.setter
    def config_context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_context", value)

    @property
    @pulumi.getter(name="configContextAuthInfo")
    def config_context_auth_info(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "config_context_auth_info")

    @config_context_auth_info.setter
    def config_context_auth_info(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_context_auth_info", value)

    @property
    @pulumi.getter(name="configContextCluster")
    def config_context_cluster(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "config_context_cluster")

    @config_context_cluster.setter
    def config_context_cluster(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_context_cluster", value)

    @property
    @pulumi.getter(name="configPath")
    def config_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "config_path")

    @config_path.setter
    def config_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_path", value)

    @property
    @pulumi.getter(name="configPaths")
    def config_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "config_paths")

    @config_paths.setter
    def config_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "config_paths", value)

    @property
    @pulumi.getter(name="exec")
    def exec_(self) -> Optional[pulumi.Input['ProviderKubernetesExecArgs']]:
        return pulumi.get(self, "exec_")

    @exec_.setter
    def exec_(self, value: Optional[pulumi.Input['ProviderKubernetesExecArgs']]):
        pulumi.set(self, "exec_", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def insecure(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "insecure")

    @insecure.setter
    def insecure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "proxy_url")

    @proxy_url.setter
    def proxy_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proxy_url", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class ProviderKubernetesExecArgs:
    def __init__(__self__, *,
                 api_version: pulumi.Input[str],
                 command: pulumi.Input[str],
                 args: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 env: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        pulumi.set(__self__, "api_version", api_version)
        pulumi.set(__self__, "command", command)
        if args is not None:
            pulumi.set(__self__, "args", args)
        if env is not None:
            pulumi.set(__self__, "env", env)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Input[str]:
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter
    def command(self) -> pulumi.Input[str]:
        return pulumi.get(self, "command")

    @command.setter
    def command(self, value: pulumi.Input[str]):
        pulumi.set(self, "command", value)

    @property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "args")

    @args.setter
    def args(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "args", value)

    @property
    @pulumi.getter
    def env(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "env")

    @env.setter
    def env(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "env", value)

