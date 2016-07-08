from flask import Blueprint

wuxithat = Blueprint('wuxithat', __name__)

from . import views
