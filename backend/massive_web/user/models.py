from django.db import models
from oauth2client import client, crypt

STATUS_USER_ACTIVE = 10
STATUS_ADMIN_ACTIVE = 11
STATUS_INACTIVE = 12
GOOGLE_USER_ID = '629002016280-i54mtm5av310m0as2i279s7aq5cvl37l.apps.googleusercontent.com'

class User(models.Model):
    name = models.TextField(max_length=200, null=False)
    surname = models.TextField(max_length=200, null=True)
    status = models.IntegerField(null=True, default=10)
    image_url = models.TextField(max_length=300, null=True)
    email = models.TextField(max_length=150, unique=True, null=False)
    google_token = models.TextField(null=True)
    google_id = models.TextField(max_length=100, null=True)
    facebook_token = models.TextField(null=True)
    facebook_id = models.TextField(null=True)
    token = models.TextField(max_length=500, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def backend_data(self):
        return {
            'name' : self.name,
            'surname': self.surname,
            'image_url': self.image_url,
            'email': self.email,
            'created_at': self.created_at
        }

    def create_google_user(self, payload, user_data):
        u = User
        u.email = payload['email']
        u.name = payload['given_name']
        u.surname = payload['family_name']
        u.image_url = payload['image_url']
        u.google_id = user_data['id']
        u.google_token = user_data['token']
        u.save()

    def google_validate(self, token):
        """
        Validates if the request actually comes from Google.
        :param token:
        :return: payload in the format
            azp:GOOGLE_USER_ID, (Unused, for android app)
            aud:GOOGLE_USER_ID, (Used)
            sub: Unused (and not sure what it does)
            email: User email,
            email_verified:bool,
            at_hash: string
            iss: Always accounts.google.com
            iat: timestamp
            exp: timestamp
            name: name family name
            picture: URL,
            given_name: Name,
            family_name: Family name,
            locale: en
        """
        try:
            payload = client.verify_id_token(token, GOOGLE_USER_ID)
            if payload['iss'] not in ['accounts.google.com', 'https://accounts.google.com'] or payload['aud'] != GOOGLE_USER_ID:
                return False
            else:
                return payload
        except crypt.AppIdentityError:
                return False