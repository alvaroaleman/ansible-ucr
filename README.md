# The Ansible ucr module

This module alters values in Univention Configuration Registry (UCR)

## Placement

Place this module below the library folder in your Ansible directory structure

## Options

parameter | required | default | choices | comments
--------- | -------- | ------- | ------- | ------
key       | true     |         |         | The key of the ucr setting to change
value     | true     |         |         | Desired value of the ucr key

## Sample task

```
- name: set nameserver1
  tags: dns
  ucr:
    key=nameserver1
    value=8.8.8.8
```

## Original Author

Alvaro Aleman
