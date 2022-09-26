# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .example import *
from .provider import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import cloud_toolkit_aws.storage as __storage
    storage = __storage
else:
    storage = _utilities.lazy_import('cloud_toolkit_aws.storage')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "cloud-toolkit-aws",
  "mod": "index",
  "fqn": "cloud_toolkit_aws",
  "classes": {
   "cloud-toolkit-aws:index:Example": "Example"
  }
 },
 {
  "pkg": "cloud-toolkit-aws",
  "mod": "storage",
  "fqn": "cloud_toolkit_aws.storage",
  "classes": {
   "cloud-toolkit-aws:storage:Bucket": "Bucket"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "cloud-toolkit-aws",
  "token": "pulumi:providers:cloud-toolkit-aws",
  "fqn": "cloud_toolkit_aws",
  "class": "Provider"
 }
]
"""
)
