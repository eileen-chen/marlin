# import os
# import base64
# import blowfish

# from django.http import HttpResponse
# from users.models import User, Profile, Demography
# from account.forms import UserForm
# from account.views.encoding import byte_to_str, str_to_bytes

# def sign_up(request):
#     if request.method == 'POST':
#         __userform = UserForm(request.POST)
#         if __userform.is_valid():
#             email = __userform.cleaned_data['email']
#             password = __userform.cleaned_data['password']

#             # create user
#             __user = User.objects.create(
#                 email=email,
#                 password=byte_to_str(__encrypt_password(password))
#             )

#             # creare user base infor
#             if __user:
#                 Profile(user=__user).save()
#                 Demography(user=__user).save()
#             return HttpResponse(200)
#         else:
#             pass


# def __encrypt_password(password):
#     import environ
#     env = environ.Env()
#     environ.Env.read_env()

#     # generate cipher
#     CIPHER_KEY = env('CIPHER_KEY')
#     cipher = blowfish.Cipher(str_to_bytes(CIPHER_KEY))

#     # encrypt password
#     byte_password = str_to_bytes(password)
#     byte_encrypted_password = b"".join(cipher.encrypt_ecb_cts(byte_password))
#     encoded_password = base64.b64encode(byte_encrypted_password)
#     return byte_to_str(encoded_password)
    