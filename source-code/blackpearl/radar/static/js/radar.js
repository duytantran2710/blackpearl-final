function getDataFromServer() {
    $.ajax({
        url: '/radar',
        data: { request:1 },
        type: 'POST',
        success: function (response) {
            processResponse(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function processResponse(r) {
    var response = jQuery.parseJSON(r);
    var distance = response.distance;
    var pos = response.pos;
    var id = response.id;
    console.log(id);
   // console.log("distance: "+distance+" - position: "+pos);
    if(!isZero(distance) && !isZero(pos)) {
        if (pos < 90) {
            var x = findXLessThan90(distance, pos);
            var y = findYLessThan90(distance, pos);
        }
        if(pos == 90) {
            var x = 0;
            var y = distance;
        }
        if(pos > 90) {
            var x = findXGreaterThan90(distance, pos);
            var y = findYGreaterThan90(distance, pos);
        }
    
        if(x < 150 && x > -150 && y < 150 && x != 0 && y != 0) {
            var xPixel = getX(convertToPixel(x));
            var yPixel = getY(convertToPixel(y));
            console.log("x: "+x+" - y: "+y);
            console.log("x: "+xPixel+" px - y: "+yPixel+" px");
            displayObject(id, xPixel, yPixel);
            setPosition(id, xPixel, yPixel);
        }
    
        // console.log("x: "+x+" - y: "+y);
    }
}

function findXLessThan90(dis, pos) {
    cos = Math.cos((pos*Math.PI)/180);
    x = Math.floor(cos*dis);
    return x;
}

function findYLessThan90(dis, pos) {
    sin = Math.sin((pos*Math.PI)/180);
    y = Math.floor(sin*dis);
    return y;
}

function findXGreaterThan90(dis, pos) {
    pos = pos - 90;
    sin = Math.sin((pos*Math.PI)/180);
    x = Math.floor(sin*dis);
    return 0-x;
}

function findYGreaterThan90(dis, pos) {
    pos = pos - 90;
    cos = Math.cos((pos*Math.PI)/180);
    y = Math.floor(cos*dis);
    return y;
}

function isZero(n) {
    if(n == 0) {
        return true;
    }
    return false;
}

function convertToPixel(n) {
    return Math.floor(n*2.9);
}

function getX(x) {
    var MAX_WIDTH = 580;    // in px
    var result;
    if(x < 0) {
        result = (MAX_WIDTH/2) - Math.abs(x);
    } else if(x > 0) {
        result = (MAX_WIDTH/2) + x;
    }
    return result;
}

function getY(y) {
    var MAX_HEIGHT = 290;   // in px
    return MAX_HEIGHT - y;
}

function displayObject(id) {
    var $radar = $('#radar');
    $radar.append('<div class="object" id="'+id+'"></div>');
}

function setPosition(id, x, y) {
    var $object = $('#'+id);
    
    $object.css({
        'top':y,
        'left':x
    });
    
    $object.fadeOut(10000, function() {
        $object.remove();
    });
    
}

$('document').ready(function () {
    setInterval(getDataFromServer, 500);
})
