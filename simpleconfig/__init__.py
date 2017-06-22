"""
Load configuration files. Given the following config file:

var1 = a toplevel key in the default section

[ section1 ]
# explain the variables
var1 = something
var2 = another possibility

[ section2 ]
var1 = blah blah
...

parse() would return a dictionary:
        { 'section1': {'var1': 'something',
                       'var2': 'another possibility'},
          'section2': {'var1': 'blah blah'}}
"""

import re
import kutils.dicts as kd

VERSION = '2.0.0'


def _parse(cfg, iterator):
    """_parse is the internal parser."""
    if cfg is None:
        cfg = kd.AttrDictDict()

    current_section = "default"
    section_re = re.compile(r'^\s*\[\s*(\w+)\s*\]\s*$')
    line_re = re.compile(r'^\s*(\w+)\s*=\s*(.*)\s*$')
    comment_re = re.compile(r'^[#;].*$')
    blank_re = re.compile(r'^\s*$')

    for line in iterator:
        if blank_re.match(line):
            continue
        elif comment_re.match(line):
            continue
        elif section_re.match(line):
            section = section_re.sub(r'\1', line)
            if section != "":
                current_section = section
                cfg[current_section] = kd.AttrStrDict()
        elif line_re.match(line):
            key = line_re.sub(r'\1', line)
            val = line_re.sub(r'\2', line)
            if current_section not in cfg:
                cfg[current_section] = kd.AttrStrDict()
            if key != "":
                cfg[current_section][key] = val
        else:
            raise IOError("malformed configuration")
    return cfg


def parse(filename=None, cfg=None):
    """
    Given a filename, parse the file and return the configuration structure.
    To add to an existing configuration, pass it in with the cfg keyword.
    :type cfg: dict
    :type filename: str
    :param filename: INI-style configuration file
    :param cfg: an existing configuration or None
    :return: the parse configuration
    """

    if filename is None:
        return cfg

    with open(filename) as conf:
        return _parse(cfg, conf)


def parse_string(config_data, cfg=None):
    """
    Parse the configuration data stored in string.
    :type cfg: dict
    :type config_data: str
    :param config_data: INI-style configuration file data
    :param cfg: an existing configuration or None
    :return: the parse configuration
    """
    if config_data is None:
        return cfg

    conf = config_data.split('\n')
    return _parse(cfg, conf)
