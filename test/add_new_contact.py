# -*- coding: utf-8 -*

from model.contact import Contact


    
def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(first_name="Yaro", last_name="Korsakov", address="123 Front street, San Rafael, CA, 94903", phone="4151234567",
                            email="yaro.korsakov@test.com"))
    app.contact.go_to_homepage()
    app.session.logout()
