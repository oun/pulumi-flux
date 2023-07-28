// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Pulumi.Flux
{
    public static class Config
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "IDE1006", Justification = 
        "Double underscore prefix used to avoid conflicts with variable names.")]
        private sealed class __Value<T>
        {
            private readonly Func<T> _getter;
            private T _value = default!;
            private bool _set;

            public __Value(Func<T> getter)
            {
                _getter = getter;
            }

            public T Get() => _set ? _value : _getter();

            public void Set(T value)
            {
                _value = value;
                _set = true;
            }
        }

        private static readonly global::Pulumi.Config __config = new global::Pulumi.Config("flux");

        private static readonly __Value<Pulumi.Flux.Config.Types.Git?> _git = new __Value<Pulumi.Flux.Config.Types.Git?>(() => __config.GetObject<Pulumi.Flux.Config.Types.Git>("git"));
        /// <summary>
        /// Configuration block with settings for Kubernetes.
        /// </summary>
        public static Pulumi.Flux.Config.Types.Git? Git
        {
            get => _git.Get();
            set => _git.Set(value);
        }

        private static readonly __Value<Pulumi.Flux.Config.Types.Kubernetes?> _kubernetes = new __Value<Pulumi.Flux.Config.Types.Kubernetes?>(() => __config.GetObject<Pulumi.Flux.Config.Types.Kubernetes>("kubernetes"));
        /// <summary>
        /// Configuration block with settings for Kubernetes.
        /// </summary>
        public static Pulumi.Flux.Config.Types.Kubernetes? Kubernetes
        {
            get => _kubernetes.Get();
            set => _kubernetes.Set(value);
        }

        public static class Types
        {

             public class Git
             {
                public string? AuthorEmail { get; set; } = null!;
                public string? AuthorName { get; set; } = null!;
                public string? Branch { get; set; } = null!;
                public string? CommitMessageAppendix { get; set; } = null!;
                public string? GpgKeyId { get; set; } = null!;
                public string? GpgKeyRing { get; set; } = null!;
                public string? GpgPassphrase { get; set; } = null!;
                public Pulumi.Flux.Config.Types.GitHttp? Http { get; set; } = null!;
                public Pulumi.Flux.Config.Types.GitSsh? Ssh { get; set; } = null!;
                public string Url { get; set; }
            }

             public class GitHttp
             {
                public bool? AllowInsecureHttp { get; set; }
                public string? CertificateAuthority { get; set; } = null!;
                public string? Password { get; set; } = null!;
                public string? Username { get; set; } = null!;
            }

             public class GitSsh
             {
                public string? Password { get; set; } = null!;
                public string? PrivateKey { get; set; } = null!;
                public string? Username { get; set; } = null!;
            }

             public class Kubernetes
             {
                public string? ClientCertificate { get; set; } = null!;
                public string? ClientKey { get; set; } = null!;
                public string? ClusterCaCertificate { get; set; } = null!;
                public string? ConfigContext { get; set; } = null!;
                public string? ConfigContextAuthInfo { get; set; } = null!;
                public string? ConfigContextCluster { get; set; } = null!;
                public string? ConfigPath { get; set; } = null!;
                public ImmutableArray<string> ConfigPaths { get; set; }
                public Pulumi.Flux.Config.Types.KubernetesExec? Exec { get; set; } = null!;
                public string? Host { get; set; } = null!;
                public bool? Insecure { get; set; }
                public string? Password { get; set; } = null!;
                public string? ProxyUrl { get; set; } = null!;
                public string? Token { get; set; } = null!;
                public string? Username { get; set; } = null!;
            }

             public class KubernetesExec
             {
                public string ApiVersion { get; set; }
                public ImmutableArray<string> Args { get; set; }
                public string Command { get; set; }
                public ImmutableDictionary<string, string>? Env { get; set; } = null!;
            }
        }
    }
}
