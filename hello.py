from flask import Flask
from flask import request
from flask import render_template
import pandas
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("main.html")


@app.route('/action_page', methods=['GET','POST'])
def convert():
    english_word = request.form.get('english')
   # print (english_word)
    data =pandas.read_csv("static/eng_nepali.csv")
    refined_data = data.to_dict (orient="records") ##this is a list with dictionary in it
    
    found = False
     
    for item in refined_data:
        if item['English'] == english_word:
            nepali_word=(item['Nepali'])
            found = True
            break

        if found == False:
           nepali_word="not found"
           
       
    #print(data) #checking the type of output
    # textdata=open('static/eng_nepali.csv', encoding="utf8")
    # row_data=[]
    # for line in textdata:
    #     row_data=line.strip(",").split()
    #     for i, item in enumerate(row_data):
    #         try:
    #             row_data[i]=float(item)
    #         except ValueError:
    #             pass
    #         print (row_data)
        
 

    #nepali=refined_data[English(english_word)]
    #print(nepali)
    return render_template("main.html",answer=nepali_word)