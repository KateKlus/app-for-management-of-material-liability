/**
 * Created by catherine on 06.04.17.
 */
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




});

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
    $.ajax({
        url: '../update_mo/'+mo_id,
        data: mo_id,
        dataType: 'html',
        success: function (data) {
            $('.edit_mo').html(data);
            }
          });
        // Get the modal
    var modal = document.getElementById('myModal');

    // Get the button that opens the modal
    var btn = document.getElementById("myBtn");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];
        modal.style.display = "block";

    // When the user clicks on the button, open the modal
    btn.onclick = function() {
        modal.style.display = "block";
    };

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    };

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

function push_update_mo(mo_pk){
    $.ajax({
        method: "POST",
        dataType: 'json',
        url: '../update_mo/'+mo_pk,
        data: $("#mo_form").serialize(),
        success: show_post,
        error: fail
        });
}

function get_mo_result(type) {
    var mo_id = mo.getAttribute("name");

    $.ajax({
        url: 'get_monitor_detail/'+mo_id,
        dataType: 'html',
        success: function (data) {
            $('#'+mo_id+'mon_detail').html(data);
            }
          });
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

