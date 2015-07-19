# -*- coding: utf-8 -*-
__author__ = 'nshahzad'

import shelly
import unittest

class CommandTest(unittest.TestCase):

    def test_has_redir(self):
        _cmd = shelly.Command('ls', ['> /some/file'])
        self.assertTrue(_cmd._has_redir(), 'has a redirect in the args')

    def test_no_redir(self):
        _cmd = shelly.Command('ls', ['/some/file'])
        self.assertFalse(_cmd._has_redir(), 'does not have a redirect in the args')
