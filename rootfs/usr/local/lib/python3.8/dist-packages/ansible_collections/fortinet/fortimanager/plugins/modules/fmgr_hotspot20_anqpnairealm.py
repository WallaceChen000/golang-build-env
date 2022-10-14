#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2021 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_hotspot20_anqpnairealm
short_description: Configure network access identifier
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Frank Shen (@fshen01)
    - Hongbin Lu (@fgtdev-hblu)
notes:
    - Running in workspace locking mode is supported in this FortiManager module, the top
      level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
    - To create or update an object, use state present directive.
    - To delete an object, use state absent directive.
    - Normally, running one module can fail when a non-zero rc is returned. you can also override
      the conditions to fail or succeed with parameters rc_failed and rc_succeeded

options:
    enable_log:
        description: Enable/Disable logging for task
        required: false
        type: bool
        default: false
    proposed_method:
        description: The overridden method for the underlying Json RPC request
        required: false
        type: str
        choices:
          - update
          - set
          - add
    bypass_validation:
        description: only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters
        required: false
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock for FortiManager running in workspace mode, the value can be global and others including root
        required: false
        type: str
    workspace_locking_timeout:
        description: the maximum time in seconds to wait for other user to release the workspace lock
        required: false
        type: int
        default: 300
    state:
        description: the directive to create, update or delete an object
        type: str
        required: true
        choices:
          - present
          - absent
    rc_succeeded:
        description: the rc codes list with which the conditions to succeed will be overriden
        type: list
        required: false
    rc_failed:
        description: the rc codes list with which the conditions to fail will be overriden
        type: list
        required: false
    adom:
        description: the parameter (adom) in requested url
        type: str
        required: true
    hotspot20_anqpnairealm:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            nai-list:
                description: 'Nai-List.'
                type: list
                suboptions:
                    eap-method:
                        description: 'Eap-Method.'
                        type: list
                        suboptions:
                            auth-param:
                                description: 'Auth-Param.'
                                type: list
                                suboptions:
                                    id:
                                        type: str
                                        description: 'ID of authentication parameter.'
                                        choices:
                                            - 'non-eap-inner-auth'
                                            - 'inner-auth-eap'
                                            - 'credential'
                                            - 'tunneled-credential'
                                    index:
                                        type: int
                                        description: 'Param index.'
                                    val:
                                        type: str
                                        description: 'Value of authentication parameter.'
                                        choices:
                                            - 'eap-identity'
                                            - 'eap-md5'
                                            - 'eap-tls'
                                            - 'eap-ttls'
                                            - 'eap-peap'
                                            - 'eap-sim'
                                            - 'eap-aka'
                                            - 'eap-aka-prime'
                                            - 'non-eap-pap'
                                            - 'non-eap-chap'
                                            - 'non-eap-mschap'
                                            - 'non-eap-mschapv2'
                                            - 'cred-sim'
                                            - 'cred-usim'
                                            - 'cred-nfc'
                                            - 'cred-hardware-token'
                                            - 'cred-softoken'
                                            - 'cred-certificate'
                                            - 'cred-user-pwd'
                                            - 'cred-none'
                                            - 'cred-vendor-specific'
                                            - 'tun-cred-sim'
                                            - 'tun-cred-usim'
                                            - 'tun-cred-nfc'
                                            - 'tun-cred-hardware-token'
                                            - 'tun-cred-softoken'
                                            - 'tun-cred-certificate'
                                            - 'tun-cred-user-pwd'
                                            - 'tun-cred-anonymous'
                                            - 'tun-cred-vendor-specific'
                            index:
                                type: int
                                description: 'EAP method index.'
                            method:
                                type: str
                                description: 'EAP method type.'
                                choices:
                                    - 'eap-identity'
                                    - 'eap-md5'
                                    - 'eap-tls'
                                    - 'eap-ttls'
                                    - 'eap-peap'
                                    - 'eap-sim'
                                    - 'eap-aka'
                                    - 'eap-aka-prime'
                    encoding:
                        type: str
                        description: 'Enable/disable format in accordance with IETF RFC 4282.'
                        choices:
                            - 'disable'
                            - 'enable'
                    nai-realm:
                        type: str
                        description: 'Configure NAI realms (delimited by a semi-colon character).'
                    name:
                        type: str
                        description: 'NAI realm name.'
            name:
                type: str
                description: 'NAI realm list name.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: Configure network access identifier
      fmgr_hotspot20_anqpnairealm:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         hotspot20_anqpnairealm:
            nai-list:
              -
                  eap-method:
                    -
                        auth-param:
                          -
                              id: <value in [non-eap-inner-auth, inner-auth-eap, credential, ...]>
                              index: <value of integer>
                              val: <value in [eap-identity, eap-md5, eap-tls, ...]>
                        index: <value of integer>
                        method: <value in [eap-identity, eap-md5, eap-tls, ...]>
                  encoding: <value in [disable, enable]>
                  nai-realm: <value of string>
                  name: <value of string>
            name: <value of string>

'''

RETURN = '''
request_url:
    description: The full url requested
    returned: always
    type: str
    sample: /sys/login/user
response_code:
    description: The status of api request
    returned: always
    type: int
    sample: 0
response_message:
    description: The descriptive message of the api response
    type: str
    returned: always
    sample: OK.

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import NAPIManager
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_galaxy_version
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_parameter_bypass


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/anqp-nai-realm',
        '/pm/config/global/obj/wireless-controller/hotspot20/anqp-nai-realm'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/anqp-nai-realm/{anqp-nai-realm}',
        '/pm/config/global/obj/wireless-controller/hotspot20/anqp-nai-realm/{anqp-nai-realm}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'enable_log': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'forticloud_access_token': {
            'type': 'str',
            'required': False,
            'no_log': True
        },
        'proposed_method': {
            'type': 'str',
            'required': False,
            'choices': [
                'set',
                'update',
                'add'
            ]
        },
        'bypass_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'rc_succeeded': {
            'required': False,
            'type': 'list'
        },
        'rc_failed': {
            'required': False,
            'type': 'list'
        },
        'state': {
            'type': 'str',
            'required': True,
            'choices': [
                'present',
                'absent'
            ]
        },
        'adom': {
            'required': True,
            'type': 'str'
        },
        'hotspot20_anqpnairealm': {
            'required': False,
            'type': 'dict',
            'revision': {
                '6.0.0': True,
                '6.2.1': True,
                '6.2.3': True,
                '6.2.5': True,
                '6.4.0': True,
                '6.4.2': True,
                '6.4.5': True,
                '7.0.0': True
            },
            'options': {
                'nai-list': {
                    'required': False,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': True,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'type': 'list',
                    'options': {
                        'eap-method': {
                            'required': False,
                            'revision': {
                                '6.0.0': True,
                                '6.2.1': True,
                                '6.2.3': True,
                                '6.2.5': True,
                                '6.4.0': True,
                                '6.4.2': True,
                                '6.4.5': True,
                                '7.0.0': True
                            },
                            'type': 'list',
                            'options': {
                                'auth-param': {
                                    'required': False,
                                    'revision': {
                                        '6.0.0': True,
                                        '6.2.1': True,
                                        '6.2.3': True,
                                        '6.2.5': True,
                                        '6.4.0': True,
                                        '6.4.2': True,
                                        '6.4.5': True,
                                        '7.0.0': True
                                    },
                                    'type': 'list',
                                    'options': {
                                        'id': {
                                            'required': False,
                                            'revision': {
                                                '6.0.0': True,
                                                '6.2.1': True,
                                                '6.2.3': True,
                                                '6.2.5': True,
                                                '6.4.0': True,
                                                '6.4.2': True,
                                                '6.4.5': True,
                                                '7.0.0': True
                                            },
                                            'choices': [
                                                'non-eap-inner-auth',
                                                'inner-auth-eap',
                                                'credential',
                                                'tunneled-credential'
                                            ],
                                            'type': 'str'
                                        },
                                        'index': {
                                            'required': False,
                                            'revision': {
                                                '6.0.0': True,
                                                '6.2.1': True,
                                                '6.2.3': True,
                                                '6.2.5': True,
                                                '6.4.0': True,
                                                '6.4.2': True,
                                                '6.4.5': True,
                                                '7.0.0': True
                                            },
                                            'type': 'int'
                                        },
                                        'val': {
                                            'required': False,
                                            'revision': {
                                                '6.0.0': True,
                                                '6.2.1': True,
                                                '6.2.3': True,
                                                '6.2.5': True,
                                                '6.4.0': True,
                                                '6.4.2': True,
                                                '6.4.5': True,
                                                '7.0.0': True
                                            },
                                            'choices': [
                                                'eap-identity',
                                                'eap-md5',
                                                'eap-tls',
                                                'eap-ttls',
                                                'eap-peap',
                                                'eap-sim',
                                                'eap-aka',
                                                'eap-aka-prime',
                                                'non-eap-pap',
                                                'non-eap-chap',
                                                'non-eap-mschap',
                                                'non-eap-mschapv2',
                                                'cred-sim',
                                                'cred-usim',
                                                'cred-nfc',
                                                'cred-hardware-token',
                                                'cred-softoken',
                                                'cred-certificate',
                                                'cred-user-pwd',
                                                'cred-none',
                                                'cred-vendor-specific',
                                                'tun-cred-sim',
                                                'tun-cred-usim',
                                                'tun-cred-nfc',
                                                'tun-cred-hardware-token',
                                                'tun-cred-softoken',
                                                'tun-cred-certificate',
                                                'tun-cred-user-pwd',
                                                'tun-cred-anonymous',
                                                'tun-cred-vendor-specific'
                                            ],
                                            'type': 'str'
                                        }
                                    }
                                },
                                'index': {
                                    'required': False,
                                    'revision': {
                                        '6.0.0': True,
                                        '6.2.1': True,
                                        '6.2.3': True,
                                        '6.2.5': True,
                                        '6.4.0': True,
                                        '6.4.2': True,
                                        '6.4.5': True,
                                        '7.0.0': True
                                    },
                                    'type': 'int'
                                },
                                'method': {
                                    'required': False,
                                    'revision': {
                                        '6.0.0': True,
                                        '6.2.1': True,
                                        '6.2.3': True,
                                        '6.2.5': True,
                                        '6.4.0': True,
                                        '6.4.2': True,
                                        '6.4.5': True,
                                        '7.0.0': True
                                    },
                                    'choices': [
                                        'eap-identity',
                                        'eap-md5',
                                        'eap-tls',
                                        'eap-ttls',
                                        'eap-peap',
                                        'eap-sim',
                                        'eap-aka',
                                        'eap-aka-prime'
                                    ],
                                    'type': 'str'
                                }
                            }
                        },
                        'encoding': {
                            'required': False,
                            'revision': {
                                '6.0.0': True,
                                '6.2.1': True,
                                '6.2.3': True,
                                '6.2.5': True,
                                '6.4.0': True,
                                '6.4.2': True,
                                '6.4.5': True,
                                '7.0.0': True
                            },
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'nai-realm': {
                            'required': False,
                            'revision': {
                                '6.0.0': True,
                                '6.2.1': True,
                                '6.2.3': True,
                                '6.2.5': True,
                                '6.4.0': True,
                                '6.4.2': True,
                                '6.4.5': True,
                                '7.0.0': True
                            },
                            'type': 'str'
                        },
                        'name': {
                            'required': False,
                            'revision': {
                                '6.0.0': True,
                                '6.2.1': True,
                                '6.2.3': True,
                                '6.2.5': True,
                                '6.4.0': True,
                                '6.4.2': True,
                                '6.4.5': True,
                                '7.0.0': True
                            },
                            'type': 'str'
                        }
                    }
                },
                'name': {
                    'required': True,
                    'revision': {
                        '6.0.0': True,
                        '6.2.1': True,
                        '6.2.3': True,
                        '6.2.5': True,
                        '6.4.0': True,
                        '6.4.2': True,
                        '6.4.5': True,
                        '7.0.0': True
                    },
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'hotspot20_anqpnairealm'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        connection.set_option('enable_log', module.params['enable_log'] if 'enable_log' in module.params else False)
        connection.set_option('forticloud_access_token',
                              module.params['forticloud_access_token'] if 'forticloud_access_token' in module.params else None)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        fmgr.validate_parameters(params_validation_blob)
        fmgr.process_curd(argument_specs=module_arg_spec)
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
