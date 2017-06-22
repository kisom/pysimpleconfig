Configurations
==============

Configurations are what's returned from the the parsers. They are instances
of `kutils.dicts.AttrDictDict <http://kutils.readthedocs.io/en/latest/dicts.html>`_,
which have the following properties in this module:

+ attempting to read a non-existent section returns an empty dictionary.
+ attempting to read a non-existent key returns an empty string.

This is because of a conscious design choice to avoid throwing exceptions for
missing sections; typically, the author handles this with ::

	def defaulted(value, default):
		if len(value) is not 0:
			return value
		return default

Otherwise, they behave exactly like ``dict``s, and can be used anywhere a ``dict``
can.