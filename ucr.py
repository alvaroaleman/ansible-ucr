#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2014. Alvaro Aleman <alvaro.aleman@agsserver.com>


DOCUMENTATION = '''
---
module: ucr
version_added: "1.8.2"
short_description: "Sets values in Univention Configuration Registry"
extends_documentation_fragment: ''
description:
  - Sets values of keys in Univention Configuration Registry
notes:
  - none
requirements: [ ]
author: Alvaro Aleman
options:
  key:
    description:
    - 'The key of the ucr setting to change'
  required: true
  value:
    description:
    - 'Desired value of the ucr key'
  required: true
  
'''

EXAMPLES = '''
- ucr: key=repository/online/unmaintained value=yes

'''

def get_value(module, key):
    ''' Find out current value '''
    return module.run_command('/usr/sbin/ucr get ' + str(key))[1][:-1] 

def set_value(module, key, value):
    ''' Set value for key '''
    return module.run_command('/usr/sbin/ucr set ' + str(key) + '="' + str(value) + '"')

def main():

    module = AnsibleModule(
        argument_spec = dict(
            key = dict(required=True, aliases=['name']),
            value = dict(required=True)
        ),
        supports_check_mode=True
    )

    key = module.params['key']
    value = module.params['value']

    old_value = get_value(module, key)

    changed = old_value != value

    if changed and not module.check_mode:
        set_value(module, key, value)

    return module.exit_json(
        changed=changed,
        key=key,
        value=value,
        old_value=old_value
    )

from ansible.module_utils.basic import *

main()

