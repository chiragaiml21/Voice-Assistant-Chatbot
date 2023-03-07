$('#chat-form').submit(function(e) {
    e.preventDefault();
    $.ajax({
        url: '/chatbot',
        type: 'POST',
        data: $('#chat-form').serialize(),
        success: function(data) {
            $('#chat-messages').append('<div class="message">' + data.response + '</div>');
        }
    });
    $('#chat-form')[0].reset();
});
