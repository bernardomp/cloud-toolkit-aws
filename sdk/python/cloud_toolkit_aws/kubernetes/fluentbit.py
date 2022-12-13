# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ..irsa import Irsa
from ._inputs import *
import pulumi_aws
import pulumi_kubernetes

__all__ = ['FluentbitArgs', 'Fluentbit']

@pulumi.input_type
class FluentbitArgs:
    def __init__(__self__, *,
                 aws_region: pulumi.Input[str],
                 cluster_name: pulumi.Input[str],
                 logging: Optional[pulumi.Input['FluentbitLoggingArgsArgs']] = None):
        """
        The set of arguments for constructing a Fluentbit resource.
        :param pulumi.Input[str] aws_region: The AWS Region.
        :param pulumi.Input[str] cluster_name: The cluster name.
        :param pulumi.Input['FluentbitLoggingArgsArgs'] logging: Configure logging.
        """
        pulumi.set(__self__, "aws_region", aws_region)
        pulumi.set(__self__, "cluster_name", cluster_name)
        if logging is not None:
            pulumi.set(__self__, "logging", logging)

    @property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> pulumi.Input[str]:
        """
        The AWS Region.
        """
        return pulumi.get(self, "aws_region")

    @aws_region.setter
    def aws_region(self, value: pulumi.Input[str]):
        pulumi.set(self, "aws_region", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The cluster name.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input['FluentbitLoggingArgsArgs']]:
        """
        Configure logging.
        """
        return pulumi.get(self, "logging")

    @logging.setter
    def logging(self, value: Optional[pulumi.Input['FluentbitLoggingArgsArgs']]):
        pulumi.set(self, "logging", value)


class Fluentbit(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_region: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 logging: Optional[pulumi.Input[pulumi.InputType['FluentbitLoggingArgsArgs']]] = None,
                 __props__=None):
        """
        Fluentbit is a component that deploy the Fluentbit component to send logs to AWS CloudWatch.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_region: The AWS Region.
        :param pulumi.Input[str] cluster_name: The cluster name.
        :param pulumi.Input[pulumi.InputType['FluentbitLoggingArgsArgs']] logging: Configure logging.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FluentbitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Fluentbit is a component that deploy the Fluentbit component to send logs to AWS CloudWatch.

        :param str resource_name: The name of the resource.
        :param FluentbitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FluentbitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_region: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 logging: Optional[pulumi.Input[pulumi.InputType['FluentbitLoggingArgsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FluentbitArgs.__new__(FluentbitArgs)

            if aws_region is None and not opts.urn:
                raise TypeError("Missing required property 'aws_region'")
            __props__.__dict__["aws_region"] = aws_region
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["logging"] = logging
            __props__.__dict__["application"] = None
            __props__.__dict__["irsa"] = None
            __props__.__dict__["log_group_application_log"] = None
            __props__.__dict__["log_group_dataplane_log"] = None
            __props__.__dict__["log_group_host_log"] = None
            __props__.__dict__["namespace"] = None
        super(Fluentbit, __self__).__init__(
            'cloud-toolkit-aws:kubernetes:Fluentbit',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def application(self) -> pulumi.Output[Optional['pulumi_kubernetes.apiextensions.CustomResource']]:
        return pulumi.get(self, "application")

    @property
    @pulumi.getter
    def irsa(self) -> pulumi.Output[Optional['Irsa']]:
        """
        IRSA for Fluentbit component
        """
        return pulumi.get(self, "irsa")

    @property
    @pulumi.getter(name="logGroupApplicationLog")
    def log_group_application_log(self) -> pulumi.Output[Optional['pulumi_aws.cloudwatch.LogGroup']]:
        """
        The AWS CloudWatch LogGroup where application logs are stored.
        """
        return pulumi.get(self, "log_group_application_log")

    @property
    @pulumi.getter(name="logGroupDataplaneLog")
    def log_group_dataplane_log(self) -> pulumi.Output[Optional['pulumi_aws.cloudwatch.LogGroup']]:
        """
        The AWS CloudWatch LogGroup where dataplane logs are stored.
        """
        return pulumi.get(self, "log_group_dataplane_log")

    @property
    @pulumi.getter(name="logGroupHostLog")
    def log_group_host_log(self) -> pulumi.Output[Optional['pulumi_aws.cloudwatch.LogGroup']]:
        """
        The AWS CloudWatch LogGroup where Hosts logs are stored.
        """
        return pulumi.get(self, "log_group_host_log")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional['pulumi_kubernetes.core.v1.Namespace']]:
        """
        The Namespace used to deploy the component.
        """
        return pulumi.get(self, "namespace")

