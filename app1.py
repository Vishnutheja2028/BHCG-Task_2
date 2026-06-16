from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()

    url = data.get("url")

    return jsonify({
        "received_url": url
    })

if __name__ == "__main__":
    app.run(debug=True)