server
	{
		listen 80;
		#listen [::]:80;
		listen 443;
		server_name {$target} www.{$target};
		index index.html index.htm index.php default.html default.htm default.php;
		root  /home/wwwroot/{$target};
		
		ssl on;
		ssl_certificate /root/{$target_crt_file_name}.crt;
		ssl_certificate_key /root/myserver.key;

		location / {
			proxy_pass {$http_type}://{$domain}/;
			subs_filter 'www.{$domain}' '{$target}' gi;
			subs_filter '{$domain}' '{$target}' gi;
			subs_filter 'll.sdk-1.1.js' '';
			subs_filter '<a href="http://www.shopify.com" target="_blank">Ecommerce Software by Shopify</a>' '';
			subs_filter 'UOI Boutique' 'TheCloudOutlet Boutique';
			subs_filter '<div id="follow-us">' '<div id="follow-us" style="display:none;">';
			subs_filter '<li class="icons">' '<li class="icons" style="display:none;">';
			subs_filter '<li><a href="https://itunes.apple.com/us/app/uoi-online-mobile/id911280917?mt=8&uo=4">iPhone App</a></li>' '<li><a href="/pages/privacy-policy">Privacy Policy</a></li>';
			subs_filter '<li><a href="https://play.google.com/store/apps/details?id=com.shopgate.android.app13546">Android App</a></li>' '<li><a href="/pages/faqs">FAQs</a></li>';
			subs_filter '<li><a href="/blogs/news">Blog</a></li>' '';
			subs_filter '<li><a href="https://itunes.apple.com/us/app/uoi-online-mobile/id911280917?mt=8&uo=4" title="">iPhone App</a></li>' '<li><a href="/pages/privacy-policy">Privacy Policy</a></li>';
			subs_filter '<img src="//cdn.shopify.com/s/files/1/0194/1577/files/Rep_Search_Page_6e5157fc-d2d0-42a1-833f-6f9f6ae990fe.jpg?27862" />' '<img src="//cdn.shopify.com/s/files/1/0194/1577/files/Rep_Search_Page_6e5157fc-d2d0-42a1-833f-6f9f6ae990fe.jpg?27862" style="display:none;" />';
			subs_filter '<li><a href="https://play.google.com/store/apps/details?id=com.shopgate.android.app13546" title="">Android App</a></li>' '<li><a href="/pages/uoi-rewards">Rewards</a></li>';
			subs_filter '<input type="submit" name="checkout" id="checkout" value="Checkout" class="button" />' '';
			subs_filter 'fill out the form below.' 'please Email us at TheCloudOutletonlinereps@gmail.com';
			subs_filter '<iframe src="https://docs.google.com/forms/d/1aKkXdwk_v4FGCq3wNrnNJIVwh7osGHNy7rY0O2sN3bY/viewform?embedded=true" ' '<iframe src="https://docs.google.com/forms/d/1aKkXdwk_v4FGCq3wNrnNJIVwh7osGHNy7rY0O2sN3bY/viewform?embedded=true" style="display:none;" ';
			subs_filter 'UOI' 'TheCloudOutlet';
			subs_filter 'uoi' 'thecloudoutlet';
			
			subs_filter '//cdn.shopify.com/s/files/1/0194/1577/t/14/assets/logo.png' 'http://{$target}/iimages/logo.png';
			subs_filter '//cdn.shopify.com/s/files/1/0194/1577/t/14/assets/favicon.png' 'http://{$target}/iimages/favicon.png';
			subs_filter '//cdn.shopify.com/s/files/1/0194/1577/files/Holiday_Return_Policy_FINAL.png' 'http://{$target}/iimages/Holiday_Return_Policy_FINAL.png';
			subs_filter '//cdn.shopify.com/s/files/1/0194/1577/files/Contact-Us-Page_01.jpg' 'http://{$target}/iimages/Contact-Us-Page_01.jpg';
			subs_filter '<a href="/cart">' '<a href="https://{$target}/cart">';
			
			subs_filter '<p><a title="Follow us on Facebook!" target="_blank" href="https://www.facebook.com/TheCloudOutlet.UrbanOutlet.Inc"> <img src="//cdn.shopify.com/s/files/1/0194/1577/files/Contact-Us-Page_02.jpg?27793" /></a><a title="Follow us on Instagram!" target="_blank" href="//instagram.com/thecloudoutletonline"><img src="//cdn.shopify.com/s/files/1/0194/1577/files/Contact-Us-Page_03.jpg?27793" /></a><a title="Follow us on Pinterest!" target="_blank" href="//www.pinterest.com/TheCloudOutletURBANOUTLET/"><img src="//cdn.shopify.com/s/files/1/0194/1577/files/Contact-Us-Page_04.jpg?27793" /></a><a title="Follow us on Twitter!" target="_blank" href="https://twitter.com/TheCloudOutletOnline"><img src="//cdn.shopify.com/s/files/1/0194/1577/files/Contact-Us-Page_05.jpg?27793" /></a><a title="Follow us on Wanelo!" target="_blank" href="//wanelo.com/thecloudoutletonline"><img src="//cdn.shopify.com/s/files/1/0194/1577/files/Contact-Us-Page_06.jpg?27793" /></a><a title="Follow us on Google+!" target="_blank" href="https://plus.google.com/+Uoionline/posts"><img src="//cdn.shopify.com/s/files/1/0194/1577/files/Contact-Us-Page_07.jpg?27793" /></a></p>' '';
			subs_filter '//cdn.shopify.com/s/files/' '/images/';
			subs_filter 'http://' '//';
			proxy_set_header Accept-Encoding "";
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header Cookie $http_cookie;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			
			}
		location ^~/iimages/ {
			proxy_pass http://23.239.29.106/;
			
			
			
			
			proxy_set_header Accept-Encoding "";
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header Cookie $http_cookie;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			
			
			
		}
		location /images/  {
			proxy_pass http://cdn.shopify.com/s/files/ ;
		}
		location /pages/thecloudoutlet-rewards {
			
			proxy_pass http://{$target}/pages/uoi-rewards;
			
		}
		location /google2bae11be7c6ed66e.html  {
			
			proxy_pass http://23.239.29.106/google2bae11be7c6ed66e.html;
			
		}
		location /googleshopping.txt  {
			
			proxy_pass http://23.239.29.106/googleshopping.txt;
			
		}

		
	}
