from rest_framework import serializers
from MailerApp.models import Question, EmailId

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailId
        fields = ["email_id"]


class MailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = [
            "email_ids",
            "subject",
            "content",
        ]
        read_only_fields = ["email_ids"]
        
        
