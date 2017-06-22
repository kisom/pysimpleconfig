INI file format
===============

``simpleconfig`` understands INI files in the following format::

  [section_name]
  key = value

  # a comment describing the following section
  ; some ini files also use this, so it's supported too.
  [other_section]
  # this comment describes the key
  key = value

**Sections** are defined as text inside square brackets. This acts as a
namespace of sorts for the keys that follow. For example, in the above
configuration, 'key' has a different value depending on whether it refers
to 'section_name' or 'other_section'. Another example::

   [ www ]
   address = 10.137.4.28
   port = 8443
   tls = strict

   [ db ]
   address = 10.137.4.91
   port = 5432
   tls = strict

Address and port, for example, depend on whether they refer to the www server
or the db server.

If a key appears before the first section is defined, it goes into a section
called 'default'.

**Keys** are strings that name a value. They can contain any character that's
allowed in a word, but must be a single word. The parser will
trim whitespace from the ends, and will stop parsing a key on the first '='
character.

**Values** have the same restrictions as keys.

**Comments** are defined to be any line where the first non-whitespace character
is either a '#' or a ';'.