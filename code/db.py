#!/usr/bin/env/python

class Schedule(object):
    """Possible schedule"""
    def __init__(self, operations):
        self.operations = operations

    def conflicts(self):
        """ Find possible conflicts """
        # divide in possible partitions and return the couples colliding
        pass

class Operation(object):
    def __init__(self, obj, idx, op):
        """ operator can only be read or write of course """
        self.obj = obj
        self.idx = idx
        self.op = op

    def __str__(self):
        return self.op + "_" + str(self.idx) + "[" + self.obj + "]"

    def is_conflicting(self, other):
        " True if the two operations are in conflict "
        return (self.obj == other.obj) and (self.op == "w" or other.op == "w")

def trans_to_op(s):
    " Takes a list of operations separated by ','"
    return map(str_to_op, s.split(','))

def str_to_op(s):
    """ Converts a string to an operation, in form 'r1x' 'w3y' """
    return Operation(s[2], s[1], s[0])

def herbrand(schedule):
    """
    
    Arguments:
    - `schedule`: schedule is the list of transactions needed
    """
    pass

def conflicts(schedule):
    pass
