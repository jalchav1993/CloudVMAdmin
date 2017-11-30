import os
import requests
from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/workshop/', methods=['GET', 'POST'])
def get():
    errors = []
    results = {}
    return "test"
@app.route('/workshop/create/<wsid>')
#this uses get
def create(wsid):
    errors = []
    results = {}
    return "test"
@app.route('/workshop/update/<wsid>')
def update(wsid):
    errors = []
    results = {}
    return "test"
@app.route('/workshop/delete/<>')
def delete(wsid):
    errors = []
    results = {}
    return "test"
    
@app.route('/user/')
def get():
    errors = []
    results = {}
    return "test"
@app.route('/user/login/')
#this uses post
def login():
    errors = []
    results = {}
    return "test"
@app.route('/user/logour/')
def login():
    errors = []
    results = {}
    return "test"
@app.route('/user/create/<userid>')
def create(userid):
    errors = []
    results = {}
    return "test"
@app.route('/user/update/<userid>')
def update(userid):
    errors = []
    results = {}
    return "test"
@app.route('/user/delete/<userid>')
def delete(userid):
    errors = []
    results = {}
    return "test"
@app.route('/hardware/')
def get():
    return "test";
@app.route('/hardware/poll')
def poll():
    return "test";
@app.route('/hardware/clone_vm/<vm_id>')
def clone(vm_id):
    errors = []
    results = {}
    return "test"
@app.route('/hardware/create_vm/<vm_id>')
def create(vm_id):
    errors = []
    results = {}
    return "test"
@app.route('/hardware/update_vm/<vm_id>')
def create(vm_id):
    errors = []
    results = {}
    return "test"
@app.route('/hardware/delete_vm/<vm_id>')
def create(vm_id):
    errors = []
    results = {}
    return "test"
if __name__ == '__main__':
    app.run()
