from flask import Flask, jsonify, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data
df = pd.read_csv("data/accident_map_ready.csv")

# Clean text
df["State/UT/City"] = df["State/UT/City"].astype(str).str.strip().str.lower()
df["region_type"] = df["region_type"].astype(str).str.strip()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/locations")
def locations():
    region_type = request.args.get("type")
    data = df.copy()

    # STRICT: no mixing
    if region_type:
        data = data[data["region_type"] == region_type]

    return jsonify(data.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
