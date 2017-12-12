from . import users
@users.route("/users/")
def getUser():
    return UserInteractionManager.getUser();
@users.route("/users/login")
def login():
    return UserInteractionManager.logIn();
@users.route("/users/logout")
def logout():
    return UserInteractionManager.logOut();
@users.route("/users/create")
def create():
    return UserInteractionManager.createUser();
@users.route("/users/update")
def update():
    return UserInteractionManager.updateUser();
@users.route("/users/delete")
def delete():
    return UserInteractionManager.deleteUser();

