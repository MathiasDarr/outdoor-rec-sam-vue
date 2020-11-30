
import json
import time
import urllib.request
from jose import jwk, jwt
from jose.utils import base64url_decode


region = 'us-west-2'
userpool_id = 'us-west-2_Ekgyre2tA'
app_client_id = '7gcc6jp7eno3f4vaac43srcikj'
keys_url = 'https://cognito-idp.{}.amazonaws.com/{}/.well-known/jwks.json'.format(region, userpool_id)


with urllib.request.urlopen(keys_url) as f:
  response = f.read()
keys = json.loads(response.decode('utf-8'))['keys']

token = 'eyJraWQiOiJpWFVZQXVWdW1RXC9qZ3RJemg1alNKM3V0dEVxU0JnQ1BibnZWbGRrS0tLdz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlNTJkNzhlNy0zMTBiLTQwYzItODAwNy1kNDZlN2E4ZTU1ZjQiLCJhdWQiOiI3Z2NjNmpwN2VubzNmNHZhYWM0M3NyY2lraiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJldmVudF9pZCI6IjIzODczOWI5LTA2MTQtNDdlZi04YTgyLThhY2VkMzczZmRiNSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjA2NzIxNzcyLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb21cL3VzLXdlc3QtMl9Fa2d5cmUydEEiLCJjb2duaXRvOnVzZXJuYW1lIjoiZTUyZDc4ZTctMzEwYi00MGMyLTgwMDctZDQ2ZTdhOGU1NWY0IiwiZXhwIjoxNjA2NzI1MzcyLCJpYXQiOjE2MDY3MjE3NzIsImVtYWlsIjoiZGFrb2JlZGJhcmRAZ21haWwuY29tIn0.o3LAG-pGhkSl08ve4AdgTi5niiKnQLP8CyqiucxapzcRoHz1eVTHDdBz_-Cd7kFcdoVm_qGHexC6u0lV7CAUqInSOXoNlea9diMrp7Iw3AmvXICpgtr8EkXelziyVvR7deeedQiD-XCBizqntyYY240vhj6vebbYBz8Z34EdZxgSB-TkqK1JBfH-YzLVHcetQdu0wydpDPtw43E-bUh4j0d2DZ5bcRKmabM11RCVwjagwX6cW3_HubsISsKCDzMyDIyJuMbtkuasTVDmtIPZo1mniNI8-iUqsVhpKhZghtnim6z5t3Ds0TiibfDmKcsAIp6ywZJzXuv57bh4HYcW-g'

headers = jwt.get_unverified_headers(token)
kid = headers['kid']
# search for the kid in the downloaded public keys
key_index = -1
for i in range(len(keys)):
    if kid == keys[i]['kid']:
        key_index = i
        break
if key_index == -1:
    print('Public key not found in jwks.json')

# construct the public key
public_key = jwk.construct(keys[key_index])
# get the last two sections of the token,
# message and signature (encoded in base64)
message, encoded_signature = str(token).rsplit('.', 1)
# decode the signature
decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))
# verify the signature
if not public_key.verify(message.encode("utf8"), decoded_signature):
    print('Signature verification failed')

print('Signature successfully verified')
# since we passed the verification, we can now safely
# use the unverified claims
claims = jwt.get_unverified_claims(token)

if time.time() > claims['exp']:
    print('Token is expired')

if claims['aud'] != app_client_id:
    print('Token was not issued for this audience')
