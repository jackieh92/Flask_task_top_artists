from homework import app
from flask import render_template, request

# Import for Forms
from homework.forms import PhoneNumber, UserInfoForm

# Home Route
@app.route('/')
def home():
    welcome_name = "Welcome to Jackie's Top 5 Artists"
    number_one = "#1 Sofi Tukker"
    number_two = "#2 Black Keys"
    return render_template("home.html", welcome_name = welcome_name, number_one = number_one, number_two = number_two)


# Favorite Route
@app.route('/favorite', methods = ['GET', 'POST'])
def favorite():
    item_dict = {1:"Sofi Tukker", 2:"Black Keys", 3:"Emancipator", 4: "Kungs", 5: "I like random songs from many artists...the ones listed here are the artists that have made more than one song I like."}
    return render_template('favorite.html', item_dict = item_dict)


# Register Phone Number Route
@app.route('/phone', methods = ["GET", "POST"])
def phone():
    phone_number = PhoneNumber()
    if request.method == "POST" and phone_number.validate():
        first_name = phone_number.first_name.data
        last_name = phone_number.last_name.data
        area_code = phone_number.area_code.data
        number = phone_number.number.data
        print("\n", first_name, last_name, number)
    return render_template('/phone.html', phone_number = phone_number)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = UserInfoForm()
    if request.method == "POST" and form.validate():
        # Get Information
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n", username, password, email)
    return render_template('/register.html', form = form)

