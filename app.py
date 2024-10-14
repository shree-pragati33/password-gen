from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Function to generate the password
def generate_password(length, use_uppercase, use_numbers, use_symbols, exclude_duplicate, include_spaces):
    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+"
    
    if exclude_duplicate:
        characters = ''.join(set(characters))  # remove duplicate characters
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    if include_spaces:
        password = ' '.join(password[i:i + 5] for i in range(0, len(password), 5))  # add spaces every 5 characters
    
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    length = data.get('length')
    use_uppercase = data.get('uppercase')
    use_numbers = data.get('numbers')
    use_symbols = data.get('symbols')
    exclude_duplicate = data.get('exclude_duplicate')
    include_spaces = data.get('spaces')
    
    password = generate_password(length, use_uppercase, use_numbers, use_symbols, exclude_duplicate, include_spaces)
    
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
