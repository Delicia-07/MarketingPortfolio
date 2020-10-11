from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)#creating instance of flask app
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')




@app.route('/<string:page_name>')
def about(page_name=None):
    return render_template(page_name)



def write_to_database(data):
    with open('Database.txt', mode='a') as database:  # we append because file already exits
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('Database.csv',newline='', mode='a') as database2:  # we append because file already exits
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_file=csv.writer(database2,delimiter=',')
        csv_file.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
          data=request.form.to_dict()
          write_to_csv(data)
          return redirect('/thankyou.html')
        except:
            return 'Did not save to .csv'
    else:
        return "submitting your details was error"



