Introduction
============

simpleconfig is a Python module for dealing with ini-style configuration files.

For example::

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
	>>> import simpleconfig as sc
	>>> cfg = sc.parse_string(config)
	>>> cfg['owner']['name']
	'John Doe'
	>>> cfg.owner.name
	'John Doe'
