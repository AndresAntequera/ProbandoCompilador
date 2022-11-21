from functionalities import funtions as F
from flask import Flask, render_template,request,jsonify
import jyserver.Flask as jsf

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/checkLexer',methods = ['GET','POST'])
def checkLexer():    
    if request.method == 'POST':
        text = request.form["syntax"]
        print('xd')
        syntax = F(text)
        syntax.saveTokens()
        tokens = syntax.getTokens()
    
    return jsonify(tokens)
    

if __name__ == "__main__":
    app.run(debug=True)