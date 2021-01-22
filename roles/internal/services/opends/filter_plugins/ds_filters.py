"""ansible filters."""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
import json, os

# Return a logical name based on inventory file
# e.g. development (from /somepath/development.ini)
def opends_cmd(cmd_config):
   # bn = os.path.basename(inv_file)
   # return bn.split('.',1)[0]
   # d = {'x': 1, 'y': 2, 'z': 3}
   # test = ''.join(x for x in d.values())
   return ''

class FilterModule(object):
    """ansible filters."""

    def filters(self):
        return {
            'opends_cmd': opends_cmd
        }
