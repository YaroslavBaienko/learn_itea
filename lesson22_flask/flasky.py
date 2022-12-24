from flask import (
    Flask,
    request,
    make_response,
    abort,
    render_template
)

app = Flask(__name__)
app.static_folder = 'static'

# @app.route('/')
# def index():
#     user_cookie = request.headers.get('Cookie')
#     print(request.headers)
#     return f'<p>Your browser is {user_cookie}</p>'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/set/')
def set_cookie():
    response = make_response('<h1>This page carries a cookie!</h1>')
    response.set_cookie('answer', '100')
    return response


@app.route('/blog/<id>')
def get_blog(id):
    blogs = {
        '1': 'Cook blog',
        '2': 'Fitness blog',
        '3': 'Python blog'
    }
    if id not in blogs:
        abort(404)
    return f'<h1>Blog: {blogs[id]}</h1>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
