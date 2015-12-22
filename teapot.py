#!/usr/bin/python
# -*- coding: utf-8 -*-

teapot = """I'm a little teapot short and stout.
Here is my handle.
Here is my spout.
When I get all steamed up,
Hear me shout!
Just tip me over
And pour me out

I'm a clever teapot, yes it's true.
Here's an example of what I can do.
I can turn my handle to a spout.
Just tip me over and pour me out"""

from hashlib import sha256


print(teapot)
print(sha256(teapot.encode()).hexdigest())
