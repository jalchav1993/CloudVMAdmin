from . import workshop
import json
@workshop.route("/workshop/getAllWg/")
def getAllWg():
  c = [
        {
          "worgkshop_group_name": "Workshop Group A",
          "numbreps_workshop": "2",
          "host_ip": "123.123.122.2",
          "status_s": "brightness_3",
          "workshop_description": "desc",
          "workshop_unit_list": ["Workshop Unit 1", "Workshop Unit 2"]
        },
        {
          "worgkshop_group_name": "Workshop Group B",
          "numbreps_workshop": "2",
          "host_ip": "153.134.152.5",
          "status_s": "brightness_3",
          "workshop_description": "desc",
          "workshop_unit_list": ["Workshop Unit 3", "Workshop Unit 4"]
        }
  ];
  return json.dumps(c);
@workshop.route("/workshop/getAllWu")
def getAllWu():
  c = [
        {
    	    "worgkshop_group_name": "Workshop Group A",
    	    "numbreps_workshop": "2",
    	    "host_ip": "123.123.122.2",
    	    "status_s": "brightness_3",
    	    "workshop_description": "desc",
    	    "workshop_unit_list": ["Workshop Unit 1", "Workshop Unit 2"]
        },
        {
          "worgkshop_group_name": "Workshop Group B",
          "numbreps_workshop": "2",
          "host_ip": "153.134.152.5",
          "status_s": "brightness_3",
          "workshop_description": "desc",
    	    "workshop_unit_list": ["Workshop Unit 3", "Workshop Unit 4"]
        }
      ];
@workshop.route("/workshop/clone/<workshopGroupName>")
def cloneThis(workshopGroupName):
    return ""
@workshop.route("/workshop/<ws>")
def getWorkshop(ws):
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
