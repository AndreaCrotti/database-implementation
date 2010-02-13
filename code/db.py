#!/usr/bin/env/python
# -*- mode: python -*-
# http://github.com/AndreaCrotti/database-implementation/blob/master/code/db.py
import re
import sqlite3

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
                    confs.append((o1, o2))
        return confs

    def is_useful(self, act1, act2):
        """ Check if act1 is useful for act2"""
        pass

    def is_alive(self, action):
        """ Check if operation is alive """
        pass

    def lrf(self):
        """ Computes live-reads-from relations """
        pass

    def read_from(self):
        """ Computes the read from relations between transactions"""
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
        """ Parse the operation given regexp """
        return Operation.regexp.match(oper_str).groupdict()

    def is_conflicting(self, other):
        " True if the two operations are in conflict "
        return (self.op['object'] == other.op['object'])\
               and (self.op['action'] == "w" or other.op['action'] == "w")



