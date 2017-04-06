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
    });

