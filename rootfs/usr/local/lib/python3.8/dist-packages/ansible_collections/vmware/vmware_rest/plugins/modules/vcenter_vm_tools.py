#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by vmware_rest_code_generator.
# See: https://github.com/ansible-collections/vmware_rest_code_generator
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: vcenter_vm_tools
short_description: Update the properties of VMware Tools.
description: Update the properties of VMware Tools.
options:
  command_line_options:
    description:
    - Command line options passed to the installer to modify the installation procedure
      for Tools.
    type: str
  session_timeout:
    description:
    - 'Timeout settings for client session. '
    - 'The maximal number of seconds for the whole operation including connection
      establishment, request sending and response. '
    - The default value is 300s.
    type: float
    version_added: 2.1.0
  state:
    choices:
    - present
    - upgrade
    default: present
    description: []
    type: str
  upgrade_policy:
    choices:
    - MANUAL
    - UPGRADE_AT_POWER_CYCLE
    description:
    - The C(upgrade_policy) defines when Tools are auto-upgraded for a virtual machine.
    type: str
  vcenter_hostname:
    description:
    - The hostname or IP address of the vSphere vCenter
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_HOST) will be used instead.
    required: true
    type: str
  vcenter_password:
    description:
    - The vSphere vCenter password
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_PASSWORD) will be used instead.
    required: true
    type: str
  vcenter_rest_log_file:
    description:
    - 'You can use this optional parameter to set the location of a log file. '
    - 'This file will be used to record the HTTP REST interaction. '
    - 'The file will be stored on the host that run the module. '
    - 'If the value is not specified in the task, the value of '
    - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
    type: str
  vcenter_username:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_USER) will be used instead.
    required: true
    type: str
  vcenter_validate_certs:
    default: true
    description:
    - Allows connection when SSL certificates are not valid. Set to C(false) when
      certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_VALIDATE_CERTS) will be used instead.
    type: bool
  vm:
    description:
    - Identifier of the virtual machine. This parameter is mandatory.
    required: true
    type: str
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 0.1.0
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.2
"""

EXAMPLES = r"""
- name: Look up the VM called test_vm1 in the inventory
  register: search_result
  vmware.vmware_rest.vcenter_vm_info:
    filter_names:
    - test_vm1

- name: Collect information about a specific VM
  vmware.vmware_rest.vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info

- name: Retrive vm-tools information
  vmware.vmware_rest.vcenter_vm_tools:
    vm: '{{ test_vm1_info.id }}'

- name: Change vm-tools upgrade policy to UPGRADE_AT_POWER_CYCLE
  vmware.vmware_rest.vcenter_vm_tools:
    vm: '{{ test_vm1_info.id }}'
    upgrade_policy: UPGRADE_AT_POWER_CYCLE

- name: Change vm-tools upgrade policy to MANUAL
  vmware.vmware_rest.vcenter_vm_tools:
    vm: '{{ test_vm1_info.id }}'
    upgrade_policy: MANUAL
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Retrive vm-tools information
id:
  description: moid of the resource
  returned: On success
  sample: null
  type: dict
value:
  description: Retrive vm-tools information
  returned: On success
  sample:
    auto_update_supported: 0
    install_attempt_count: 0
    install_type: OPEN_VM_TOOLS
    run_state: RUNNING
    upgrade_policy: MANUAL
    version: '10346'
    version_number: 10346
    version_status: UNMANAGED
  type: dict
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "upgrade": {
        "query": {},
        "body": {"command_line_options": "command_line_options"},
        "path": {"vm": "vm"},
    },
    "update": {
        "query": {},
        "body": {"upgrade_policy": "upgrade_policy"},
        "path": {"vm": "vm"},
    },
}  # pylint: disable=line-too-long

import json
import socket
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
    session_timeout,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["command_line_options"] = {"type": "str"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["present", "upgrade"],
        "default": "present",
    }
    argument_spec["upgrade_policy"] = {
        "type": "str",
        "choices": ["MANUAL", "UPGRADE_AT_POWER_CYCLE"],
    }
    argument_spec["vm"] = {"required": True, "type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/tools").format(**params)


async def entry_point(module, session):

    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _update(params, session):
    payload = prepare_payload(params, PAYLOAD_FORMAT["update"])
    _url = ("https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/tools").format(**params)
    async with session.get(_url, **session_timeout(params)) as resp:
        _json = await resp.json()
        if "value" in _json:
            value = _json["value"]
        else:  # 7.0.2 and greater
            value = _json
        for k, v in value.items():
            if k in payload:
                if isinstance(payload[k], dict) and isinstance(v, dict):
                    to_delete = True
                    for _k in list(payload[k].keys()):
                        if payload[k][_k] != v.get(_k):
                            to_delete = False
                    if to_delete:
                        del payload[k]
                elif payload[k] == v:
                    del payload[k]
                elif payload[k] == {}:
                    del payload[k]

        if payload == {} or payload == {"spec": {}}:
            # Nothing has changed
            if "value" not in _json:  # 7.0.2
                _json = {"value": _json}
            _json["id"] = params.get("None")
            return await update_changed_flag(_json, resp.status, "get")
    async with session.patch(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        # e.g: content_configuration
        if not _json and resp.status == 204:
            async with session.get(_url, **session_timeout(params)) as resp_get:
                _json_get = await resp_get.json()
                if _json_get:
                    _json = _json_get

        _json["id"] = params.get("None")
        return await update_changed_flag(_json, resp.status, "update")


async def _upgrade(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["upgrade"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["upgrade"])
    subdevice_type = get_subdevice_type("/api/vcenter/vm/{vm}/tools?action=upgrade")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm/{vm}/tools?action=upgrade"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "upgrade")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
