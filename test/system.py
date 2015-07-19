# -*- coding: utf-8 -*-
__author__ = 'nshahzad'

import shelly


shelly.run('multitail', ['/var/log/system.log'])
