(function($){

    $.fn.commentsBlock = function() {

        return this.each(function(){

            var bl = $(this);

            var formBody = bl.find('.comments-form-body');

            var commentsList = bl.find('.comments-list');

            var form = bl.find('form');

            commentsList.on('click', '.answer-comment', function(){
                answer.apply(this);
            });

            bl.find('.cancel-answer').on('click', function(e){
                e.preventDefault();
                answerCancel.apply(this);
            })

            form.on('submit', function (e) {

                e.preventDefault();

                var data = form.serialize();

                $.post(form.attr('action'), data).done(function (data) {

                    formBody.html(data);

                    commentsList.load(form.attr('action') + "?id=" + form.find('[name="obj"]').val());

                }).fail(function (xhr, textStatus, errorThrown) {
                        formBody.html(xhr.responseText);
                });

            });

            function answer() {
                form.find('[name="parent"]').val($(this).data("id"));
                bl.find('.answer-name').html($(this).data("username"));
                bl.find('.answer-info').show();
            }

            function answerCancel() {
                form.find('[name="parent"]').val('');
                bl.find('.answer-name').html('');
                bl.find('.answer-info').hide();
            }

        });


    }

})(jQuery);