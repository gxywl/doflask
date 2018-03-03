from flask import Blueprint

from app.models import Permission

main=Blueprint('main',__name__)

@main.app_context_processor
def inject_permissions():
    return  dict(Perimission=Permission)

from . import views, errors