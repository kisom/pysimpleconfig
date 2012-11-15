simpleconfig
============

why?
----
I've written this code several times for a couple projects; I got sick of
copying the file over to new project directories.

configuration file syntax
-------------------------
[section_name]
key = value

# a comment describing the following section
[other_section]
key = value

There may be as many key = value lines in a given section. Multiline values
are not supported. Anything not matching one of these patterns will raise
an IOError exception in the module. White space is not significant in section
headers (i.e. [ section1 ] is the same as [section1]) or in the key = value
pairs (i.e. key=value is the same as key = value). Keys, values, and section
names may have whitespace in them. The default section name, if none is
provided, is 'default'.

return value and example
------------------------
`parse()` returns a dictionary where each section is a key at the top level,
and is a dictionary of key=value pairs itself. For example, given the config
file:

```
# section 1 contains various Zork-related keys and values
[section1]
foo = bar
baz = quux

spam = eggs

# section 2 contains various Pinky and the Brain-related keys and values.
[section2]
zort = troz
narf = poit
```

We could parse this with `simpleconfig`:
```
>>> import simpleconfig
>>> simpleconfig.parse('test.conf')
{'section2': {'zort': 'troz', 'narf': 'poit'}, 'section1': {'foo': 'bar', 'baz': 'quux', 'spam': 'eggs'}}
```

license
-------
simpleconfig is released under an ISC license.

author
------
`simpleconfig` was written by Kyle Isom <coder@kyleisom.net>.

The source for `simpleconfig` is online:

* [Github](https://github.com/kisom/pysimpleconfig)
* [Bitbucket](https://bitbucket.org/kisom/pysimpleconfig)
