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