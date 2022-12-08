from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from EVNCrawlFacebook.selenium.utils import facebook_login


import time

@api_view(["POST"])
def get_comment(request: Request):
    """Example
    {
        "link_post": "https://www.facebook.com/groups/630943070407078/subgroups/1331640773991372/posts/1444534716035310/",
        "number_comment": 5
    }
    """
    data = request.data
    link_request = data.get("link_post", "")
    number_comment = data.get("number_comment", "")
    if not link_request or not isinstance(number_comment, int):
        messsage = {
            'message': 'error input'
        }
        return Response(messsage, status=status.HTTP_400_BAD_REQUEST)
    else:
        messsage = {
            'message': 'successful check'
        }
        facebook_login.login()
        return Response(messsage, status=status.HTTP_200_OK)
