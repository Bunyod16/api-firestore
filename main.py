from flask import Flask, request, make_response, send_file
from threading import Thread
import database
import os

app = Flask('')
@app.route('/')
def main():
    return "API DB IS LIVE!"

@app.route("/api/add_wallet", methods=['POST'])
def api_add_wallet():
    args = dict(request.args)
    response = database.add_wallet(args["wallet"], args["user_id"], args["user_name"], args["date"])
    if (response == 0):
        response = 400
    else:
        response = 200
    return make_response("ok", response)

@app.route("/api/get_wallet", methods=['GET'])
def api_get_wallet():
    args = dict(request.args)
    response = database.get_wallet(args["user_id"])
    if (not response):
        return make_response("no wallet", 400)
    return make_response(response,  200)

@app.route("/api/update_wallet", methods=['POST'])
def api_update_wallet():
    args = dict(request.args)
    response = database.update_wallet(args["wallet"], args["user_id"], args["date"])
    if (response == 0):
        return make_response("error", 400)
    else:
        return make_response("ok", 200)

@app.route('/api/csv', methods=['GET'])
def excel_export():
    database.db_clear_csv()
    database.db_export_csv()
    try:
        return send_file('./whitelist.csv', as_attachment=True)
    except:
        return make_response(404)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
