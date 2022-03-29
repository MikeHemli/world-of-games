from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/score")
def score_server():
    try:
        with open("scores.txt") as f:
            score = f.readline()
            return render_template("score.html", SCORE=" " + score)
    except BaseException as ex:
        print(ex)
        return render_template("error.html", ERROR='There was an error while loading this page...')


app.run(port=5001, debug=True)
