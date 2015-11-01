from django_assets import Bundle, register as asset_register

js = Bundle('jquery/dist/jquery.min.js', 'fancybox/source/jquery.fancybox.pack.js', 'main/js/ajaxForm.js', 'main/js/main.js')
css = Bundle('fancybox/source/jquery.fancybox.css')
asset_register('js_all', js)
asset_register('css_all', css)
