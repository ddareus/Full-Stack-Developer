from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def my_home():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{email}, {subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database_2:
        email_2 = data["email"]
        subject_2 = data["subject"]
        message_2 = data["message"]
        csv_writer = csv.writer(
            database_2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email_2, subject_2, message_2])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thank_you.html')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong. Try again'
