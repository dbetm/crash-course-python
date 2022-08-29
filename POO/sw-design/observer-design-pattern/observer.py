from api.log_listener import setup_log_event_handlers
from api.plan import upgrade_plan
from api.slack_listener import setup_slack_event_handlers
from api.user import register_new_user, password_forgotten

setup_log_event_handlers()
setup_slack_event_handlers()

# register a new user
register_new_user(name="David", password="abcd", email="david@mail.com")

# send a password reset message
password_forgotten(email="david@mail.com")

# upgrade the plan
upgrade_plan(email="david@mail.com")

