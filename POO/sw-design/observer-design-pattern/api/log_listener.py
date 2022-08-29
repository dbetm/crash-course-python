from .event import subscribe
from lib.log import log


def handle_user_registered_event(user):
    log(f"User registered with email: {user.email}")


def handle_user_password_forgotten_event(user):
    log(f"User with email address {user.email} requested a password reset.")


def setup_log_event_handlers():
    subscribe(
        event_type="user_registered", 
        fn=handle_user_registered_event
    )
    subscribe(
        "user_password_forgotten",
        handle_user_password_forgotten_event
    )