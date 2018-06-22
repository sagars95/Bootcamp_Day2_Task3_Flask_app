import json                                                     

from flask import Flask, request                                

app = Flask(__name__)                                           

@app.route('/',methods=['GET'])                                 
def hello_world():                                              
    return 'Hello World!'                                       

@app.route('/customerupdate',methods=['GET','POST'])            
def customerupdate():                                           
    posted_file = str(request.files['document'].read(), 'utf-8')
    posted_data = json.load(request.files['datas'])             
    print(posted_file)                                          
    print(posted_data)                                          
    return '{}\n{}\n'.format(posted_file, posted_data)    