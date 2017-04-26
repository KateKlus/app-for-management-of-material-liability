function get_mo_list(location) {
    var loc_id = location.getAttribute("name");

    $.ajax({
        url: 'get_mo_list/'+loc_id,
        dataType: 'html',
        success: function (data) {
            $('#mo_list_res').html(data);
            }
          });
    }

function get_mo_detail(mo) {
    var mo_id = mo.getAttribute("name");

    $.ajax({
        url: 'get_mo_detail/'+mo_id,
        dataType: 'html',
        success: function (data) {
            $('#mo_detail_res').html(data);
            }
          });
    }

function get_comp_detail(mo) {
    var mo_id = mo.getAttribute("name");

    $.ajax({
        url: 'get_comp_detail/'+mo_id,
        dataType: 'html',
        success: function (data) {
            $('#'+mo_id+'_detail').html(data);
            }
          });
    }

function get_monitor_detail(mo) {
    var mo_id = mo.getAttribute("name");

    $.ajax({
        url: 'get_monitor_detail/'+mo_id,
        dataType: 'html',
        success: function (data) {
            $('#'+mo_id+'mon_detail').html(data);
            }
          });
    }

function update_mo(mo_id) {
    update_mo_id = mo_id;
    var url = '../update_mo/'+mo_id;
    ajax_update_mo(mo_id, url);
}

function update_comp (mo_id) {
    update_mo_id = mo_id;
    var url = '../update_comp/'+mo_id;
    ajax_update_mo(mo_id, url);
}

function update_monitor (mo_id) {
    update_mo_id = mo_id;
    var url = '../update_monitor/'+mo_id;
    ajax_update_mo(mo_id, url);
}

function push_mo() {
    var url = '../update_mo/'+update_mo_id;

    var form = document.forms["mo_update_form"];
    var data = {
            location: form.elements["id_location"].value,
            name: form.elements["id_name"].value,
            serial: form.elements["id_serial"].value,
            contact: form.elements["id_contact"].value,
            mo_type: form.elements["id_mo_type"].value,
            note: form.elements["id_note"].value
        };

    ajax_push_update_mo(data, url);
}

function push_comp() {
    var url = '../update_comp/'+update_mo_id;

    var form = document.forms["mo_update_form"];
    var data = {
            locations: form.elements["id_locations"].options[form.elements["id_locations"].selectedIndex].value,
            name: form.elements["id_name"].value,
            serial: form.elements["id_serial"].value,
            otherserial: form.elements["id_otherserial"].value,
            users_id_tech: form.elements["id_users_id_tech"].options[form.elements["id_users_id_tech"].selectedIndex].value
        };

    ajax_push_update_mo(data, url);
}

function push_monitor() {
    var url = '../update_monitor/'+update_mo_id;

    var form = document.forms["mo_update_form"];
    var data = {
            locations: form.elements["id_locations"].options[form.elements["id_locations"].selectedIndex].value,
            name: form.elements["id_name"].value,
            serial: form.elements["id_serial"].value,
            users_id_tech: form.elements["id_users_id_tech"].options[form.elements["id_users_id_tech"].selectedIndex].value
        };

    ajax_push_update_mo(data, url);
}

//ajax post запрос на обновление оборудования
function ajax_push_update_mo(data, url){

    $.ajaxSetup({
        beforeSend: function(xhr, settings)
        {
            function getCookie(name)
            {
                var cookieValue = null;
                if (document.cookie && document.cookie != '')
                {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++)
                    {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '='))
                        {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url)))
            {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $.ajax({
        method: "POST",
        url: url,
        data: data,
        beforeSend: function(xhr, settings) {
            $.ajaxSettings.beforeSend(xhr, settings);
        },

        success : function(json) {
            alert("Данные успешно обновлены");
        },
        
        error : function(xhr,errmsg,err) {
            alert("Ошибка");
        }

        });
}

//ajax get запрос на обновление оборудования
function ajax_update_mo(mo_id, url) {
    $.ajax({
        url: url,
        data: mo_id,
        dataType: 'html',
        success: function (data) {
            $('.edit_mo').html(data);
            }
          });

    var modal = document.getElementById('myModal');
    var btn = document.getElementById("myBtn");
    var span = document.getElementsByClassName("close")[0];
        modal.style.display = "block";

    btn.onclick = function() {
        modal.style.display = "block";
    };

    span.onclick = function() {
        modal.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}