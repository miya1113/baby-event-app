from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    gender = request.form["gender"]
    birthday = datetime.strptime(request.form["birthday"], "%Y-%m-%d")

    events = {
        "お七夜": birthday + timedelta(days=7),
        "お宮参り": birthday + timedelta(days=30),
        "100日祝い（お食い初め）": birthday + timedelta(days=100),
        "ハーフバースデー": birthday + timedelta(days=182),
        "1歳の誕生日": birthday + timedelta(days=365),
    }

    event_details = {
    "お七夜": "生後7日目に赤ちゃんの名前をお披露目する日。",
    "お宮参り": "生後30日前後に神社へ参拝し、健やかな成長を祈る行事。",
    "100日祝い（お食い初め）": "一生食べ物に困らないように願う儀式。",
    "ハーフバースデー": "生後6ヶ月のお祝い。写真撮影が人気。",
    "1歳の誕生日": "一升餅や選び取りなど、地域によっていろいろな祝い方がある。",
    "初節句（男の子：5月5日）": "こどもの日。兜や鯉のぼりを飾る。",
    "初節句（女の子：3月3日）": "ひな祭り。ひな人形を飾って成長を願う日。"
}

    # 初節句（性別で分岐）
    if gender == "boy":
        events["初節句（男の子：5月5日）"] = datetime(birthday.year, 5, 5)
    else:
        events["初節句（女の子：3月3日）"] = datetime(birthday.year, 3, 3)

    return render_template("result.html", events=events, details=event_details)

if __name__ == "__main__":
    app.run(debug=True)