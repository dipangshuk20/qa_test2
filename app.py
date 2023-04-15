from flask import Flask,render_template,redirect, url_for,request
from flask_paginate import Pagination
from google.cloud import storage
from google.oauth2 import service_account
import os,json,random


app = Flask(__name__)
app.config["SECRET_KEY"] = "50e396fd597eb96c3e7e6c027058b649786eb19d"
app.config["MONGO_URI"] = "mongodb+srv://dipangshuk20:<daas2023>@cluster0.uq1xlpk.mongodb.net/test"
import json
status="default"

import sqlite3
from flask import Flask, request, jsonify
from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client.htmls
db1d = db.db1
db2d = db.db2
#Setting DB initially 1
# 
# 
# .
#                       ***********************  Setting up models  ********************




def connect_to_database():
  connection = sqlite3.connect('checkboxes.db')
  cursor = connection.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS checkboxes (
      id INTEGER PRIMARY KEY,
      item_id INTEGER,
      is_checked INTEGER
    )
  ''')
  connection.commit()
  return connection

@app.route("/update-checkboxes", methods=["POST"])
def update_checkboxes():
    data = request.get_json()
    checkedIds = data["checkedIds"]

    # Connect to SQLite database
    conn = sqlite3.connect("checkboxes.db")
    cursor = conn.cursor()

    # Update the checkbox states in the database
    cursor.execute("DELETE FROM checkboxes")
    for checkboxId in checkedIds:
        cursor.execute("INSERT INTO checkboxes (id) VALUES (?)", (checkboxId,))
    conn.commit()
    conn.close()

    # Return a success message
    return jsonify({"message": "Checkboxes updated successfully"})
@app.route('/')
def index():

  return render_template('index.html', items=items)







#                   *******************************     Views           ***********************






g=open("new_batch_letera()next_batch_5-2.json","r")
data_db2=json.loads(g.read())
g.close()

f=open("new_batch_letera_3-2.json","r")
data=json.loads(f.read())
f.close()
h=open("new_2019_next_batch_5-2.json","r")
data_2019=json.loads(h.read())

def set_database():
    g=open("new_batch_letera()next_batch_5-2.json","r")
    data_db2=json.loads(g.read())
    g.close()
    return data_db2


done_html=[]
done=open("dobe.txt","w")


@app.route("/update_status/<id>")
def update_status(id):
    done_html.append(id)
    print("dobe")
    done.write(id)
    return redirect(url_for('serve_html'))




@app.route('/start', methods=('GET', 'POST'))
def start():
    data=set_database()
    return redirect(url_for('serve_html',data=data))
         
@app.route('/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        user = request.form['user']
        return redirect(url_for('serve'),user=user)

    return render_template('login.html')
#Just checking
##  ***************************Testing ****************************8
# pages = [
#     "<html><body><h1>Page 1</h1></body></html>",
#     "<html><body><h1>Page 2</h1></body></html>",
#     "<html><body><h1>Page 3</h1></body></html>"
# ]
# @app.route('/')
# def index_test():
#     return "Go to /serve to get started..."

@app.route('/next_test')
def next_page(pages):
    current_page = int(request.args.get('current_page', 0))
    next_page = current_page + 1
    if next_page >= len(pages):
        next_page = 0
    return render_template('index_test.html', pages=pages, current_page=next_page)

#   
########################## end of testing ####################3333
import json
@app.route("/serve", methods=('GET', 'POST'))
def serve_html():
    
    # items = [
    # { 'id': 1, 'name': 'Item 1' },
    # { 'id': 2, 'name': 'Item 2' },
    # { 'id': 3, 'name': 'Item 3' }]
    # connection = connect_to_database()
    # cursor = connection.cursor()
    # cursor.execute('SELECT item_id, is_checked FROM checkboxes')
    # checked_items = cursor.fetchall()

    # for item in items:
    #   item['is_checked'] = False
    #   for checked_item in checked_items:
    #     if item['id'] == checked_item[0]:
    #       item['is_checked'] = True 
    if request.method=='POST':
        db=request.form.get('db')
        if db=='db2':
            return redirect(url_for("db2",db=db))
        if db=='db3':
            return redirect(url_for("db3",db=db))
        your_variable=False
        ids = {obj["iden"] for obj in data}
        identifier={}
        for each in ids:
            identifier[each]={}
            identifier[each]['link']=url_for('page',id=each)
            identifier[each]['status']=status
            for obje in data:
                if obje['iden']==each:
                    name=obje['name']
                    identifier[each]['name']=name 
        return render_template("index.html",ids=identifier,your_variable=your_variable,dboption=10,done_html=done_html)#,items=items)
    return render_template("index.html",dboption=11)#,items=items)
      #return data[0]



@app.route("/update_st/<id>")
def update_st(id):
    # print(id)
    # return id
    file_n='new_2019_next_batch_5-2.json'
    handlig_up=open(file_n,'r')
    dic_till_now=json.loads(handlig_up.read())
    for obj in dic_till_now:
        if obj['iden']==id:
            obj['status']='success'
            break
            return obj['iden']
            dic_till_now['iden']['status']="success"
    new_handlig=open(file_n,'w')
    kk = str(dic_till_now)
    pretty =json.dump(kk,new_handlig)
    json.dump(new_handlig,indent=2)
    new_handlig.write('\n')
    new_handlig.close()
    return redirect(url_for('serve/<id>'))
    # handlig_up.write(dic_till_now)
    # return redirect(url_for('db3'))




# @app.route('/next_test')
# def next_page(pages):
#     current_page = int(request.args.get('current_page', 0))
#     next_page = current_page + 1
#     if next_page >= len(pages):
#         next_page = 0
#     return render_template('index_test.html', pages=pages, current_page=next_page)


current_page = 0

@app.route('/serve/<id>', methods=['GET', 'POST'])
def page(id):
    obj = next((obj for obj in data if obj["iden"] == id), None)
    if obj:
        pages=obj['html']
    else:
        return "Error: Object not found"
    if request.method=='POST':
        global current_page
        current_page = (current_page + 1) % len(pages)
        return render_template('index_test.html', pages=pages, current_page=current_page,obj=obj)

    else:
        return render_template("index_test.html",obj=obj,   pages=pages, current_page=0)
    

## @Rajdeep write js code to update the status after button is clicked on page.html so that next time when index is loaded, status of that is updated...
# def update_status(id):
#     console.log(id)
#     print(id)
#     status="success"


print(len(data_db2))
@app.route("/db2")
def db2():
    # data_db2=set_database()
    your_variable=False
    list1 = []
    print("db2")
    ids = {obj["iden"] for obj in data_db2}
    #print(ids)
    identifier={}
    for each in ids:
        identifier[each]={}
        identifier[each]['link']=url_for('page_db2',id=each)
        identifier[each]['status']=status
        # for obje in data_db2:
        #     if obje['iden']==each:
        #         """name=obje['name']
        #         identifier[each]['name']=name"""
        #         y = len(ids)
        #         print(ids)
        #         print(y)
        #         for i in range(0,y):
        #             if obje['iden']==each:
        #                     name=obje['name']
        #                     identifier[each]['name']=name   
                            
        #             i=i+10  
        # print(identifier)
    return render_template("index.html",ids=identifier,your_variable=your_variable,dboption=-1)   

                
    

    """list=[]
    listx = []
    for ids in listx:
        print(listx)
    
    
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1
    PER_PAGE = 10
    List=db2.list()
    i=(page-1)*PER_PAGE
    List1=List[i:i+5]
    pagination = Pagination(page=page,per_page=PER_PAGE, total=len(List), record_name='List')
    return render_template("retrieveFile.html",List=List1,db2=db2,form="submit It",pagination=pagination,)
        
        
        
        
    print(ids)"""
    
    

@app.route('/db2/<id>', methods=['GET', 'POST'])
def page_db2(id):
    obj = next((obj for obj in data_db2 if obj["iden"] == id), None)
    if obj:
        pages=obj['html']
    else:
        return "Error: Object not found"
    if request.method=='POST':
        global current_page
        current_page = (current_page + 1) % len(pages)
        return render_template('index_test.html', pages=pages, current_page=current_page,)

    else:
        return render_template("index_test.html",obj=obj,   pages=pages, current_page=0)
    
@app.route("/db3")
def db3():
    # data_db2=set_database()
    your_variable=False
    print("db2")
    ids = {obj["iden"] for obj in data_2019}
    identifier={}
    #print(data_2019)
    for each in ids:
        def replicate_recur(times, ids, result=None):
                    if result is None:  # create a new result if no intermediate was given
                        result = []
                    if times == 1:
                        result.append(ids)
                        result.fetch(10)
                    else:
                        result.append(ids)
                        replicate_recur(times - 1, ids, result)
                        result.fetch(10)
                        print(result)
        identifier[each]={}
        identifier[each]['link']=url_for('page_db3',id=each)
        

        # identifier[each]['status']=status
        for obje in data_2019:
            if obje['iden']==each:
                name=obje['name']
                identifier[each]['name']=name
                try:
                    if obje['status']:
                        print("hum jeet gye")
                        identifier[each]['status']='success'
                except:
                    print("kuch to gadbar hai daya")

                

    return render_template("index.html",ids=identifier,result=replicate_recur,your_variable=your_variable,dboption=-1)

#@app.route()

@app.route('/db3/<id>', methods=['GET', 'POST'])
def page_db3(id):
    obj = next((obj for obj in data_2019 if obj["iden"] == id), None)
    if obj:
        pages=obj['html']
    else:
        return "Error: Object not found"
    if request.method=='POST':
        global current_page
        current_page = (current_page + 1) % len(pages)
        return render_template('index_test.html', pages=pages, current_page=current_page,id=obj['iden'],obj=obj)

    else:
        return render_template("index_test.html",obj=obj,   pages=pages, current_page=0,id=obj['iden'])
    

"""@app.route("/db4")
def db3():
    # data_db2=set_database()
    storage_cleint = storage.Client.from_service_account_json('compfox-367313-ad58ca97af3b.json')
    def name_split(filename):
        # split the filename by underscore
        parts = filename.split('_')

        # extract the required substring
        name = parts[3][:-4]
        return name
    #client = storage.Client(Credentials=google_credentials)
    bucket_name = "regular_final_html"

    # Get a reference to the bucket
    bucket = storage_cleint.get_bucket(bucket_name)
    # List all HTML files in the bucket
    blobs = bucket.list_blobs(prefix="", delimiter="/")
    filenames = []
    dict_list = []
    keys = []
    data = {}
    for blob in blobs:
        if blob.name.endswith('.pdf'):
            name = name_split(blob.name)
            filenames.append(name)
            html_blob = bucket.blob(blob.name)
            html_contents = html_blob.download_as_string().decode("utf-8")
            my_dict = json.loads(html_contents)
            for key, value in my_dict.items():
                print(key)
                keys.append(key)
                id = random.randint(0,10000)
                data[id] = {"text": value, "filename":name}
        if len(keys) >100:
            dict_list.append(data)
            data = {}
            keys = []
    # convert the list to JSON
    json_data = json.dumps(dict_list)

    # save the JSON data to a file
    with open('db4_data.json', 'w') as f:
        f.write(json_data)
    with open('filename.txt','w') as p:
        p.write(filenames)
    print(len(filenames))
    print(len(dict_list))
    return render_template("index.html",ids=identifier,your_variable=your_variable,dboption=-1)"""