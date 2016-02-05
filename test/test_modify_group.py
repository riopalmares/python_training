
from model.group import Group


def test_delete_first_group(app):
        app.session.login(username="admin", password="secret")
        app.group.modify_first_group(Group(name="MODIFIED GROUP", header="", footer=""))
        app.session.logout()
