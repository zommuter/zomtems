---
format: markdown_github
comment: use pandoc
---


# zomtems
Zommuting Items - Proving knowledge of secrets without revealing them

## Motivation
You have some information (be it e.g. an idea, a confession or
[your bag's contents](http://crypto.stackexchange.com/q/26658/2663)) that you
want to prove having, without revealing it (yet)? For the sake of an example,
[take](http://www.rif.org/books-activities/fingerplays/im-a-little-teapot/)

```python
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
```

### Hashes
[Cryptographic Hashes](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
are your friends: Publish your information's hash (e.g.
`sha256(teapot) = ade30c62db29b887ce71c8c6a5f33fc958913e2e502c7b5a2581f474d71e405a`),
or even have it notarized, and you've got credible proof of having knowledge
of the information itself^[Or more precisely, it is highly unlikely that you'll
find another meaningful string that yields the same hash.].


### The problem
But what if you don't want to reveal the entire information when someone
else merely claimed knowledge of a part of your information, say of
`partial = "I'm a clever teapot"`? You could of course generate hashes for
each line, sentence, or even word of your information, but that means a vast
amount of hashes (and probably a larger bill by your notary) for each and
every conceivable permutation. And context is important, too, how to include
that? So hashes are good, but not sufficient here.

### The solution
