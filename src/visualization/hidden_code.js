// This code hidden cell if contains: hide_code
%%html

<script>
code_show = true;

function code_display() {
    if (!code_show) {
        $('div.input').each(function (id) {
            $(this).show();
        });
        $('div.output_prompt').css('opacity', 1);
    } else {
        $('div.input').each(function (id) {
            if (id == 0 || $(this).html().indexOf('hide_code') > -1) {
                $(this).hide();
            }
        });
        $('div.output_prompt').css('opacity', 0);
    }
    ;
    code_show = !code_show;
}

$(document).ready(code_display);
</script>

<form action="javascript: code_display()">
    <input style="color: #0f0c0c; background: LightGray; opacity: 0.8;" \
    type="submit" value="Click to display or hide code cells">
</form>
