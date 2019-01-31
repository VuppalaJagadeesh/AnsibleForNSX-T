#!/usr/bin/env python
# coding=utf-8
#
# Copyright © 2015 VMware, Inc. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions
# of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.




import json
import yaml
## LOGGER
import logging
logger = logging.getLogger('chaperone_details')
hdlr = logging.FileHandler('/var/log/chaperone/ChaperoneNSXtLog.log')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(funcName)s: %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(10)


    
def main():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)  
    rc, out, err = module.run_command(['hostname', '-i'])
    logger.debug("rc-{}".format(out))
    rc1, out1, err1 = module.run_command(['whoami'])       
    logger.debug("rc-{}".format(out1))
    if rc==0:
        module.exit_json(changed=True, hostname=out.rstrip("\n"), username=out1.rstrip("\n"), msg='Got cert details')
    else:
        module.fail_json(changed=False, msg='Error getting details')        
    
    
        
    
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
