# -*- coding: utf-8 -*-
__author__ = 'nshahzad'


def __output(line):
    print line


def __install_handler(cmd):
    """
    Install signal handler to pass into command
    """
    pass


class Command(object):

    REDIR = ['<', '>']

    def __init__(self, cmd, args, output=False):

        self.cmd = cmd
        self.output = output
        self.args = args or []

        self.has_redir = self._has_redir()

    def _has_redir(self):
        for a in self.args:
            for r in self.REDIR:
                if r in a:
                    return True

        return False

    def run(self):
        pass


def run(cmd, args=None, output=True):
    """
    """
    if not args:
        args = []

    _cmd = Command(cmd, args, output)
    __install_handler(_cmd)

    return _cmd.run()
