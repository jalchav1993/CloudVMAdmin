import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/workshop/')
def get():
    errors = []
    results = {}
    return "test"
@app.route('/workshop/create/')
def create():
    errors = []
    results = {}
    return "test"
@app.route('/workshop/update/')
def update():
    errors = []
    results = {}
    return "test"
@app.route('/workshop/delete/')
def delete():
    errors = []
    results = {}
    return "test"
    
@app.route('/user/')
def get():
    errors = []
    results = {}
    return "test"
@app.route('/user/create/')
def create():
    errors = []
    results = {}
    return "test"
@app.route('/user/update/')
def update():
    errors = []
    results = {}
    return "test"
@app.route('/user/delete/')
def delete():
    errors = []
    results = {}
    return "test"
    
@app.route('/hardware/poll')
def poll():
    return "test";
@app.route('/hardware/clone_vm/')
def clone():
    errors = []
    results = {}
    return "test"
@app.route('/hardware/create_vm/')
def create():
    errors = []
    results = {}
    return "test"
@app.route('/hardware/update_vm/')
def create():
    errors = []
    results = {}
    return "test"
@app.route('/hardware/delete_vm/')
def create():
    errors = []
    results = {}
    return "test"
if __name__ == '__main__':
    app.run()
