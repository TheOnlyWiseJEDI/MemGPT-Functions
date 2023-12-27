The function checks for the current weather for the specified zipcode at openweathermap.org.

It requres a free API key. Once you have the key you can edit the code and insert it where you see 'YOUR-API-KEY'

You will need to adjust the time zone for your area. Currently it is set for EST. In the function convert_time() you will find "est_time = utc_time - timedelta(hours=5)" This is the offset from UTC -5 hours for Eastern Standard Time. Central Standard Time (CST) would be -6 for example (hours=6).

There are also two urls that get added to the results. In the function format_weather_output() you will find 'radar_map' & 'forecast'. You can change these URL's to point to resources that apply to your area.

Once you have the results from get_weather, if you have 'send_to_chrome' installed you can simply ask the AI to open either of the URL's in the default system browser.
