#!/usr/bin/env/python
# -*- mode: python -*-
import re
from itertools import count, groupby
# import optparse
# import sys


s0 = "w1[x] r2[x] w2[y] r1[y] w1[y] w3[x] w3[y] c1 a2"

class Schedule(object):
    """Possible schedule"""

    def __init__(self, sched_list):
        self.operations = self.parse_schedule(sched_list)
        # TODO: some function to sort operations by different parameters

    def __str__(self):
        return "\n".join([str(o) for o in self.operations])

    def get_transactions(self):
        " Returns the transactions found in the schedule"
        return set([o['index'] for o in self.operations])

    @staticmethod
    def parse_schedule(sched_list):
        "Parse a schedule which is in form \"op1 op2 op3...\""
        return [ Operation(op) for op in sched_list.split(' ') ]

    def conflicts(self):
        """ Find possible conflicts """
        # divide in possible partitions and return the couples colliding
        # TODO: Add checking for aborted transactions
        confs = []
        num_ops = len(self.operations)
        for idx in range(num_ops):
            for jdx in range(idx + 1, num_ops):
                o1, o2 = self.operations[idx], self.operations[jdx]
                if o1.is_conflicting(o2):
                    confs.append((o1,o2))
        return confs

    @staticmethod
    def herbrand(index):
        """
        Get the herbrand semantics of the schedule,
        better in a recursive way
        H_s(ri(x)) = H_s(wj(x)) and wj(x) is the last write action before ri(x)
        We must keep track of all writings, not just final value obtained
        """
        pass
    
    # Implement some possible schedulers which are CORRECT


class Operation(object):
    """ Representing a single operation """
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


