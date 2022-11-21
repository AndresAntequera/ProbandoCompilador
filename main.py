from functionalities import funtions as F
from functionalities import validateParser
from flask import Flask, render_template,request
import jyserver.Flask as jsf

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/checkLexer',methods = ['GET','POST'])
def checkLexer():    
    result = ""
    if request.method == 'POST':
        text = request.form["syntax"]
        try:
            state = request.form["lexer"]
            if state == 'lexer':
                syntax = F(text)
                syntax.saveTokens()
                tokens = syntax.getTokens()
                result = tokens
            
            return render_template('index.html',result=result,text=text)   
        except:
            result = checkParser(text)
            
    return render_template('index.html',result=result,text=text)


def checkParser(text):    
    syntax = validateParser(text)
                
    return syntax

if __name__ == "__main__":
    app.run(debug=True)