from fastapi_users.authentication import  CookieTransport, JWTStrategy, AuthenticationBackend



#Cookie
cookie_tansport = CookieTransport(cookie_name="bands", cookie_max_age=3600)



#JWT
SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_tansport,
    get_strategy=get_jwt_strategy,
)