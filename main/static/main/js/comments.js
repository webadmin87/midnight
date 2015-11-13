(function($){

    $.fn.commentsBlock = function() {

        return this.each(function(){

            var bl = $(this);

            var formBody = bl.find('.comments-form-body');

            var commentsList = bl.find('.comments-list');

            var form = bl.find('form');

            commentsList.on('click', '.answer-comment', function(){
                answer($(this).data("id"), $(this).data("username"));
            });

            commentsList.on('click', '.quote-comment', function(){
                answer($(this).data("id"), $(this).data("username"));
                quote($(this).data("text"));
            });

            bl.find('.cancel-answer').on('click', function(e){
                e.preventDefault();
                answerCancel.apply(this);
            })

            form.on('submit', function (e) {

                e.preventDefault();

                bl.find('.alert').hide();

                var data = form.serialize();

                $.post(form.attr('action'), data).done(function (data) {

                    formBody.html(data);

                    commentsList.load(form.attr('action') + "?id=" + form.find('[name="obj"]').val());

                    answerCancel();

                    clearForm(form);

                    bl.find('.alert-success').show();

                }).fail(function (xhr, textStatus, errorThrown) {
                        formBody.html(xhr.responseText);
                        bl.find('.alert-danger').show();
                });

            });

            function answer(id, username) {
                form.find('[name="parent"]').val(id);
                bl.find('.answer-name').html(username);
                bl.find('.answer-info').show();
            }

            function answerCancel() {
                form.find('[name="parent"]').val('');
                bl.find('.answer-name').html('');
                bl.find('.answer-info').hide();
            }

            function quote(text) {

                var txt = form.find("[name='text']");

                var val = txt.val();

                txt.val(val+'[quote]'+text+'[/quote]');

            }

            function clearForm(form)
            {
                form.find('[name="text"]').val('');
            }

        });


    }

})(jQuery);