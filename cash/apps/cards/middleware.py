from models import Cards
from django.shortcuts import redirect

class UserMiddleware(object):
    cookie_name = 'usersession'

    def process_request(self, request):
        # print "="*20, request.session.set_expiry(0)
        # print "="*20, request.session.get_expiry()
        if request.session.get('card_id'):

            request.usr = Cards.objects.get(cards_num = request.session.get('card_id'))
        # else:
        #     return redirect('/')

    def process_response(self, request, response):
        if not hasattr(request, 'usr'):
            return response
        # print '+'*20
        # session_key = request.usr.session_key
        #
        # if request.usr.save_session:
        #     max_age = request.usr.max_age
        # else:
        #     max_age = None
        #
        # if session_key:
        #     response.set_cookie(self.cookie_name, session_key, max_age=max_age)
        # elif request.COOKIES.get(self.cookie_name):
        #     response.delete_cookie(self.cookie_name)

        return response