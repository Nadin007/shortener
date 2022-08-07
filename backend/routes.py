import random
import string
from urllib.parse import urlparse
from backend.config import HOST_NAME
from datetime import datetime as dt

from flask import Blueprint, Response, request, redirect

from backend import db
from backend.models import URLModel


def random_string(size: int = 10):
    pool = string.ascii_letters + string.digits
    return ''.join(random.choice(pool) for i in range(size))


def is_valid_url(url):
    try:
        urlparse(url)
        return True
    except ValueError:
        return False


second = Blueprint('second', __name__)


@second.route("/<id>", methods=['GET'])
def retrive(id):
    link = URLModel.query.filter_by(shortened_url=id).first_or_404()
    link.counter += 1
    link.date = dt.utcnow()
    db.session.commit()
    return redirect(link.original_url)


@second.route("/create", methods=['POST'])
def cut():
    url = request.json['url']
    if not url or not is_valid_url(url):
        return Response("Incorrect url! PLEASE check url and fill the form again.", status=400)
    link = URLModel.query.filter_by(original_url=url).first()
    if link:
        return link.shortened_url, 200
    while True:
        try:
            shortened_url = random_string()
            new_url = f'http://{HOST_NAME}/{shortened_url}'
            new_data = URLModel(original_url=url, shortened_url=shortened_url)
            db.session.add(new_data)
            db.session.commit()
            return Response(new_url, status=200)
        except Exception:
            pass
