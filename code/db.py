#!/usr/bin/env/python


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
    locks = ['wu', 'wl', 'rl', 'rw']
    rw = ['r', 'w']
    act = ['a', 'c']

    def __init__(self, op, idx, obj=None):
        """ operator can only be read or write of course
        Possible operations are:
        - c[i] (commit)
        - a[i] (abort)
        - r_i[x] (read x)
        - w_i[x] (write on x)
        """
        if op in ('r', 'w'):
            if not(obj):
                print "error, must also give the object"
            else:
                self.obj = obj

        self.idx = idx
        self.op = op

    def __str__(self):
        if self.op in ('a', 'c'):
            return self.op + str(self.idx)
        else:
            return self.op + "_" + str(self.idx) + "[" + self.obj + "]"

    def is_conflicting(self, other):
        " True if the two operations are in conflict "
        return (self.obj == other.obj) and (self.op == "w" or other.op == "w")


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
