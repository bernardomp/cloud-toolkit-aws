import * as ct from "@cloud-toolkit/cloud-toolkit-aws";

const example = new ct.kubernetes.Cluster("test-sdk",{});

export const kubeconfig = example.kubeconfig;
