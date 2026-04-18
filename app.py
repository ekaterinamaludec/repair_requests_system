from flask import Flask, render_template, request, redirect, url_for
from database import add_request, get_all_requests, update_status, create_tables

app = Flask(__name__)


create_tables()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/requests')
def show_requests():
    all_requests = get_all_requests()
    return render_template('requests.html', requests=all_requests)


@app.route('/create', methods=['GET', 'POST'])
def create_request():
    if request.method == 'POST':
        equipment = request.form['equipment']
        problem = request.form['problem']
        requester = request.form['requester']

        add_request(equipment, problem, requester)

        return redirect(url_for('show_requests'))

    return render_template('create.html')


@app.route('/update/<int:request_id>/<status>')
def update(request_id, status):
    update_status(request_id, status)
    return redirect(url_for('show_requests'))


if __name__ == '__main__':
    app.run(debug=True)