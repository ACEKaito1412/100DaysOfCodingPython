from flask import Blueprint, render_template, url_for, redirect

profile_bp = Blueprint('profile' , __name__)

@profile_bp.route('/')
def home():
    return render_template('profile.html')