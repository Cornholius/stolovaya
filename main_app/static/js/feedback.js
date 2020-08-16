$(document).ready(function(){
    $("#feedback").click(function(e){
            e.preventDefault();
             data = {
                'name': $("input[name='name']").val(),
                'email': $("input[name='email']").val(),
                'subject': $("input[name='subject']").val(),
                'message': $("textarea[name='message']").val(),
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            };
            $.post('/feedback/', data);
//            console.log($('#FeedbackForm')[0]);
            $('#FeedbackForm')[0].reset();
            alert('Ваш отзыв отправлен!');
            $.modal.close();
            });
});
