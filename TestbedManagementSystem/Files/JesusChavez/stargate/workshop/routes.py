from . import workshop
@users.route("/workshop/<ws>")
def getWorkshops(ws):
    return WorkshopManager.getWorkshop(ws);
@users.route("/workshop/create/<ws>")
def create(ws):
    return WorkshopManager.createWorkshop(ws);
@users.route("/workshop/update/<ws>")
def update(ws):
    return WorkshopManager.updateWorkshop(ws);
@users.route("/workshop/delete/<ws>")
def delete(ws):
    return WorkshopManager.deleteWorkshop(ws);

from . import users
