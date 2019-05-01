# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EventsPageViewInfo(Model):
    """The page view information.

    :param name: The name of the page
    :type name: str
    :param url: The URL of the page
    :type url: str
    :param duration: The duration of the page view
    :type duration: str
    :param performance_bucket: The performance bucket of the page view
    :type performance_bucket: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'str'},
        'performance_bucket': {'key': 'performanceBucket', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EventsPageViewInfo, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.url = kwargs.get('url', None)
        self.duration = kwargs.get('duration', None)
        self.performance_bucket = kwargs.get('performance_bucket', None)