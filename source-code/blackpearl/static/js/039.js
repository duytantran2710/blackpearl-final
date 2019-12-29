/** HANDLE MOVEMENT **/
function handleMovement() {
    setMovementButtonListener('#forward-button');
    setMovementButtonListener('#backward-button');
    setMovementButtonListener('#left-button');
    setMovementButtonListener('#right-button');
    setMovementKeyPressListener();
}

function setMovementButtonListener(buttonId) {
    $(buttonId).bind('click', function (event) {
        event.preventDefault();
        var currentBtn = $(buttonId);
        var action = currentBtn.data('movement-action');
        console.log(action);
        sendMovementActionToServer(action)
    });
}

function setMovementKeyPressListener() {
    var KEY_UP = 119;
    var KEY_DOWN = 115;
    var KEY_LEFT = 97;
    var KEY_RIGHT = 100;
    $('html').keypress(function (e) {
        var key = e.keyCode;
        
        if(key == KEY_UP) {
            sendMovementActionToServer('forward');
        } else if (key == KEY_DOWN) {
            sendMovementActionToServer('backward');
        } else if (key == KEY_LEFT) {
            sendMovementActionToServer('left');
        } else if (key == KEY_RIGHT) {
            sendMovementActionToServer('right');
        }
    });
}

function sendMovementActionToServer(action) {
    $.ajax({
        url: '/movement',
        data: {action: action},
        type: 'POST',
        success: function (response) {
           //updateEventLog(response);
        },
        error: function (error) {
            console.log(error);
        }
    });
}

/* HANDLE LOG EVENT */
function updateEventLog(log) {
    log = jQuery.parseJSON(log);
    var $logSection = $('#log');
    $logSection.append('<p>'+log.logContent+'</p>');
    updateScrollbar($logSection);
}

/* scrolling log section to bottom */
function updateScrollbar(logSection) {
    logSection[0].scrollTop = logSection[0].scrollHeight;
}

$('document').ready(function () {
    handleMovement();
});
