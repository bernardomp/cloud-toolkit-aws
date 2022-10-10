// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

import * as pulumiAws from "@pulumi/aws";
import * as pulumiRandom from "@pulumi/random";

/**
 * Cloud Toolkit component for Mysql instances.
 */
export class Mysql extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'cloud-toolkit-aws:databases:Mysql';

    /**
     * Returns true if the given object is an instance of Mysql.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Mysql {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Mysql.__pulumiType;
    }

    /**
     * Security rules to allow connections to this databse instance
     */
    public /*out*/ readonly ingressSecurityGroupRules!: pulumi.Output<pulumiAws.ec2.SecurityGroupRule[]>;
    /**
     * Underlying database instance for this component
     */
    public readonly instance!: pulumi.Output<pulumiAws.rds.Instance>;
    /**
     * Random password generated for admin user
     */
    public /*out*/ readonly instancePassword!: pulumi.Output<pulumiRandom.RandomPassword>;
    /**
     * Component that protects and stores admin password in AWS
     */
    public /*out*/ readonly secret!: pulumi.Output<pulumiAws.secretsmanager.Secret>;
    /**
     *
     * Component that updates secrets in AWS
     */
    public /*out*/ readonly secretVersion!: pulumi.Output<pulumiAws.secretsmanager.SecretVersion>;
    /**
     * Security Group attached to this database instance
     */
    public /*out*/ readonly securityGroup!: pulumi.Output<pulumiAws.ec2.SecurityGroup>;
    /**
     * Set of subnets in which database instance will be deployed
     */
    public /*out*/ readonly subnetGroup!: pulumi.Output<pulumiAws.rds.SubnetGroup | undefined>;

    /**
     * Create a Mysql resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MysqlArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.database === undefined) && !opts.urn) {
                throw new Error("Missing required property 'database'");
            }
            if ((!args || args.version === undefined) && !opts.urn) {
                throw new Error("Missing required property 'version'");
            }
            resourceInputs["backup"] = args ? args.backup : undefined;
            resourceInputs["database"] = args ? args.database : undefined;
            resourceInputs["instance"] = args ? args.instance : undefined;
            resourceInputs["networking"] = args ? args.networking : undefined;
            resourceInputs["storage"] = args ? args.storage : undefined;
            resourceInputs["version"] = args ? args.version : undefined;
            resourceInputs["ingressSecurityGroupRules"] = undefined /*out*/;
            resourceInputs["instancePassword"] = undefined /*out*/;
            resourceInputs["secret"] = undefined /*out*/;
            resourceInputs["secretVersion"] = undefined /*out*/;
            resourceInputs["securityGroup"] = undefined /*out*/;
            resourceInputs["subnetGroup"] = undefined /*out*/;
        } else {
            resourceInputs["ingressSecurityGroupRules"] = undefined /*out*/;
            resourceInputs["instance"] = undefined /*out*/;
            resourceInputs["instancePassword"] = undefined /*out*/;
            resourceInputs["secret"] = undefined /*out*/;
            resourceInputs["secretVersion"] = undefined /*out*/;
            resourceInputs["securityGroup"] = undefined /*out*/;
            resourceInputs["subnetGroup"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Mysql.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a Mysql resource.
 */
export interface MysqlArgs {
    /**
     * Backup configuration parameters for the database instance
     */
    backup?: pulumi.Input<inputs.databases.MysqlBackupArgsArgs>;
    /**
     * Configuration parameters for the database instance
     */
    database: pulumi.Input<inputs.databases.MysqlDatabaseArgsArgs>;
    /**
     * Instance type to run the database instance
     */
    instance?: pulumi.Input<string>;
    /**
     * Network configuration parameters for the database instance
     */
    networking?: pulumi.Input<inputs.databases.MysqlNetworkingArgsArgs>;
    /**
     * Storage configuration parameters for the database instance
     */
    storage?: pulumi.Input<inputs.databases.MysqlStorageArgsArgs>;
    /**
     * Version for database instance
     */
    version: pulumi.Input<enums.databases.MysqlVersion>;
}
