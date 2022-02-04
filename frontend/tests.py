import json
from django.test import TestCase, Client
from frontend.models import Notice
from django.contrib.auth.models import User

# Create your tests here.

# Test notices view
class TestNoticesView(TestCase):
    def setUp(self) -> None:
        harry = User.objects.create(username="harry", email="harry@example.com", password="harrypotter22")
        Notice.objects.create(notice_message="test notice", issued_by=harry)
        Notice.objects.create(notice_message="test notice 2", issued_by=harry)
        self.client = Client()
        return super().setUp()

    def test_notices_are_returned_predefined_json_format(self):
        """
        Ensure notices are sent in following json format
        {
            "notices":[
                { "notice_message": "<notice-message-goes-here>", "attachment": "<notice-attachment-url>" },
            ] 
        }
        """
        expected_json = json.dumps({'notices': [{'attachment': None, 'notice_message': 'test notice'}, {'attachment': None, 'notice_message': 'test notice 2'}]})
        response = self.client.get("/notices")
        self.assertJSONEqual(expected_json, response.json())


# Ensure notice can be created by user
class TestNoticeModel(TestCase):
    def setUp(self) -> None:
        User.objects.create(username="harry", email="harry@example.com", password="harrypotter22")
        self.client = Client()
        return super().setUp()

    # Ensure attachment is optional
    def test_user_can_create_notice_without_attachment(self):
        harry = User.objects.get(username="harry")
        notice = Notice.objects.create(notice_message="test notice", issued_by=harry)
        self.assertEqual(notice, Notice.objects.get(notice_message="test notice"))