from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Dummy data for charts and table
    donut_data = [40, 30, 30]
    donut_labels = ["Math", "Science", "English"]
    bar_labels = ["Math", "Science", "English"]
    bar_data = [80, 70, 90]
    students = [
        {"name": "Alice", "subject": "Math"},
        {"name": "Bob", "subject": "Science"},
        {"name": "Charlie", "subject": "English"},
        {"name": "David", "subject": "Math"},
        {"name": "Eva", "subject": "Science"}
    ]
    return render_template('dashboard.html',
                           donut_data=donut_data,
                           donut_labels=donut_labels,
                           bar_labels=bar_labels,
                           bar_data=bar_data,
                           students=students)

if __name__ == '__main__':
    app.run(debug=True)
