<div style="text-align: center">
    <h1>MONOPOLY HELPER</h1>
</div>

#### Video Demo:  https://youtu.be/i9EF54AFrgo
#### Description:

<div style="display: flex; justify-content: center">
    <img style="width:15%" src="static/logo.png">
</div>

<br>

This is a helper website for Monopoly Game. This helps you keep track of the transactions throughout the game. 
When we initially load the index webpage, we are provided with 2 game options, **Classic** and **Custom**.
Classic Monopoly option is the most common version of the game and the one everyone is most familiar with. 
Custom Monopoly allows users to change the game according to their wishes. As we know there are alot of versions of the Monopoly Game.

## Classic Monopoly

### Homepage

When we choose the classic version of the game at the start, we are directed to the main homepage. Here we are given the option to add and remove players. User can add atmost 4 players and also should have atleast 2 players to be allowed to play. The Monopoly logo on top reverts you back to the index page if you want to change your mind and want to play Custom Monopoly. When the user adds a player, they are given options to change the name of all the players (default: Player 1, Player 2 etc). User can also choose the pieces of their choice from the available options. They can also set initial balance of all the players. There are some conditions that user needs to follow to procede. These are:

* There should atleast be 2 players
* All the players names should be unique
* All the players should have unique pieces.

If all the conditions are met, clicking on lets play starts the game. Each player is given the inputed name, piece and balance displayed beautifully as RGBY cards. Under each player card there are game functionalities,

+ **Add Money**: Clicking this option displays an input form that allows you to add an amount to add to the current players balance. If submitted empty the balance remains the same. Negative values are also not accepted (because we have another option for it). Users can use this option while playing game to simulate any money the player recieves, like Pass & Go, Recieving Rent etc.
+ **Lose Money**: Clicking this option also displays its corresponding form, similar to Add Money option. Conditions are also similar to the Add Money option, no negative numbers and empty submission does nothing. This option can be used by the users to simulate paying income tax, pay Chance or Community Chest fees, Out of Jail fees etc.
+ **My Properties**: This option will redirect the user to a page that displays all the properites owned by the player. 
+ **Pay Rent**: This option displays a form with 2 input fields, one amount field and one options field with list of other players. This option allows you to pay rent to any other field, just fill the amount in the amount field and select a player to pay the rent to. After you submit the form, the rent amount is subtracted from the current players balance and is added to the selected player.

On the top of the same page is a navigation bar with the following options:

+ **Logo**: This leads the user to the index page, ending the game.
+ **Home**: This leads the user to the main homepage (current).
+ **Property List**: Clicking this leads the user to a page with all the properties cards with all the required informations such as, price, rent, rent with houses and hotels, house price and mortgage amount.
+ **Buy**: This leads the user to a page where he can buy a property.
+ **Sell**: This leads the user to a page where he can sell any property he owns.
+ **Dice**: Also on the navigation bar is a dice which can simulate a dice roll. Clicking the dice will show a random number out of 6.

### Property List

This page shows a list of all the properties cards on the board. Just like the game, these cards display all the information of the property like its name, color, price, rent, rent with houses and hotels, price of house and mortgage amount. Players can use this page to check the property details to consider if they want to buy it or not.

### Buy

This page shows a collection of all the available property cards to buy. Any property that has been bought by any player is not shown in the collection. When we click on the buy option in the navigation bar, we are first shown a list of options with players name, to allow the user to select which player is buying the property. After the player click on the property he wants to buy, he is redirected to the homepage and the selected property is added to his My Properties list and the property price is deducted from his balance. If the player doesnot have the balance to buy the property, he is redirected to the homepage with an error message saying he is short on money. Also when a player buys a property, the property becomes unavailable further on in the collection of properties.

### Sell

This page allows the player to sell any property he owns. Like Buy option, when clicked on this option, the user is directed to a page where he is given a list of players name to select who is selling thier properties. When clicked on a player name, we are shown all the properties he owns and he can select which property he wants to sell. When they click on any property, they are redirected to the homepage and the selected property is removed from their My Property list and the mortgage value is added to that players balance. 

## Custom Monopoly

On index page, when we click on Custom Monopoly option, we are directed to a collection of all the property cards similar to the Property listings page. But here you are given the ability to change the names of all the properties. When done, clicking the submit page will redirect you to the same homepage with the updated list of properties.



 > There are a lot of other features of this game that I have not added correctly or fully, like mortgage and chance, community chest cards, Pass & Go, Income Tax, Jail etc. I didnt think of the number of these features when I started this project, so this is the version 1 of this project. But even in this version all the rules can be followed with some extra steps, like chance cards which gives players some reward cash or fines, that can be implemented with add or remove money feature.

## *Future versions plans*

+ Add mortgage funtionality properly and correctly
+ Update the paying rent functionality, where we can click on the property listing and rent can be paid.
+ Add more customizing options.
+ Add Chance and Comunity chest cards functionality which gives you a random card.
+ Make dice roll better with 2 dices.
+ Add functionality to buy and sell houses and hotels.