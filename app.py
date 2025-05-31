from flask import Flask, render_template, request
from calorie_data import estimate_calories

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/estimate', methods=['POST'])
def estimate():
    food_item = request.form.get('food')
    calories = estimate_calories(food_item)
    return render_template('result.html', food=food_item, calories=calories)

if __name__ == '__main__':
    app.run(debug=True)