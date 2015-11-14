(function($){

    $.fn.swfBanners = function() {

        return this.each(function(){

            var bl = $(this)

            swfobject.embedSWF(
                bl.data("path"),
                bl.attr("id"),
                bl.data("width"),
                bl.data("height"),
                "9.0.0",
                "expressInstall.swf", {}, {}, {});

        });

    }

})(jQuery);