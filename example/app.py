from chalice import Chalice
from propelauth_py import init_base_auth, TokenVerificationMetadata, UnauthorizedException

app = Chalice(app_name='example')

auth = init_base_auth('PROPELAUTH_AUTH_URL', 'PROPELAUTH_API_KEY',
                      token_verification_metadata=TokenVerificationMetadata(
                          verifier_key='''PROPELAUTH_VERIFIER_KEY''',
                          issuer='PROPELAUTH_AUTH_URL'
                      ))

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/whoami')
def whoami():
    try:
        auth_header = app.current_request.headers.get("authorization")
        user = auth.validate_access_token_and_get_user(auth_header)
        return {'user_id': user.user_id}
    except UnauthorizedException:
        # UnauthorizedError is Chalice's exception which will return a 401
        raise UnauthorizedError

@app.route('/org/{org_id}')
def admin_only(org_id):
    try:
        auth_header = app.current_request.headers.get("authorization")
        user_and_org_member_info = auth.validate_access_token_and_get_user_with_org(
            auth_header, org_id
        )
        return {'user_id': user_and_org_member_info.user.user_id,
                'org_name': user_and_org_member_info.org_member_info.org_name}
    except UnauthorizedException:
        raise UnauthorizedError
    except ForbiddenException:
        # We return a 403 for valid users that do not have access to the specified organization
        raise ForbiddenError

