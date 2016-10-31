from datetime import datetime

def visitor_cookie_handler(request, response):
	visits = int(request.COOKIES.get('visits',1))
	last_visit = request.COOKIES.get('lastvisit', str(datetime.now()))
	last_visit_datetime = datetime.strptime(last_visit[:-7], '%Y-%m-%d %H:%M:%S')

	if (datetime.now() - last_visit_datetime).seconds > 10:
		visits += 1
		response.set_cookie('lastvisit', datetime.now())
	else:
		response.set_cookie('lastvisit', last_visit)

	response.set_cookie('visits', visits)