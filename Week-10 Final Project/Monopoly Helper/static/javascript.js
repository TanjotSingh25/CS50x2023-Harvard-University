function foo()
{
    players = 0
    var pictureList = ["",
        "/static/hat.png",
        "/static/dog.png",
        "/static/car.png",
        "/static/boat.png"];
    
    $('#piece1').change(function () {
        var val = parseInt($('#piece1').val());
        $('#player1piece').attr("src",pictureList[val]);
    });
    
    $('#piece2').change(function () {
        var val = parseInt($('#piece2').val());
        $('#player2piece').attr("src",pictureList[val]);
    });
    
    $('#piece3').change(function () {
        var val = parseInt($('#piece3').val());
        $('#player3piece').attr("src",pictureList[val]);
    });
    
    $('#piece4').change(function () {
        var val = parseInt($('#piece4').val());
        $('#player4piece').attr("src",pictureList[val]);
    });

    submitForms = function()
    {
        player_1_name = $('#player_1_name').val();
        player_2_name = $('#player_2_name').val();
        player_3_name = $('#player_3_name').val();
        player_4_name = $('#player_4_name').val();
        if((player_1_name == '') ||(player_2_name == '') ||(player_3_name == '') ||(player_4_name == ''))
        {
            alert("Enter Valid Names");
            return;
        }
        piece1 = $('#piece1').val();
        piece2 = $('#piece2').val();
        piece3 = $('#piece3').val();
        piece4 = $('#piece4').val();
        if((piece1 == piece2) || (piece1 == piece3) ||(piece1 == piece4) ||(piece2 == piece3) || (piece2 == piece4) || (piece3 == piece4))
        {
            alert('2 Players cannot have same piece');
            return;
        }
        $('#aplayers_num').val(players);
        $('#aplayer_1_name').val(player_1_name);
        $('#aplayer_2_name').val(player_2_name);
        $('#aplayer_3_name').val(player_3_name);
        $('#aplayer_4_name').val(player_4_name);
        $('#apiece1').val(piece1);
        $('#apiece2').val(piece2);
        $('#apiece3').val(piece3);
        $('#apiece4').val(piece4);
        balance = $('#balance').val();
        $('#abalance').val(balance);
        $('#allForms').submit();
    }

    var dice = 
    {
        sides: 6,
        roll: function () {
          var randomNumber = Math.floor(Math.random() * this.sides) + 1;
          return randomNumber;
        }
    }
      

    $('#placeholder').click(function () 
    {
        var result = dice.roll();
        $('#placeholder').css('font-size', '50px');
        $('#placeholder').html(result);
    });
}

function addPlayer()
    {
        players += 1;
        setClass(players);
        $('#p'+(players-1)).css('display', 'block');
    }

function removePlayer()
{
    players -= 1;
    setClass(players);
    $('#p'+(players)).css('display', 'none');
}

function setClass(players)
{
    if(players > 1)
    {
        if($('#letsPlay').hasClass('disabled'))
        {
            $('#letsPlay').removeClass('disabled');
            $('#letsPlay').addClass('active');
        }
    }
    else
    {
        if($('#letsPlay').hasClass('active'))
        {
            $('#letsPlay').removeClass('active');
            $('#letsPlay').addClass('disabled');
        }
    }
    if(players >= 4)
    {
        if($('#addPlayerBtn').hasClass('active'))
        {
            $('#addPlayerBtn').removeClass('active');
            $('#addPlayerBtn').addClass('disabled');
        } 
    }
    else
    {
        if($('#addPlayerBtn').hasClass('disabled'))
        {
            $('#addPlayerBtn').removeClass('disabled');
            $('#addPlayerBtn').addClass('active');
        }
    }

    if(players > 0)
    {
        if($('#removePlayerBtn').hasClass('disabled'))
        {
            $('#removePlayerBtn').removeClass('disabled');
            $('#removePlayerBtn').addClass('active');
        }
    }
    else
    {
        if($('#removePlayerBtn').hasClass('active'))
        {
            $('#removePlayerBtn').removeClass('active');
            $('#removePlayerBtn').addClass('disabled');
        }
    }
}

function redirect()
{
    window.location.href = "/";
}

function toggleVisibility(id)
{
    if($('.'+id).css('visibility')=='hidden')
    {
        $('.'+id).css('visibility', 'visible');
    }
    else
    {
        $('.'+id).css('visibility', 'hidden');
    }
}

function submitChoice(id)
{
    formid = "#form" + id;
    $(formid).submit();
}

function buy(id)
{
    $('#pid').val(id);
    $('#buy').submit();
}

function sell(id)
{
    $('#pid').val(id);
    $('#sell').submit();
}