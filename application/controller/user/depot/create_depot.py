from flask import render_template, redirect, url_for
from application.models.depot import Depot
from flask_login import current_user
from flask import flash
from loguru import logger
def create_depot_get(session):
    if current_user.is_authenticated:
        if session['type'] == 1:
            return render_template("user/my_service/depot/create_depot.html")
    
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

def create_depot_post(db, session, request):
    nameDepot = request.form["nameDepot"]
    phoneNumber = request.form['phoneNumber']
    address = request.form['address']
    
    if current_user.is_authenticated:
        if session['type'] == 1:
            id_root = current_user.get_id()
            is_user = True
            
            if nameDepot and phoneNumber and address:
                new_depot = Depot( name = nameDepot, address=address, phone_num= phoneNumber, id_root = id_root, is_user= is_user)
                db.session.add(new_depot)
                db.session.commit()
                flash(message = "Bạn đã tạo kho thành công!", category = "info")
                logger.info("Add new depot")

                return render_template("user/my_service/depot/create_depot.html")
    
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))