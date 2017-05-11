/**
 * Created by catherine on 06.04.17.
 */

var update_mo_id;
var mo_list = [];

$(document).ready(function() {
    $('.mo_name').click(function () {
        $(this).parent().children('div.mo_detail').toggle('normal');
        return false;
    });

    $('.mo_group_name').click(function(){
        $(this).parent().children('.mo_group_result').toggle();
        return false;
    });

    $('.parent_loc').click(function(){
        $(this).parent().children('li.children_loc').toggle('normal');
        return false;
    });

    $('.root_ent').click(function(){
        $(this).parent().children('ul.parent_ent').toggle('normal');
        return false;
    });

    $('.parent_ent').click(function(){
        $(this).children('.children_ent').toggle('normal');
        return false;
    });

    $('.first_letter').click(function () {
        $(this).parent().children('.types').toggle('normal');
        return false;
    });

     $('.types').click(function () {
        $(this).next('.types_result').toggle('normal');
        return false;
    });

    $('.types_mo_group_result').hover(
        function(){
             $(this).children('.check').css('visibility', 'visible');
        },
        function(){
            if ($(this).children('.check').prop("checked")) {
                $(this).children('.check').css('visibility', 'visible');
            }
            else{
                 $(this).children('.check').css('visibility', 'hidden');
            }
        });

    $('.check').click(function () {
        $(this).css('visibility', 'visible !important');

    });

    var checkboxes = document.getElementsByTagName('input');

    for (var n=0; n<checkboxes.length; n++)  {
        if (checkboxes[n].type == 'checkbox')   {
            checkboxes[n].checked = false;
        }
    }


    var i = 0;
    $(":checkbox").change(function(){
        if(this.checked){
            mo_list[i] = this.name;
            i++;
            if (i == 1){
                $('.bottom_menu').animate({'margin-bottom': 0}, 300)
            }
        }else{
            var val = this.name;
            var index = mo_list.indexOf(val);
            mo_list.splice(index, 1);
            i--;
            if (i == 0){
                $('.bottom_menu').animate({'margin-bottom': -80}, 300)
            }
        }

    });

});

function show_modal(){
    var modal = document.getElementById('myModal');
        var span = document.getElementsByClassName("close")[0];

        modal.style.display = "block";

        span.onclick = function() {
            modal.style.display = "none";
        };

        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
}

function set_alphabet() {
    $('#alph').css('color',  'black');
    $('#loc').css('color',  'cadetblue');
    $('.location_lists').css('display', 'none');
    $('.alphabet_lists').css('display', 'block');
}

function set_locations() {
    $('#loc').css('color',  'black');
    $('#alph').css('color',  'cadetblue');
    $('.alphabet_lists').css('display', 'none');
    $('.location_lists').css('display', 'block');
}

//ajax post запрос на обновление оборудования
function ajax_push_update_mo(data, url) {

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        method: "POST",
        url: url,
        data: data,
        beforeSend: function (xhr, settings) {
            $.ajaxSettings.beforeSend(xhr, settings);
        },

        success: function (json) {
            alert("Данные успешно обновлены");
        },

        error: function (xhr, errmsg, err) {
            alert("Ошибка");
        }

    });

}

//ajax get запрос на обновление оборудования
function ajax_transfer_mo(loc) {

    var data = {
            loc: loc,
            mo_list: JSON.stringify(mo_list)
        };

    $.ajax({
        url: './mo_transfer/json/',
        data: data,
        dataType: 'json',
         success : function(json) {
             $('.edit_mo').html('<p>Изменения успешно внесены </p>');
        },

        error : function(xhr,errmsg,err) {
            $('.edit_mo').html('<p>Аудитория введена не верно. Изменения не были внесены</p>');
        }
    });
    show_modal();
}


function mo_transfer() {
    var loc = document.getElementById("location_name").value;
    if(loc == ''){
        $('.edit_mo').html('<p>Укажите аудиторию!</p>');
        show_modal();

    }
    else{
        ajax_transfer_mo(loc);
    }
}
