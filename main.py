
#imports
from flask import Flask, url_for, render_template, request, redirect, session, escape, make_response


#app
app = Flask(__name__)

#route index page
@app.route("/", methods=['GET', 'POST'])
def index():
    #Pressed Button
    if request.method == 'POST':
        if request.form['submit_button'] == 'Contact me!':
            print("My Email is ...")
            return render_template('index.html')
        else:
            pass #unknown
    
    #else
    elif request.method == 'GET':
        print("ERROR something went wrong")
        return render_template('index.html')
    return render_template('index.html')

#start
if __name__ == '__main__':
    app.run(port=1337, debug=True) #if website is deployed debug = False
