# -*- coding: utf-8 -*-
# import pytest
import simpleconfig as sc


def test_parse():
    cfg = sc.parse("tests/example.ini")
    assert cfg is not None

    # this should fail
    assert 'enoent' not in cfg

    # validate default
    assert 'default' in cfg
    assert len(cfg.default) == 1
    assert cfg.default.version == '1.0.5'

    # validate section1
    assert 'owner' in cfg
    assert len(cfg.owner) == 2
    assert cfg.owner.name == 'John Doe'
    assert cfg.owner.organization == 'Acme Widgets Inc.'

    # validate section2
    assert 'database' in cfg
    assert len(cfg.database) == 3
    assert cfg.database.server == '192.0.2.62'
    assert cfg.database.port == '143'
    assert cfg.database.file == '"payroll.dat"'


def test_parse_string():
    config_data = """
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
    cfg = sc.parse_string(config_data)
    assert cfg is not None

    # this should fail
    assert 'enoent' not in cfg

    # validate default
    assert 'default' in cfg
    assert len(cfg.default) == 1
    assert cfg.default.version == '1.0.5'

    # validate section1
    assert 'owner' in cfg
    assert len(cfg.owner) == 2
    assert cfg.owner.name == 'John Doe'
    assert cfg.owner.organization == 'Acme Widgets Inc.'

    # validate section2
    assert 'database' in cfg
    assert len(cfg.database) == 3
    assert cfg.database.server == '192.0.2.62'
    assert cfg.database.port == '143'
    assert cfg.database.file == '"payroll.dat"'
