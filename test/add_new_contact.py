# -*- coding: utf-8 -*
import pytest
from fixture.application import Application
from model.contact import Contact



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


    
def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(first_name="Yaro", last_name="Korsakov", address="123 Front street, San Rafael, CA, 94903", phone="4151234567",
                            email="yaro.korsakov@test.com"))
    app.contact.go_to_homepage()
    app.session.logout()
