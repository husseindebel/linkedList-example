from flask import Flask, render_template, request
from List import List

app = Flask(__name__)

global_list = List()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        item = request.form["item"]
        global_list.add_item(item)
    return render_template("index.html", linked_list=global_list)


if __name__ == "__main__":
    app.run(debug=True, port=8000)