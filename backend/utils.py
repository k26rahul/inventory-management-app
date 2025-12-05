from functools import wraps
from flask import redirect
from flask_login import current_user


def role_required(role):
  def decorator(func):  # func -> decorated func
    @wraps(func)
    def decorated_func(*args, **kwargs):
      if current_user.is_authenticated and current_user.role == role:
        return func(*args, **kwargs)
      else:
        return redirect("/login")
    return decorated_func
  return decorator
