from flask import Blueprint,Response, request
import json

from service.list_se_service import ListSEService
from util.util_encoder import UtilEncoder

app_list_se = Blueprint("app_list_se",__name__)

list_se_service = ListSEService()

@app_list_se.route('/listse')
def get_list():  # put application's code here
    #return list_se_service.list.head

    return Response(status=200,
                    response=json.dumps(list_se_service.list.head
                                        , cls=UtilEncoder), mimetype="application/json")

@app_list_se.route('/listse',methods=['POST'])
def save_kid():
    data = request.json
    return Response(status=200,response=json.dumps({"message":
                    list_se_service.add_kid(data)}),
                    mimetype="application/json")
