from django_assets import Bundle, register as asset_register

js = Bundle('swfobject/swfobject/swfobject.js', 'banners/js/swfBanners.js', 'banners/js/banners.js')
asset_register('js_banners', js)
