from flask import session, redirect, url_for
from functools import wraps


def login_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if "token" not in session:
            return redirect(url_for("login.login"))
        
        return view_func(*args, **kwargs)

    return wrapper