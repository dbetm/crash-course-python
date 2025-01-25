from datetime import datetime, timedelta
import time

import pandas as pd
import yagmail


from news import NewsFeed


def get_content():
    df = pd.read_csv("people.csv")
    topics = df["interest"].unique().tolist()
    email_body_per_topic: dict = dict()

    now_date = datetime.today().date()
    yesterday_date = now_date - timedelta(days=1)

    from_date = yesterday_date.strftime(format="%Y-%m-%d")
    to_date = now_date.strftime(format="%Y-%m-%d")

    for topic in topics:
        if not topic in email_body_per_topic:
            news_feed = NewsFeed(topic, from_date=from_date, to_date=to_date)
            email_body_per_topic[topic] = news_feed.get()

            time.sleep(1)

    return df, email_body_per_topic


def run(hour: int = 23, minute: int = 42):
    print(f"Running at {hour}:{minute} every day")

    while True:
        now_datetime = datetime.today()
        # print(now_datetime.hour, now_datetime.minute)
        if now_datetime.hour == hour and now_datetime.minute == minute:
            print("executing...")
            df, email_body_per_topic = get_content()

            print(email_body_per_topic)

            class MockYagMail:
                def send(self, *args, **kwargs) -> None:
                    print(f"Email sent to {kwargs['to']}, Done!!!")

            email_client = MockYagMail() # yagmail.SMTP(user="test@gmail.com", password="pwd")

            for idx, row in df.iterrows():
                content = email_body_per_topic[row["interest"]]
                email_client.send(
                    to=row["email"],
                    subject=f"News digest for {row['interest']} today!",
                    contents=f"Hi {row['name']} {row['surname']}\n See what's on about {row['interest']} \n\n{content}\n\n David",
                    # attachments="design.txt",
                )

        time.sleep(60)


if __name__ == "__main__":
    run()