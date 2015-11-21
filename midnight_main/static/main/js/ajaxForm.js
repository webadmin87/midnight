(function ($) {

    $.fn.ajaxForm = function (p) {

        p = p||{};

        var params = $.extend({

            'bodySelector': '.form-body',
            'alertSelector': '.alert',
            'alertSuccessSelector': '.alert-success',
            'alertDangerSelector': '.alert-danger'

        }, p);

        return this.each(function () {

            var bl = $(this);

            var formBody = bl.find(params.bodySelector);

            var form = bl.find('form');

            form.on('submit', function (e) {

                e.preventDefault();

                bl.find(params.alertSelector).hide();

                var data = form.serialize();

                $.post(form.attr('action'), data).done(function (data) {

                    formBody.html(data);

                    clearForm(form)

                    bl.find(params.alertSuccessSelector).show();

                }).fail(function (xhr, textStatus, errorThrown) {
                        formBody.html(xhr.responseText);
                        bl.find(params.alertDangerSelector).show();
                });

            });

        });

    }

    function clearForm(form)
    {
        form.find(':input').not(':button, :submit, :reset, :hidden, :checkbox, :radio').val('');
        form.find(':checkbox, :radio').prop('checked', false);
    }

})(jQuery);