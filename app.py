from flask import Flask, render_template, request
import joblib

model = joblib.load(r"Model\dtc.lb")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/project', methods=['GET', 'POST'])
def predict():

    prediction = None

    if request.method == "POST":

        income = float(request.form['income'])
        credit_score = int(request.form['credit_score'])
        loan_amount = float(request.form['loan_amount'])
        years_employed = int(request.form['years_employed'])
        points = float(request.form['points'])

        data = [[
            income,
            credit_score,
            loan_amount,
            years_employed,
            points
        ]]

        pred = model.predict(data)

        if pred[0] == 1:
            prediction = "Loan Approved ✅"
        else:
            prediction = "Loan Rejected ❌"

    return render_template(
        "project.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)