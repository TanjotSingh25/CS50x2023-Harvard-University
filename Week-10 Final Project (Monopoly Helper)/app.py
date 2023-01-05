from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///Database.db")
players = 0

color = ['red', 'green', 'blue', 'yellow']
colors = {
        'purple': '#67449e',
        'aqua': '#5ac9e4',
        'magenta': '#e843ac',
        'orange': '#ff992a',
        'red': '#e01f32',
        'yellow': '#fece00',
        'green': '#579e50',
        'blue': '#3160ae',
        'white': '#dcdcdc',
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/classic", methods=["POST", "GET"])
def classic():
    names = open("original-names.txt", "r")
    names_list = names.readlines()
    names.close()
    for i in range(len(names_list)):
        name = names_list[i].strip()
        db.execute('UPDATE listings SET name = ? WHERE pid = ?', name, i)

    return render_template("classic-monopoly.html")
    
@app.route("/play", methods=["POST", "GET"])
def play():
    player_1_name = request.form.get('aplayer_1_name')
    player_2_name = request.form.get('aplayer_2_name')
    player_3_name = request.form.get('aplayer_3_name')
    player_4_name = request.form.get('aplayer_4_name')
    piece1 = request.form.get('apiece1')
    piece2 = request.form.get('apiece2')
    piece3 = request.form.get('apiece3')
    piece4 = request.form.get('apiece4')
    balance = int(request.form.get('abalance').strip('$'))
    
    players = int(request.form.get('aplayers_num'))

    players_name = [player_1_name, player_2_name, player_3_name, player_4_name]
    pieces = ['hat', 'dog', 'car', 'boat']
    pieces_name = []
    for i in range(4):
        pieces_name.append(pieces[int(request.form.get('apiece' + str(i + 1))) - 1])

    db.execute("DROP TABLE IF EXISTS players")
    db.execute("CREATE TABLE players (id INTEGER, name TEXT, piece TEXT, balance INTEGER)")
    for i in range(players):
        db.execute("INSERT INTO players (id, name, piece, balance) VALUES(?, ?, ?, ?)", i, players_name[i], pieces_name[i], balance)
    for i in range(29):
        db.execute("UPDATE listings SET bought_by = -1 WHERE pid = ?", i)
    other_players = []
    for i in range(players):
        others = []
        for j in range(players):
            if j != i:
                others.append(players_name[j])
        other_players.append(others)
    return render_template("play.html", players_name = players_name, pieces_name = pieces_name, balance = [balance, balance, balance, balance], players = players, color = color, other_players = other_players)


@app.route("/addMoney", methods=["POST", "GET"])
def addMoney():
    amount = request.form.get('amount')
    player = request.form.get('player')
    if amount == '':
        amount = 0
    amount = int(amount)
    if amount < 0:
        return render_play("You can't add negative money")
    db.execute("UPDATE players SET balance = balance + ? WHERE id = ?", amount, player)
    return render_play()

@app.route("/removeMoney", methods=["POST", "GET"])
def removeMoney():
    amount = request.form.get('amount')
    player = request.form.get('player')
    if amount == '':
        amount = 0
    amount = int(amount)
    if amount < 0:
        amount = -amount
    db.execute("UPDATE players SET balance = balance - ? WHERE id = ?", amount, player)
    return render_play()
    
def render_play(message = ""):
    players_named = db.execute("SELECT name FROM players")
    pieces_named = db.execute("SELECT piece FROM players")
    balanced = db.execute("SELECT balance FROM players")
    players = len(players_named)
    players_name = []
    pieces_name = []
    balance = []
    for i in range(players):
        players_name.append(players_named[i]['name'])
        pieces_name.append(pieces_named[i]['piece'])
        balance.append(balanced[i]['balance'])
    other_players = []
    for i in range(players):
        others = []
        for j in range(players):
            if j != i:
                others.append(players_name[j])
        other_players.append(others)
    return render_template("play.html", message = message, players_name = players_name, pieces_name = pieces_name, balance = balance, players = players, color = color, other_players = other_players)

@app.route("/home", methods=["POST", "GET"])
def home():
    return render_play()

@app.route("/listings", methods=["POST", "GET"])
def listings():
    listings = db.execute("SELECT * FROM listings")
    del listings[0]
    white_properties = listings[22:]
    listings = listings[:22]

    return render_template("listings.html", listings = listings, colors = colors, white_properties = white_properties)

@app.route("/buy_choice", methods=["POST", "GET"])
def buy_choice():
    players_name = db.execute("SELECT name FROM players")
    players = []
    for i in range(len(players_name)):
        players.append(players_name[i]['name'])
    players_num = len(players)
    return render_template("buy_choice.html", players = players, color=color, players_num = players_num)

@app.route("/buy", methods=["POST", "GET"])
def buy():
    if request.method == "GET":
        player = request.args.get('player')

        listings = db.execute("SELECT * FROM listings")
        del listings[0]
        white_properties = listings[22:]
        listings = listings[:22]

        available_properties = []
        for property in listings:
            if property['bought_by'] == -1:
                available_properties.append(property)
        available_properties_white = []
        for property in white_properties:
            if property['bought_by'] == -1:
                available_properties_white.append(property)

        return render_template("buy.html", available_properties = available_properties, available_properties_white = available_properties_white, colors = colors, player = player)
    elif request.method == "POST":
        pid = request.form.get('pid')
        player = request.form.get('player')

        if pid == '':
            return render_play("Please select a property to buy")
        player_balance = db.execute("SELECT balance FROM players WHERE id = ?", player)[0]['balance']
        property_price = db.execute("SELECT price FROM listings WHERE pid = ?", pid)[0]['price']
        if player_balance < property_price:
            return render_play("You don't have enough money to buy this property")
        else:
            db.execute("UPDATE players SET balance = balance - ? WHERE id = ?", property_price, player)
            db.execute("UPDATE listings SET bought_by = ? WHERE pid = ?", player, pid)
            return render_play("You have successfully bought this property")

@app.route("/showProperties", methods=["POST", "GET"])
def showProperties():
    player = request.form.get('player')
    myProperties = db.execute("SELECT * FROM listings WHERE bought_by = ?", player)
    myProperties_white = []
    myProperties_not_white = []
    for property in myProperties:
        if property['color'] == 'white':
            myProperties_white.append(property)
        else:
            myProperties_not_white.append(property)
    return render_template("listings.html", listings = myProperties_not_white, colors = colors, white_properties = myProperties_white)

@app.route("/sell_choice", methods=["POST", "GET"])
def sell_choice():
    players_name = db.execute("SELECT name FROM players")
    players = []
    for i in range(len(players_name)):
        players.append(players_name[i]['name'])
    players_num = len(players)
    return render_template("sell_choice.html", players = players, color=color, players_num = players_num)

@app.route('/sell', methods=["POST", "GET"])
def sell():
    if request.method == "GET":
        player = int(request.args.get('player'))

        listings = db.execute("SELECT * FROM listings")
        del listings[0]
        white_properties = listings[22:]
        listings = listings[:22]

        my_properties = []
        for property in listings:
            if property['bought_by'] == player:
                my_properties.append(property)
        my_properties_white = []
        for property in white_properties:
            if property['bought_by'] == player:
                my_properties_white.append(property)

        return render_template("sell.html", my_properties = my_properties, my_properties_white = my_properties_white, colors = colors, player = player)
    elif request.method == "POST":
        pid = int(request.form.get('pid'))
        player = int(request.form.get('player'))

        print()
        print()
        print(pid, player)

        if pid == '':
            return render_play("Please select a property to sell")
        # if(db.execute("SELECT bought_by FROM listings WHERE pid = ?", pid)[0]['bought_by'] != player):
        #     return render_play("You don't own this property")
        mortgage_price = db.execute("SELECT mortgage FROM listings WHERE pid = ?", pid)[0]['mortgage']
        db.execute("UPDATE players SET balance = balance + ? WHERE id = ?", mortgage_price, player)
        db.execute("UPDATE listings SET bought_by = ? WHERE pid = ?", -1, pid)
        return render_play("You have successfully sold this property")

@app.route("/payRent", methods=["POST", "GET"])
def payRent():
    other_player = request.form.get('other_player')
    player = request.form.get('player')
    amount = request.form.get('amount')
    if other_player == None:
        return render_play("Please select a player to pay rent to")
    if amount == '':
        amount = 0
    amount = int(amount)
    if amount < 0:
        return render_play("You can't pay negative rent")
    db.execute("UPDATE players SET balance = balance - ? WHERE id = ?", amount, player)
    db.execute("UPDATE players SET balance = balance + ? WHERE name = ?", amount, other_player)
    return render_play("You have successfully paid rent")
    

# ----------------------------------- #

@app.route("/custom", methods=["POST", "GET"])
def custom():
    listings = db.execute("SELECT * FROM listings")
    del listings[0]
    white_properties = listings[22:]
    listings = listings[:22]

    return render_template("custom-monopoly.html", listings = listings, colors = colors, white_properties = white_properties)

@app.route("/update-names", methods=["POST", "GET"])
def update_names():
    for i in range(29):
        i = i+1
        name = request.form.get(f"prop{i}")
        db.execute("UPDATE listings SET name = ? WHERE pid = ?", name, i)
    return render_template("classic-monopoly.html")