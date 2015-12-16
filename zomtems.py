#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
from random import Random


class Zomtem(object):
    def __init__(self, value, encoding='utf-8'):
        if isinstance(value, str):
            value = value.encode(encoding)
        assert isinstance(value, bytes)
        self.value = value

    def __str__(self):
        return self.value.decode()

    def __len__(self):
        return 1 if self.value else 0

    @property
    def depth(self):
        return 0

    def hash(self, hashfun, rng, secret):
        return hashfun(self.value)


class Zombranch(object):
    def __init__(self, children=None, depth=1):
        self._length = 0
        self._depth = 1
        if children is None:
            self.children = [None, None]
        else:
            assert len(children) == 2
            self.children = children.copy()
        for child in self.children:
            if child:
                self._length += len(child)
                self._depth = max(self.depth, child.depth)

    @property
    def depth(self):
        return self._depth

    def __len__(self):
        return self._length

    def append(self, zomtem):
        """Sets a free child to `zomtem` if possible, returns success
        """
        if self._length < 2**(self._depth - 1):  # a subitem slot is available in child 0
            id = 0
        elif self._length < 2**self._depth:       # a subitem slot is available in child 1
            id = 1
        else:  # no subitem slot available, must increase depth
            assert self._length == 2 ** self._depth  # if it's more, we messed up
            self.children[0] = Zombranch(self.children, depth=self._depth)
            self.children[1] = zomtem
            self._depth += 1
            self._length += 1
            return True
        if isinstance(self.children[id], Zombranch):
            assert self.children[id].append(zomtem)  # shouldn't fail
        elif self.children[id]:
            assert isinstance(self.children[id], Zomtem)
            self.children[id] = Zombranch([self.children[id], zomtem], self._depth - 1)
        else:
            assert self.children[id] is None
            self.children[id] = zomtem
        self._length += 1
        return True

    def __repr__(self):
        return "[%s, %s]" % (self.children[0], self.children[1])

    def hash(self, seed=0, hashfun=hashlib.sha512, rng=None, secret=None):
        if not rng:
            rng = Random(seed)
        h = hashfun()
        for id in (0, 1):
            if self.children[id]:
                h.update(self.children[id].hash(hashfun=hashfun, rng=rng, secret=secret).digest())
        return h



if __name__ == '__main__':
    zombranch = Zombranch()
    for i in range(16):
        zombranch.append(Zomtem(str(i)))
        print(zombranch)
        print(zombranch.hash().hexdigest())
