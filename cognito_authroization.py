
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

token ='eyJraWQiOiJpWFVZQXVWdW1RXC9qZ3RJemg1alNKM3V0dEVxU0JnQ1BibnZWbGRrS0tLdz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlNTJkNzhlNy0zMTBiLTQwYzItODAwNy1kNDZlN2E4ZTU1ZjQiLCJhdWQiOiI3Z2NjNmpwN2VubzNmNHZhYWM0M3NyY2lraiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJldmVudF9pZCI6IjJjYzExMGMyLTI0ZDItNDA4Ny1hNjM2LWY0M2I4N2UwNTUyYyIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjA2NzI5ODIzLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb21cL3VzLXdlc3QtMl9Fa2d5cmUydEEiLCJjb2duaXRvOnVzZXJuYW1lIjoiZTUyZDc4ZTctMzEwYi00MGMyLTgwMDctZDQ2ZTdhOGU1NWY0IiwiZXhwIjoxNjA2NzMzNDIzLCJpYXQiOjE2MDY3Mjk4MjMsImVtYWlsIjoiZGFrb2JlZGJhcmRAZ21haWwuY29tIn0.jzA0jnOqZllu-0MTOwCMf1NWecwb97KFC6MdeQQg7BW5SvleHV3DWD_iAaCeYM-UIjj5IzExp5wqkWW_194WKMTT6QutJcA24xeSSJwckt8O3T5O8DP-4bdgtrIylUekEbB99vu1lq3SDFJ_RxQuUjyvU8mr6qoTYHJM3aveug51RtzhWJKlEa5aDG8pphcRHvY9VCvhryYov7cQ9SNPV9AiqoFgXOHwEjkdZldLIJMbUFnlAQ3jm-uE0NmesEIJt8pjFHtLG7tHZM3I6QC1YXjxNSj2WOMvOAf10WYIfFuayLkfJBTwdwdARyhp9m-Q0eMR3NTUEbY2lzQz7J_VVg'

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
