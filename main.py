from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# define a route for the root URL
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# define an endpoint to receive user input and return chatbot response
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # get user input from the form data
    user_input = request.form['user_input']

    # TODO: add chatbot logic to generate response
    chatbot_response = "Hello, I'm a chatbot!"

    # return response in JSON format
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
