from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Search
from . import db
from .functions import get_data, get_Citympg, get_Engine, get_Drivetrain, get_Highwaympg, get_class
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        make = request.form.get('make')
        model = request.form.get('model')
        year = request.form.get('year')
        transmission = request.form.get('transmission')
        data = get_data(make, model, year, transmission)
        cmg = get_Citympg(data)
        hmg = get_Highwaympg(data)
        drive = get_Drivetrain(data)
        engine = get_Engine(data)
        c = get_class(data)
        new_search = Search(
            make=make, model=model,
            years=year, transmission=transmission,
            cmg=cmg, hmg=hmg,
            drive=drive, engine=engine,
            c=c, user_id=current_user.id
        )
        db.session.add(new_search)
        db.session.commit()

    return render_template("home.html", user=current_user)


@views.route('/delete-search', methods=['POST'])
def delete_search():
    search = json.loads(request.data)
    searchId = search['searchId']
    search = Search.query.get(searchId)
    if search:
        if search.user_id == current_user.id:
            db.session.delete(search)
            db.session.commit()

    return jsonify({})
