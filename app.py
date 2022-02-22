from flask import Flask, render_template

app = Flask(__name__)

# Creating test for integer sq root. (Takes a value calc. sq root and say is it an integer)
def square(value):
    return (value ** 0.5).is_integer()

# placing test in Jinja environment / available in every template.
app.jinja_env.tests["square"] = square

# Simple fizzbuzz test
@app.route("/")
def test():
    title = "FizzBuzz"
    return render_template("fizzbuzz.html", title=title)