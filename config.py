class Auth:
    """
    Auth class contains details for flow used in OAuth authentication
    using Google
    """
    # OAuth credentials
    CLIENT_ID = '<494683665446-r08617vleja50ht306krubjlclu3mi1h.apps.googleusercontent.com>'
    CLIENT_SECRET = '<cnprTYSQrLkSvy-V0Dc5wULz>'
    # URI that google server will redirect to
    REDIRECT_URI = '"http://localhost:8000"'
    # Endpoint to start OAuth request from
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    # Endpoint to fetch user token
    TOKEN_URI = 'https://oauth2.googleapis.com/token'
    # Endpoint to get user information at the end of oauth
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    # Data we plan to access from Google profile
    SCOPE = ['profile', 'email']
