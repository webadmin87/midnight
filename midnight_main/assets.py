from django_assets import Bundle, register as asset_register

js = Bundle('jquery/dist/jquery.min.js', 'fancybox/source/jquery.fancybox.pack.js', 'main/js/ajaxForm.js', 'main/js/comments.js', 'main/js/main.js', filters='jsmin', output='main/js/packed.min.js')
css = Bundle('fancybox/source/jquery.fancybox.css', 'main/css/comments.css', filters='cssmin', output='main/css/packed.min.css')
asset_register('js_main', js)
asset_register('css_main', css)
