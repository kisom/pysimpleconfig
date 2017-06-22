simpleconfig
============

.. image:: https://travis-ci.org/kisom/pysimpleconfig.svg?branch=master
    :target: https://travis-ci.org/kisom/pysimpleconfig

what?
-----

simpleconfig is a Python module that reads INI files into a dictionary. It
is both Python 2 and Python 3 compatible.

why?
----
I've written this code several times for a couple projects; I got sick of
copying the file over to new project directories.

how?
----

Both a ``parse`` and ``parse_string`` function are provided. The former parses
config files, and the latter parses a config file serialised into a string.

return value and example
------------------------
Both ``parse()`` and ``parse_string`` return a dictionary (see below) where each
section is a key at the top level,
and is a dictionary of key=value pairs itself. For example, given the config
file::

	>>> config = """
	# random version information
	version = 1.0.5

	; last modified 1 April 2001 by John Doe
	; example taken from wikipedia
	[owner]
	name=John Doe
	organization=Acme Widgets Inc.

	[database]
	# use IP address in case network name resolution is not working
	server=192.0.2.62
	port=143
	file="payroll.dat"
	"""

Parsing this with ``simpleconfig`` yields::

	>>> import simpleconfig as sc
	>>> cfg = sc.parse_string(config)
	>>> cfg['owner']['name']
	'John Doe'
	>>> cfg.owner.name
	'John Doe'

Note that the dictionary type returned by the parse functions is actually a
`kutils.dicts.AttrDictDict <http://kutils.readthedocs.io/en/latest/dicts.html>`_,
which is derived from the ``dict`` type and can be used wherever a ``dict`` can.

license
-------
simpleconfig is released under an ISC license.

author
------
`simpleconfig` was written by Kyle Isom <coder@kyleisom.net>.

additional
----------

The module is only tested for compatibility against Python 2.7 and
Python 3.3+. There are no guarantees (or attempts) at compatibility
with previous version of Python.

The docs are on `RTD <https://simpleconfig.readthedocs.io>`_.

The source for `simpleconfig` is online:

* `Github <https://github.com/kisom/pysimpleconfig>`_

