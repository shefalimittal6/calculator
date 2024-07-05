from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
            operation_symbol = '+'
        elif operation == 'subtract':
            result = num1 - num2
            operation_symbol = '-'
        elif operation == 'multiply':
            result = num1 * num2
            operation_symbol = '*'
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Division by zero"
            result = num1 / num2
            operation_symbol = '/'

        return render_template('index.html', num1=num1, num2=num2, result=result, operation_symbol=operation_symbol)

    except ValueError:
        return "Invalid input. Please enter valid numbers."

if __name__ == '__main__':
    app.run(debug=True)
