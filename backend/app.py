from flask import Flask, render_template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

uri = "mongodb+srv://rares082001:Ruta2001@xiiidb.cymisn3.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.XIIIDB

@app.route('/')
def test():
    return 'Hello World!'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    education_list = db.Education.find()
    experience_list = db.Experience.find()
    prog_lang_list = db.Prog_Lang.find()
    return render_template('resume.html', education_list=education_list, 
                           experience_list=experience_list,
                           prog_lang_list=prog_lang_list)

@app.route('/portofolio')
def portofolio():
    return render_template('portofolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)