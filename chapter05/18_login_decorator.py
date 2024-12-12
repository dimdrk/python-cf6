# Create a dictionary about session details
user_session = {
    'is_logged_in':False
}

# Login required decorator
def login_required(func):
    def wrapper(*args, **kwargs):
        if user_session.get('is_logged_in'):
            return func(*args, **kwargs)
        else:
            print("you have to login first.")
            return None
    return wrapper

@login_required
def view_profile():
    print("Welocome to your profile.")

view_profile()

# User logins
user_session['is_logged_in'] = True

view_profile()