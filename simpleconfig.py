"""
Load configuration files. Given the following config file:

[ section1 ]
# explain the variables
var1 = something
var2 = another possibility

[section2 ]
var1 = blah blah
...

parse() would return a dictionary:
        { 'section1': {'var1': 'something',
                       'var2': 'another possibility'},
          'section2': {'var1': 'blah blah'}}
"""

import re


def parse(filename=None, cfg=None):
    """
    Given a filename, parse the file and return the configuration structure.
    To add to an existing configuration, pass it in with the cfg keyword.
    """

    if filename is None:
        return cfg
    elif cfg is None:
        cfg = {}

    section_re = re.compile(r'^\s*\[\s*(\w+)\s*\]\s*$')
    line_re = re.compile(r'^\s*(\w+)\s*=\s*(.*)\s*$')
    comment_re = re.compile(r'^#.*$')
    blank_re = re.compile('^\s*$')

    current_section = "default"

    with open(filename) as conf:
        for line in conf:
            if blank_re.match(line):
                continue
            elif comment_re.match(line):
                continue
            elif section_re.match(line):
                section = section_re.sub(r'\1', line)
                if not section == "":
                    current_section = section
                    cfg[current_section] = {}
            elif line_re.match(line):
                key = line_re.sub(r'\1', line)
                val = line_re.sub(r'\2', line)
                if not key == "":
                    cfg[current_section][key] = val
            else:
                raise IOError("invalid configuration file")
    return cfg
