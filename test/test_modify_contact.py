
from model.contact import Contact


def test_delete_first_group(app):
        app.contact.modify_first_contact(Contact(first_name="MODIFIED", last_name="", address="", phone="",
                            email=""))
