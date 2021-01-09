from django.shortcuts import render
from rest_framework.views import APIView
from MailerApp.serializers import MailSerializer
from rest_framework.response import Response
from MailerApp.Apis import SendgridMailApi, MailjetApi
import json

# Create your views here.

class MailAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = MailSerializer(data=data)
        if serializer.is_valid():
            subject = data["subject"]
            content = data["content"]
            try:
                mj = MailjetApi()
                response = mj.send_mail(data["email_ids"], subject, content) 
                if response.status_code == 200:
                    return Response(data, response.status_code)
                else:
                    raise Exception("mail not send with mailjet api")
            # IF we get any exception then variable 'e' will catch that exception. 
            # So to handle the exception or error we continue to send email using
            # second Email API that is Mailjet.
            except Exception as e:
                Sg = SendgridMailApi()
                response = Sg.send_mail(data["email_ids"], subject, content) 
                # print(response.status_code)
                # print(response.body)
                # print(response.headers)
                if response.status_code == 202:
                    return Response(data, response.status_code)
                A = {}
                A["eror"] = "Unsuccessful attempt check credentials"
                return Response(json.dumps(A), status=400)
        else:
            return Response(serializer.errors, status=400)
        
