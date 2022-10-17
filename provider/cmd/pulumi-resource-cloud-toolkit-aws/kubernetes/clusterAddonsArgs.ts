import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";
import * as aws from "@pulumi/aws";

export interface ClusterAddonsArgs {
  k8sProvider: kubernetes.Provider;
  identityProvidersArn: pulumi.Input<string>[];
  issuerUrl: pulumi.Input<string>;
  domain: string;
  ingress?: ClusterAddonsIngressArgs;
  zoneArns: pulumi.Input<string>[];
  clusterName: pulumi.Input<string>;
  clusterAutoscaler: ClusterAddonsClusterAutoscalerArgs;
}

export interface ClusterAddonsIngressArgs {
  enabled?: boolean;
  admin?: ClusterAddonsIngressItemArgs;
  global?: ClusterAddonsIngressItemArgs;
}

export interface ClusterAddonsIngressItemArgs {
  public?: boolean;
  whitelist?: pulumi.Input<string>[];
}

export interface ClusterAddonsClusterAutoscalerArgs {
  delayAfterAdd?: number;
  delayAfterDelete?: number;
  delayAfterFailure?: number;
  unneededTime?: number;
}

export const defaultClusterAddonsArgs = {
  ingress: {
    enabled: true,
    admin: {
      public: true,
      whitelist: ["0.0.0.0/0"],
    },
    global: {
      public: true,
      whitelist: ["0.0.0.0/0"],
    }
  }
};
