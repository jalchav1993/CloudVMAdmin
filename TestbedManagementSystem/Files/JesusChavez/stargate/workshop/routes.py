from . import workshop
@workshop.route("/workshop/<ws>")
def getWorkshops(ws):
    return WorkshopManager.getWorkshop(ws);
@workshop.route("/workshop/create/<ws>")
def create(ws):
    return WorkshopManager.createWorkshop(ws);
@workshop.route("/workshop/update/<ws>")
def update(ws):
    return WorkshopManager.updateWorkshop(ws);
@workshop.route("/workshop/delete/<ws>")
def delete(ws):
    return WorkshopManager.deleteWorkshop(ws);

