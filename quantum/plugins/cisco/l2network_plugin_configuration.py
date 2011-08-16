# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2011 Cisco Systems, Inc.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Sumit Naiksatam, Cisco Systems, Inc.
#

import os

from quantum.plugins.cisco.common import cisco_configparser as confp

CONF_FILE = "conf/l2network_plugin.ini"

cp = confp.CiscoConfigParser(os.path.dirname(os.path.realpath(__file__)) \
                             + "/" + CONF_FILE)

section = cp['VLANS']
VLAN_NAME_PREFIX = section['vlan_name_prefix']
VLAN_START = section['vlan_start']
VLAN_END = section['vlan_end']

section = cp['PORTS']
MAX_PORTS = section['max_ports']

section = cp['PORTPROFILES']
MAX_PORT_PROFILES = section['max_port_profiles']

section = cp['NETWORKS']
MAX_NETWORKS = section['max_networks']

section = cp['MODEL']
MODEL_CLASS = section['model_class']

CONF_FILE = "conf/plugins.ini"

cp = confp.CiscoConfigParser(os.path.dirname(os.path.realpath(__file__)) \
                             + "/" + CONF_FILE)
plugins = cp.walk(cp.dummy)
