#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for vyos_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: vyos_interfaces
short_description: Interfaces resource module
description:
- This module manages the interface attributes on VyOS network devices.
- This module supports managing base attributes of Ethernet, Bonding, VXLAN, Loopback
  and Virtual Tunnel Interfaces.
version_added: 1.0.0
notes:
- Tested against VyOS 1.1.8 (helium).
- This module works with connection C(network_cli). See L(the VyOS OS Platform Options,../network/user_guide/platform_vyos.html).
author:
- Nilashish Chakraborty (@nilashishc)
- Rohit Thakur (@rohitthakur2590)
options:
  config:
    description: The provided interfaces configuration.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Full name of the interface, e.g. eth0, eth1, bond0, vti1, vxlan2.
        type: str
        required: true
      description:
        description:
        - Interface description.
        type: str
      duplex:
        description:
        - Interface duplex mode.
        - Applicable for Ethernet interfaces only.
        choices:
        - full
        - half
        - auto
        type: str
      enabled:
        default: true
        description:
        - Administrative state of the interface.
        - Set the value to C(true) to administratively enable the interface or C(false)
          to disable it.
        type: bool
      mtu:
        description:
        - MTU for a specific interface. Refer to vendor documentation for valid values.
        - Applicable for Ethernet, Bonding, VXLAN and Virtual Tunnel interfaces.
        type: int
      speed:
        description:
        - Interface link speed.
        - Applicable for Ethernet interfaces only.
        type: str
        choices:
        - auto
        - '10'
        - '100'
        - '1000'
        - '2500'
        - '10000'
      vifs:
        description:
        - Virtual sub-interfaces related configuration.
        - 802.1Q VLAN interfaces are represented as virtual sub-interfaces in VyOS.
        type: list
        elements: dict
        suboptions:
          vlan_id:
            description:
            - Identifier for the virtual sub-interface.
            type: int
          description:
            description:
            - Virtual sub-interface description.
            type: str
          enabled:
            description:
            - Administrative state of the virtual sub-interface.
            - Set the value to C(true) to administratively enable the interface or
              C(false) to disable it.
            type: bool
            default: true
          mtu:
            description:
            - MTU for the virtual sub-interface.
            - Refer to vendor documentation for valid values.
            type: int
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the VyOS device
      by executing the command B(show configuration commands | grep interfaces).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
    - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - rendered
    - gathered
    - parsed
    default: merged
"""
EXAMPLES = """
# Using merged
#
# -------------
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces loopback lo

- name: Merge provided configuration with device configuration
  vyos.vyos.vyos_interfaces:
    config:
    - name: eth2
      description: Configured by Ansible
      enabled: true
      vifs:
      - vlan_id: 200
        description: VIF 200 - ETH2

    - name: eth3
      description: Configured by Ansible
      mtu: 1500

    - name: bond1
      description: Bond - 1
      mtu: 1200

    - name: vti2
      description: VTI - 2
      enabled: false
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# "before": [
#      	{
#            "enabled": true,
#            "name": "lo"
#      	},
#       {
#            "enabled": true,
#            "name": "eth3"
#        },
#        {
#            "enabled": true,
#            "name": "eth2"
#        },
#        {
#            "enabled": true,
#            "name": "eth1"
#        },
#        {
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
# "commands": [
#        "set interfaces ethernet eth2 description 'Configured by Ansible'",
#        "set interfaces ethernet eth2 vif 200",
#        "set interfaces ethernet eth2 vif 200 description 'VIF 200 - ETH2'",
#        "set interfaces ethernet eth3 description 'Configured by Ansible'",
#        "set interfaces ethernet eth3 mtu '1500'",
#        "set interfaces bonding bond1",
#        "set interfaces bonding bond1 description 'Bond - 1'",
#        "set interfaces bonding bond1 mtu '1200'",
#        "set interfaces vti vti2",
#        "set interfaces vti vti2 description 'VTI - 2'",
#        "set interfaces vti vti2 disable"
#    ]
#
# "after": [
#        {
#            "description": "Bond - 1",
#            "enabled": true,
#            "mtu": 1200,
#            "name": "bond1"
#        },
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "description": "VTI - 2",
#            "enabled": false,
#            "name": "vti2"
#        },
#        {
#            "description": "Configured by Ansible",
#            "enabled": true,
#            "mtu": 1500,
#            "name": "eth3"
#        },
#        {
#            "description": "Configured by Ansible",
#            "enabled": true,
#            "name": "eth2",
#            "vifs": [
#                {
#                    "description": "VIF 200 - ETH2",
#                    "enabled": true,
#                    "vlan_id": "200"
#                }
#            ]
#        },
#        {
#            "enabled": true,
#            "name": "eth1"
#        },
#        {
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
#
# -------------
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces bonding bond1 description 'Bond - 1'
# set interfaces bonding bond1 mtu '1200'
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth2 description 'Configured by Ansible'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth2 vif 200 description 'VIF 200 - ETH2'
# set interfaces ethernet eth3 description 'Configured by Ansible'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 mtu '1500'
# set interfaces loopback lo
# set interfaces vti vti2 description 'VTI - 2'
# set interfaces vti vti2 disable
#


# Using replaced
#
# -------------
# Before state:
# -------------
#
# vyos:~$ show configuration commands | grep eth
# set interfaces bonding bond1 description 'Bond - 1'
# set interfaces bonding bond1 mtu '1400'
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 description 'Management Interface for the Appliance'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:f3:6c:b5'
# set interfaces ethernet eth0 smp_affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 description 'Configured by Ansible Eng Team'
# set interfaces ethernet eth1 duplex 'full'
# set interfaces ethernet eth1 hw-id '08:00:27:ad:ef:65'
# set interfaces ethernet eth1 smp_affinity 'auto'
# set interfaces ethernet eth1 speed '100'
# set interfaces ethernet eth2 description 'Configured by Ansible'
# set interfaces ethernet eth2 duplex 'full'
# set interfaces ethernet eth2 hw-id '08:00:27:ab:4e:79'
# set interfaces ethernet eth2 mtu '500'
# set interfaces ethernet eth2 smp_affinity 'auto'
# set interfaces ethernet eth2 speed '100'
# set interfaces ethernet eth2 vif 200 description 'Configured by Ansible'
# set interfaces ethernet eth3 description 'Configured by Ansible'
# set interfaces ethernet eth3 duplex 'full'
# set interfaces ethernet eth3 hw-id '08:00:27:17:3c:85'
# set interfaces ethernet eth3 mtu '1500'
# set interfaces ethernet eth3 smp_affinity 'auto'
# set interfaces ethernet eth3 speed '100'
# set interfaces loopback lo
#
#
- name: Replace device configurations of listed interfaces with provided configurations
  vyos.vyos.vyos_interfaces:
    config:
    - name: eth2
      description: Replaced by Ansible

    - name: eth3
      description: Replaced by Ansible

    - name: eth1
      description: Replaced by Ansible
    state: replaced
#
#
# -----------------------
# Module Execution Result
# -----------------------
#
# "before": [
#        {
#            "description": "Bond - 1",
#            "enabled": true,
#            "mtu": 1400,
#            "name": "bond1"
#        },
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "description": "Configured by Ansible",
#            "duplex": "full",
#            "enabled": true,
#            "mtu": 1500,
#            "name": "eth3",
#            "speed": "100"
#        },
#        {
#            "description": "Configured by Ansible",
#            "duplex": "full",
#            "enabled": true,
#            "mtu": 500,
#            "name": "eth2",
#            "speed": "100",
#            "vifs": [
#                {
#                    "description": "VIF 200 - ETH2",
#                    "enabled": true,
#                    "vlan_id": "200"
#                }
#            ]
#        },
#        {
#            "description": "Configured by Ansible Eng Team",
#            "duplex": "full",
#            "enabled": true,
#            "name": "eth1",
#            "speed": "100"
#        },
#        {
#            "description": "Management Interface for the Appliance",
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
# "commands": [
#        "delete interfaces ethernet eth2 speed",
#        "delete interfaces ethernet eth2 duplex",
#        "delete interfaces ethernet eth2 mtu",
#        "delete interfaces ethernet eth2 vif 200 description",
#        "set interfaces ethernet eth2 description 'Replaced by Ansible'",
#        "delete interfaces ethernet eth3 speed",
#        "delete interfaces ethernet eth3 duplex",
#        "delete interfaces ethernet eth3 mtu",
#        "set interfaces ethernet eth3 description 'Replaced by Ansible'",
#        "delete interfaces ethernet eth1 speed",
#        "delete interfaces ethernet eth1 duplex",
#        "set interfaces ethernet eth1 description 'Replaced by Ansible'"
#    ]
#
# "after": [
#        {
#            "description": "Bond - 1",
#            "enabled": true,
#            "mtu": 1400,
#            "name": "bond1"
#        },
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "description": "Replaced by Ansible",
#            "enabled": true,
#            "name": "eth3"
#        },
#        {
#            "description": "Replaced by Ansible",
#            "enabled": true,
#            "name": "eth2",
#            "vifs": [
#                {
#                    "enabled": true,
#                    "vlan_id": "200"
#                }
#            ]
#        },
#        {
#            "description": "Replaced by Ansible",
#            "enabled": true,
#            "name": "eth1"
#        },
#        {
#            "description": "Management Interface for the Appliance",
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
#
# -------------
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces bonding bond1 description 'Bond - 1'
# set interfaces bonding bond1 mtu '1400'
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 description 'Management Interface for the Appliance'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 description 'Replaced by Ansible'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth2 description 'Replaced by Ansible'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth2 vif 200
# set interfaces ethernet eth3 description 'Replaced by Ansible'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces loopback lo
#
#
# Using overridden
#
#
# --------------
# Before state
# --------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 description 'Ethernet Interface - 0'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 mtu '1200'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 description 'Configured by Ansible Eng Team'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 mtu '100'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth1 vif 100 description 'VIF 100 - ETH1'
# set interfaces ethernet eth1 vif 100 disable
# set interfaces ethernet eth2 description 'Configured by Ansible Team (Admin Down)'
# set interfaces ethernet eth2 disable
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 mtu '600'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth3 description 'Configured by Ansible Network'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces loopback lo
# set interfaces vti vti1 description 'Virtual Tunnel Interface - 1'
# set interfaces vti vti1 mtu '68'
#
#
- name: Overrides all device configuration with provided configuration
  vyos.vyos.vyos_interfaces:
    config:
    - name: eth0
      description: Outbound Interface For The Appliance
      speed: auto
      duplex: auto

    - name: eth2
      speed: auto
      duplex: auto

    - name: eth3
      mtu: 1200
    state: overridden
#
#
# ------------------------
# Module Execution Result
# ------------------------
#
# "before": [
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "description": "Virtual Tunnel Interface - 1",
#            "enabled": true,
#            "mtu": 68,
#            "name": "vti1"
#        },
#        {
#            "description": "Configured by Ansible Network",
#            "enabled": true,
#            "name": "eth3"
#        },
#        {
#            "description": "Configured by Ansible Team (Admin Down)",
#            "enabled": false,
#            "mtu": 600,
#            "name": "eth2"
#        },
#        {
#            "description": "Configured by Ansible Eng Team",
#            "enabled": true,
#            "mtu": 100,
#            "name": "eth1",
#            "vifs": [
#                {
#                    "description": "VIF 100 - ETH1",
#                    "enabled": false,
#                    "vlan_id": "100"
#                }
#            ]
#        },
#        {
#            "description": "Ethernet Interface - 0",
#            "duplex": "auto",
#            "enabled": true,
#            "mtu": 1200,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
# "commands": [
#        "delete interfaces vti vti1 description",
#        "delete interfaces vti vti1 mtu",
#        "delete interfaces ethernet eth1 description",
#        "delete interfaces ethernet eth1 mtu",
#        "delete interfaces ethernet eth1 vif 100 description",
#        "delete interfaces ethernet eth1 vif 100 disable",
#        "delete interfaces ethernet eth0 mtu",
#        "set interfaces ethernet eth0 description 'Outbound Interface For The Appliance'",
#        "delete interfaces ethernet eth2 description",
#        "delete interfaces ethernet eth2 mtu",
#        "set interfaces ethernet eth2 duplex 'auto'",
#        "delete interfaces ethernet eth2 disable",
#        "set interfaces ethernet eth2 speed 'auto'",
#        "delete interfaces ethernet eth3 description",
#        "set interfaces ethernet eth3 mtu '1200'"
#    ],
#
# "after": [
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "enabled": true,
#            "name": "vti1"
#        },
#        {
#            "enabled": true,
#            "mtu": 1200,
#            "name": "eth3"
#        },
#        {
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth2",
#            "speed": "auto"
#        },
#        {
#            "enabled": true,
#            "name": "eth1",
#            "vifs": [
#                {
#                    "enabled": true,
#                    "vlan_id": "100"
#                }
#            ]
#        },
#        {
#            "description": "Outbound Interface For The Appliance",
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
#
# ------------
# After state
# ------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 description 'Outbound Interface For The Appliance'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth1 vif 100
# set interfaces ethernet eth2 duplex 'auto'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth2 speed 'auto'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 mtu '1200'
# set interfaces loopback lo
# set interfaces vti vti1
#
#
# Using deleted
#
#
# -------------
# Before state
# -------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces bonding bond0 mtu '1300'
# set interfaces bonding bond1 description 'LAG - 1'
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 description 'Outbound Interface for this appliance'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 description 'Configured by Ansible Network'
# set interfaces ethernet eth1 duplex 'full'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth1 speed '100'
# set interfaces ethernet eth2 description 'Configured by Ansible'
# set interfaces ethernet eth2 disable
# set interfaces ethernet eth2 duplex 'full'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 mtu '600'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth2 speed '100'
# set interfaces ethernet eth3 description 'Configured by Ansible Network'
# set interfaces ethernet eth3 duplex 'full'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 speed '100'
# set interfaces loopback lo
#
#
- name: Delete attributes of given interfaces (Note - This won't delete the interfaces
    themselves)
  vyos.vyos.vyos_interfaces:
    config:
    - name: bond1

    - name: eth1

    - name: eth2

    - name: eth3
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
# "before": [
#        {
#            "enabled": true,
#            "mtu": 1300,
#            "name": "bond0"
#        },
#        {
#            "description": "LAG - 1",
#            "enabled": true,
#            "name": "bond1"
#        },
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "description": "Configured by Ansible Network",
#            "duplex": "full",
#            "enabled": true,
#            "name": "eth3",
#            "speed": "100"
#        },
#        {
#            "description": "Configured by Ansible",
#            "duplex": "full",
#            "enabled": false,
#            "mtu": 600,
#            "name": "eth2",
#            "speed": "100"
#        },
#        {
#            "description": "Configured by Ansible Network",
#            "duplex": "full",
#            "enabled": true,
#            "name": "eth1",
#            "speed": "100"
#        },
#        {
#            "description": "Outbound Interface for this appliance",
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
# "commands": [
#        "delete interfaces bonding bond1 description",
#        "delete interfaces ethernet eth1 speed",
#        "delete interfaces ethernet eth1 duplex",
#        "delete interfaces ethernet eth1 description",
#        "delete interfaces ethernet eth2 speed",
#        "delete interfaces ethernet eth2 disable",
#        "delete interfaces ethernet eth2 duplex",
#        "delete interfaces ethernet eth2 disable",
#        "delete interfaces ethernet eth2 description",
#        "delete interfaces ethernet eth2 disable",
#        "delete interfaces ethernet eth2 mtu",
#        "delete interfaces ethernet eth2 disable",
#        "delete interfaces ethernet eth3 speed",
#        "delete interfaces ethernet eth3 duplex",
#        "delete interfaces ethernet eth3 description"
#    ]
#
# "after": [
#        {
#            "enabled": true,
#            "mtu": 1300,
#            "name": "bond0"
#        },
#        {
#            "enabled": true,
#            "name": "bond1"
#        },
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "enabled": true,
#            "name": "eth3"
#        },
#        {
#            "enabled": true,
#            "name": "eth2"
#        },
#        {
#            "enabled": true,
#            "name": "eth1"
#        },
#        {
#            "description": "Outbound Interface for this appliance",
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
#
# ------------
# After state
# ------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces bonding bond0 mtu '1300'
# set interfaces bonding bond1
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 description 'Outbound Interface for this appliance'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces loopback lo
#
#


# Using gathered
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep interfaces
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:50:5e:19'
# set interfaces ethernet eth0 smp_affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 description 'Configured by Ansible'
# set interfaces ethernet eth1 duplex 'auto'
# set interfaces ethernet eth1 mtu '1500'
# set interfaces ethernet eth1 speed 'auto'
# set interfaces ethernet eth1 vif 200 description 'VIF - 200'
# set interfaces ethernet eth2 description 'Configured by Ansible'
# set interfaces ethernet eth2 duplex 'auto'
# set interfaces ethernet eth2 mtu '1500'
# set interfaces ethernet eth2 speed 'auto'
# set interfaces ethernet eth2 vif 200 description 'VIF - 200'
#
- name: Gather listed interfaces with provided configurations
  vyos.vyos.vyos_interfaces:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
#         {
#             "description": "Configured by Ansible",
#             "duplex": "auto",
#             "enabled": true,
#             "mtu": 1500,
#             "name": "eth2",
#             "speed": "auto",
#             "vifs": [
#                 {
#                     "description": "VIF - 200",
#                     "enabled": true,
#                     "vlan_id": 200
#                 }
#             ]
#         },
#         {
#             "description": "Configured by Ansible",
#             "duplex": "auto",
#             "enabled": true,
#             "mtu": 1500,
#             "name": "eth1",
#             "speed": "auto",
#             "vifs": [
#                 {
#                     "description": "VIF - 200",
#                     "enabled": true,
#                     "vlan_id": 200
#                 }
#             ]
#         },
#         {
#             "duplex": "auto",
#             "enabled": true,
#             "name": "eth0",
#             "speed": "auto"
#         }
#     ]
#
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep interfaces
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:50:5e:19'
# set interfaces ethernet eth0 smp_affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 description 'Configured by Ansible'
# set interfaces ethernet eth1 duplex 'auto'
# set interfaces ethernet eth1 mtu '1500'
# set interfaces ethernet eth1 speed 'auto'
# set interfaces ethernet eth1 vif 200 description 'VIF - 200'
# set interfaces ethernet eth2 description 'Configured by Ansible'
# set interfaces ethernet eth2 duplex 'auto'
# set interfaces ethernet eth2 mtu '1500'
# set interfaces ethernet eth2 speed 'auto'
# set interfaces ethernet eth2 vif 200 description 'VIF - 200'


# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_interfaces:
    config:
    - name: eth0
      enabled: true
      duplex: auto
      speed: auto
    - name: eth1
      description: Configured by Ansible - Interface 1
      mtu: 1500
      speed: auto
      duplex: auto
      enabled: true
      vifs:
      - vlan_id: 100
        description: Eth1 - VIF 100
        mtu: 400
        enabled: true
      - vlan_id: 101
        description: Eth1 - VIF 101
        enabled: true
    - name: eth2
      description: Configured by Ansible - Interface 2 (ADMIN DOWN)
      mtu: 600
      enabled: false
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#         "set interfaces ethernet eth0 duplex 'auto'",
#         "set interfaces ethernet eth0 speed 'auto'",
#         "delete interfaces ethernet eth0 disable",
#         "set interfaces ethernet eth1 duplex 'auto'",
#         "delete interfaces ethernet eth1 disable",
#         "set interfaces ethernet eth1 speed 'auto'",
#         "set interfaces ethernet eth1 description 'Configured by Ansible - Interface 1'",
#         "set interfaces ethernet eth1 mtu '1500'",
#         "set interfaces ethernet eth1 vif 100 description 'Eth1 - VIF 100'",
#         "set interfaces ethernet eth1 vif 100 mtu '400'",
#         "set interfaces ethernet eth1 vif 101 description 'Eth1 - VIF 101'",
#         "set interfaces ethernet eth2 disable",
#         "set interfaces ethernet eth2 description 'Configured by Ansible - Interface 2 (ADMIN DOWN)'",
#         "set interfaces ethernet eth2 mtu '600'"
#     ]


# Using parsed
#
#
- name: Parse the configuration.
  vyos.vyos.vyos_interfaces:
    running_config:
      "set interfaces ethernet eth0 address 'dhcp'
       set interfaces ethernet eth0 duplex 'auto'
       set interfaces ethernet eth0 hw-id '08:00:27:50:5e:19'
       set interfaces ethernet eth0 smp_affinity 'auto'
       set interfaces ethernet eth0 speed 'auto'
       set interfaces ethernet eth1 description 'Configured by Ansible'
       set interfaces ethernet eth1 duplex 'auto'
       set interfaces ethernet eth1 mtu '1500'
       set interfaces ethernet eth1 speed 'auto'
       set interfaces ethernet eth1 vif 200 description 'VIF - 200'
       set interfaces ethernet eth2 description 'Configured by Ansible'
       set interfaces ethernet eth2 duplex 'auto'
       set interfaces ethernet eth2 mtu '1500'
       set interfaces ethernet eth2 speed 'auto'
       set interfaces ethernet eth2 vif 200 description 'VIF - 200'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#         {
#             "description": "Configured by Ansible",
#             "duplex": "auto",
#             "enabled": true,
#             "mtu": 1500,
#             "name": "eth2",
#             "speed": "auto",
#             "vifs": [
#                 {
#                     "description": "VIF - 200",
#                     "enabled": true,
#                     "vlan_id": 200
#                 }
#             ]
#         },
#         {
#             "description": "Configured by Ansible",
#             "duplex": "auto",
#             "enabled": true,
#             "mtu": 1500,
#             "name": "eth1",
#             "speed": "auto",
#             "vifs": [
#                 {
#                     "description": "VIF - 200",
#                     "enabled": true,
#                     "vlan_id": 200
#                 }
#             ]
#         },
#         {
#             "duplex": "auto",
#             "enabled": true,
#             "name": "eth0",
#             "speed": "auto"
#         }
#     ]


"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample:
    - 'set interfaces ethernet eth1 mtu 1200'
    - 'set interfaces ethernet eth2 vif 100 description VIF 100'
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.interfaces.interfaces import (
    InterfacesArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.interfaces.interfaces import (
    Interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]
    module = AnsibleModule(
        argument_spec=InterfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
    )

    result = Interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
