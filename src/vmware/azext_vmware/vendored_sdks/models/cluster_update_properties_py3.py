# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ClusterUpdateProperties(Model):
    """The properties of a cluster that may be updated.

    :param cluster_size: The cluster size
    :type cluster_size: int
    """

    _attribute_map = {
        'cluster_size': {'key': 'clusterSize', 'type': 'int'},
    }

    def __init__(self, *, cluster_size: int=None, **kwargs) -> None:
        super(ClusterUpdateProperties, self).__init__(**kwargs)
        self.cluster_size = cluster_size
