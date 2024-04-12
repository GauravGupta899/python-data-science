from flask import Flask, render_template , request
from database import User, Message , get_db ,save_to_db
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add/user', methods=['GET', 'POST'])
def add_user():
    status = None
    if request.method == "POST":
        name = request.form.get('uname')
        email = request.form.get('email')
        password = request.form.get('pwd')
        if name and email and password:
            u = User(name = name , email=email, password=password)
            try:
                save_to_db(u)
                status ="User added successfully"
            except Exception as e:
                status= f"Error: {e}" 
        else:
            status = "Please fill all the fields"
                        
    return render_template('add_user.html', status=status)
    pass 
    

@app.route('/add/message', methods=['GET', 'POST'])
def add_message():
        status= None
        if request.method == "POST":
           user_id = request.form.get('user_id')
           message= request.form.get('message')
        
           if user_id and message:
              
              u = Message(user_id= user_id , message= message)
              try:
                  save_to_db(u)
                  status ="Message added successfully"
              except Exception as e:
                status= f"Error: {e}" 
           else:
               
               status = "Please fill all the fields"
                        
        return render_template('add_message.html',status=status)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 