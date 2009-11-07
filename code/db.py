#!/usr/bin/env/python

import re


class Schedule(object):
    """Possible schedule"""

    def __init__(self, operations):
        self.operations = operations

    def conflicts(self):
        """ Find possible conflicts """
        # divide in possible partitions and return the couples colliding
        confs = [(o, o1) for (o, o1) in (self.operations, self.operations)
                 if o.is_conflicting(o1)]
        return list(set(confs))

    def __str__(self):
        return "\n".join([str(o) for o in self.operations])


class Operation(object):
    regexp = re.compile(r"""(?P<action>(wu|wl|rl|rw|r|w|a|c))(?P<index>\d+)(\[(?P<object>\w+)\])?""")

    def __init__(self, operation):
        """ operator can only be read or write of course
        Possible operations are:
        - c[i] (commit)
        - a[i] (abort)
        - r_i[x] (read x)
        - w_i[x] (write on x)
        - rl_i[x], ru_i[x], put/release read lock
        - wl_i[x], wu_i[x], put/release write lock
        """
        self.s = operation
        self.op = self.parse_operation(operation)

    def __str__(self):
        return self.s

    @staticmethod
    def parse_operation(oper_str):
        return Operation.regexp.match(oper_str).groupdict()

    def is_conflicting(self, other):
        " True if the two operations are in conflict "
        return (self.op['object'] == other.op['object'])\
               and (self.op['action'] == "w" or other.op['action'] == "w")


def trans_to_op(s):
    " Takes a list of operations separated by ','"
    return map(str_to_op, s.split(','))


def str_to_op(s):
    """ Converts a string to an operation, in form 'r1x' 'w3y' """
    if len(s) == 2:
        return Operation(s[0], s[1])
    elif len(s) == 3:
        return Operation(s[0], s[1], s[2])


def herbrand(schedule):
    pass


def conflicts(schedule):
    pass
