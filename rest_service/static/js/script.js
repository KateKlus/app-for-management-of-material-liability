/**
 * Created by catherine on 06.04.17.
 */
var update_mo_id;

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

