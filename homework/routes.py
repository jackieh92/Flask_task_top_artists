from homework import app
from flask import render_template

# Home Route
@app.route('/')
def home():
    welcome_name = "Welcome to Jackie's Top 5 Artists"
    number_one = "#1 Sofi Tukker"
    number_two = "#2 Black Keys"
    return render_template("home.html", welcome_name = welcome_name, number_one = number_one, number_two = number_two)


# Favorite Route
@app.route('/favorite', methods = ['GET', 'POST'])
def register():
    item_dict = {1:"Sofi Tukker", 2:"Black Keys", 3:"Emancipator", 4: "Kungs", 5: "I like random songs from many artists...the ones listed here are the artists that have made more than one song I like."}
    return render_template('favorite.html', item_dict = item_dict)