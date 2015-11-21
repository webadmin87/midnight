(function($){

    $(document).ready(function(){

        // Инициализация фотогалереи

        $('.photogallery').fancybox();

        // Инициализация ajax форм

        $(".ajax-form").ajaxForm();

        // Инициализация комментариев

        $('.comments-block').commentsBlock();

    });

})(jQuery);