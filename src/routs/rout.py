from src.database.database import db,Goods,Orders,Admin
from flask import Blueprint,request,jsonify
from src.database.variable import UPLOAD_FOLDER

pizza_rout = Blueprint('pizza', __name__)



# POST админ создать товар
@pizza_rout.route("/api/v1/newGood", methods=['POST']) 
def POST_admin_new_good():
    try:
        return {"message":"Ура! Боря сосямба"}, 200  
    except Exception as e:
        print(e)
        return {"message":f"Ошибка сервера"}, 500   