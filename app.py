from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def mlapp():
    return "first ml end to end project"

if __name__==("__main__"):
    app.run(debug=True)