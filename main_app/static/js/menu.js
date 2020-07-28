$(function () {
  $(".js-menu").click(function () {
  alert("hhhhhhhhhhhhhhh"),
    const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});
    $.ajax({
      url: '/' + $(this).data("id")+ '/',
      type: 'post',
      dataType: 'json',
      data: {
        'id': $(this).data("id"),
      },
       success: function(data) {
        alert("Вы добавили в корзину позицию = "+ data['name']);
        console.log(data);
    }
    });
  });
});