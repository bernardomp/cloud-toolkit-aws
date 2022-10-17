import * as pulumi from "@pulumi/pulumi";
import { IrsaApplicationAddonArgs } from "./applicationAddonArgs";

export interface ClusterAutoscalerArgs extends IrsaApplicationAddonArgs {
    clusterName: pulumi.Input<string>;
    downscale?: ClusterAutoscalerDonwscaleArgs
  }

export interface ClusterAutoscalerDonwscaleArgs {
  delayAfterAdd?: number;
  delayAfterDelete?: number;
  delayAfterFailure?: number;
  unneededTime?: number;
}