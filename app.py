from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
from forms import MyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
csrf = CSRFProtect(app)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = MyForm()  # Instantiate your WTForm
    if request.method == 'POST':
        # Extract data from the form
        name = request.form['name']
        student_number = request.form['student_number']
        email = request.form['email']
        course_grades = request.form['course_grades']
        satisfaction = request.form['satisfaction']
        improvements = request.form['improvements']

        # Save the data to a text file
        with open('form_data.txt', 'a') as file:  # Open file in append mode
            file.write(f"Name: {name}\n")
            file.write(f"Student Number: {student_number}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Course Grades: {course_grades}\n")
            file.write(f"Satisfaction: {satisfaction}\n")
            file.write(f"Improvements: {improvements}\n\n")

        return jsonify({'message': 'Form submitted successfully'})
    else:
        return render_template('data_collection.html', form=form)


# Define Flask Routes

if __name__ == '__main__':
    app.run(debug=True)
