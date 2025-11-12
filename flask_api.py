from flask import Flask, request, jsonify, render_template

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def return_json_api():
    if request.method == "POST":
        response_with_json = {
            "args": request.args.to_dict(),
            "data": request.data.decode("utf-8"),
            "files": {k: v.filename for k, v in request.files.items()},
            "form": request.form.to_dict(),
            "headers": dict(request.headers),
            "json": request.get_json(silent=True),
            "origin": request.remote_addr,
            "url": request.url,
        }
        return jsonify(response_with_json)
    else:
        return render_template("html_form.html")

if __name__ == "__main__":
    app.run(debug=True)