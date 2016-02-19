
from model.contact import Contact


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Contact(first_name = "test"))
    app.contact.modify_first_contact(Contact(first_name="MODIFIED", last_name="", address="", phone="",
                            email=""))
