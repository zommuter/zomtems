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

Actually, since [almost every 256-bit number is a valid private ECDSA
key](http://bitcoin.stackexchange.com/a/21269/1137) and as such can be used
to generate a [bitcoin](https://en.wikipedia.org/wiki/Bitcoin) (or similar)
address, you can transfer a tiny amount of bitcoins to that and back to your
own (or better yet, use a multisignature transaction) such that the [Bitcoin
network](https://en.wikipedia.org/wiki/Bitcoin_network) serves as a simple
[timestamp](https://en.wikipedia.org/wiki/Timestamp).


### The problem
But what if you don't want to reveal the entire information when someone
else merely claimed knowledge of a part of your information, say of
`partial = "I'm a clever teapot"`? What about additional information obtained
or generated later? You could of course generate hashes for each line,
sentence, or even word of your information, but that means a vast amount of
hashes (and probably a larger bill by your notary) for each and every
conceivable permutation. And context is important, too, especially if the
information is split into very small chunks, how to include that?
So hashes are good, but not sufficient here.

### The solution
Let's use a [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree):
Each piece of information, from now on called _zomtem_ as motivated later on,
is individually hashed, and two or more such hashes are concatenated and
hashed again, and so on until a single hash is left for publication. Assuming
the protocol is cryptograhically secure^[`xor`ing the hashes e.g. would _not_
work since you could fake a "hash" to `xor` your claimed idea with as well...]
this is sufficient proof of knowledge of _all_ zomtems involved by revealing
the respective branches of the tree _without_ revealing what the other hashes
represent.

### Refinements
#### Salt &amp; Pepper
As hinted at e.g. [here](http://crypto.stackexchange.com/a/26660/2663), the
"sibblings" of zomtems you revealed might be guessed by a brute force attack,
especially if you broke your idea down into very short sentences. Therefore,
each zomtem should additionally be concatenated with an _individual_ key per
item. One method is described in the previously mentioned place, by defining
a global secret `k` and generating the `i`th zomtem's key as `hash(k, i)`.
Alternatively, a deterministig PRNG could be used^[This key is not exactly a
[salt](https://en.wikipedia.org/wiki/Salt_%28cryptography%29), since it's
kept secret, nor is a pepper, which would be the same for _each_ zomtem, but
the meaning should be clear nonetheless.].

#### Digital signature
However, since the unhashed zomtems need to be stored in a secure manner as
well (otherwise one cannot reproduce the Merkle tree and all effort was in
vain), using encryption is strongly recommended. And then one might just as
well use a (deterministic!) cryptographic signature instead of the
aforementioned salt-ish approach.

#### Context
As mentioned before, context may be important to store alongside the zomtem,
therefore one could for example append a string such as

```
Follows: 0xbeef
Precedes: 0xcafe
Other context: 0xfeed, 0x3ead
```

to the zomtem before hashing it into the Merkle tree, where the hex-codes
represent other zomtems' hashes (without their context-block, unless you
like recursion). Again, these can be modified via the aforementioned methods
in order to prevent premature information leakages.

## About the name
As mentioned before, a _zomtem_ denotes a piece of information, and the name
is a [portmanteau](https://en.wikipedia.org/wiki/Portmanteau) of _zommuting
item_. Determining the meaning of _zommuting_ is left as an excercise to the
reader for now, a brief explanation is denoted by
`6c22977048a0ef1771dac88ea38696610cd8511ce56c812b119247977f31da5d` (or
`7c034cdd5ff0ae45f431d9b644596c075f1cbba709474fef588a14620b942da9`)
and should be rather obvious from watching
[the `29892acefcdb5bbd2a9fb0f3ee74e1f35c20d1c1feb8d57da439064366492629`
scene](https://`624bf2865e7809510819e428fbd1978d97fc3b377353294d83b530d644b768ee`)
from `46fbdcf215fdb142ff52c30f91531116a3927f797d602017aeb4f966051cf87c`.
