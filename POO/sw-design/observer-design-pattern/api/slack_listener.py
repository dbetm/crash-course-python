from .event import subscribe
from lib.slack import post_slack_message


def handle_user_registered_event(user):
    post_slack_message(
        "sales", 
        (
            f"{user.name} has registered with email: {user.email}."
            " Don't forget to spam :)"
        )
    )

def setup_slack_event_handlers():
    subscribe(
        event_type="user_registered", 
        fn=handle_user_registered_event
    )