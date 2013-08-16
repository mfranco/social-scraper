from flask import Flask, jsonify, request

from common.views import APIView
from users.resources import UserResource


class UserAPIView(APIView):
    def get(self, **kwargs):
        resource = UserResource(request.json)
        data ={'user_list': resource.filter_by()}
        return self.json_response(data=data)


    def post(self):
        response = {}
        user_resource = UserResource(request.json)
        try:
            response['user_list'] = user_resource.get_or_create()
        except Exception as error:
            print error
            pass
        return self.json_response(data=response)


app = Flask(__name__)
app.add_url_rule('{0}/users/'.format(UserAPIView.ENDPOINT), view_func=UserAPIView.as_view('users'))

def run_app():
    app.run()
