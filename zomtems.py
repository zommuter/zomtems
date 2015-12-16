#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
from random import Random


class Zomtem(object):
    def __init__(self, value):
        assert isinstance(value, str)
        self.value = value

    def __str__(self):
        return self.value

    def __len__(self):
        return 1 if self.value else 0

    @property
    def depth(self):
        return 0


class Zombranch(object):
    def __init__(self, children=None, depth=1):
        self.length = 0
        self._depth = 1
        if children is None:
            self.children = [None, None]
        else:
            assert len(children) == 2
            self.children = children.copy()
        for child in self.children:
            if child:
                self.length += len(child)
                self._depth = max(self.depth, child.depth)

    @property
    def depth(self):
        return self._depth

    def append(self, zomtem):
        """Sets a free child to `zomtem` if possible, returns success
        """
        if self.length < 2**(self._depth - 1):  # a subitem slot is available in child 0
            id = 0
        elif self.length < 2**self._depth:       # a subitem slot is available in child 1
            id = 1
        else:  # no subitem slot available, must increase depth
            assert self.length == 2**self._depth  # if it's more, we messed up
            self.children[0] = Zombranch(self.children, depth=self._depth)
            self.children[1] = zomtem
            self._depth += 1
            self.length += 1
            return True
        if isinstance(self.children[id], Zombranch):
            assert self.children[id].append(zomtem)  # shouldn't fail
            self.length += 1
            return True
        elif self.children[id]:
            assert isinstance(self.children[id], Zomtem)
            self.children[id] = Zombranch([self.children[id], zomtem], self._depth - 1)
            self.length += 1
            return True
        else:
            assert self.children[id] is None
            self.children[id] = zomtem
            self.length += 1
            return True

    def __repr__(self):
        return "%s" % [str(child) for child in self.children]


class Zomtree(object):
    def __init__(self, seed=0):
        self.rnd = Random(seed)
        self.base = Zombranch()

    def append(self, zomtem):
        assert self.base.append(zomtem)

    def __repr__(self):
        return repr(self.base)


if __name__ == '__main__':
    zomtree = Zomtree()
    for i in range(16):
        zomtree.append(Zomtem(str(i)))
        print(zomtree)
