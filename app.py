from flask import Flask, request

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
    return "Hello World"


@app.route('/report-flush', methods=['GET', 'POST'])
def report_flush():
    if request.method == 'GET':
        return "Get not supported on this page"

    # Todo: write to the database
    return "Post success", 200


if __name__ == '__main__':
    app.run()
