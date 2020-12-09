from botocore.exceptions import ClientError


def authenticate_user(cidp, user_pool_client, username, password):
    """
    Authenticate a user & return JWT id token
    :param cidp: cognito identity provider client,
    :param user_pool_client: user pool client ID
    :param username:
    :param password:
    :return: JWT identificaiton token
    """
    response = cidp.initiate_auth(AuthFlow='USER_PASSWORD_AUTH',
                                  AuthParameters={'USERNAME': username, 'PASSWORD': password},
                                  ClientId=user_pool_client)
    return response['AuthenticationResult']['IdToken']

