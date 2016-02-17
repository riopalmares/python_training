# -*- coding: utf-8 -*-

from model.group import Group


    
def test_add_group(app):
        app.group.create(Group(name="1234567890", header="efwefw", footer="wefefew"))


def test_add_empty_group(app):
        app.group.create(Group(name="", header="", footer=""))


