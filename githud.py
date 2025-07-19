import requests


class Githud:
    def __init__(self):
        self.domain = "https://api.github.com"
        self.api = "users"


    def get_events(self, username):
        url = f"{self.domain}/{self.api}/{username}/events"
        print(f"Getting events for {username}")
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: {response.status_code} {response.reason}")
        else:

            response_data = response.json()
            if len (response_data) == 0:
                print(f"No events found for {username}")
                return
            for r in response_data:
                event = r["type"]
                payload = r["payload"]
                _type = payload.get("ref_type", " ")
                action = payload.get("action", " ").capitalize()
                commits = len(payload.get("commits", []))
                name = r["repo"]["name"]
                date = r["created_at"]

                match event:
                    case "PushEvent":
                        print(f"- Pushed {commits} commits to {name} at {date}")
                    case "WatchEvent":
                        print(f"- Started in {name} at {date}")
                    case "CreateEvent":
                        print(f"- Created a {_type} in {name} at {date}")
                    case "DeleteEvent":
                        print(f"- Deleted a {_type} in {name} at {date}")
                    case "ForkEvent":
                        print(f"- Forked in {name} at {date}")
                    case "IssuesEvent":
                        print(f"- {action} a issues in {name} at {date}")
                    case "PullRequestEvent":
                        print(f"- {action} a pull request in {name} at {date}")
                    case "IssueCommentEvent":
                        print(f"- {action} a comment for issue in {name} at {date}")
                    case "PullRequestReviewCommentEvent":
                        print(f"- {action} a comment for a pull and review in {name} at {date}")
                    case "ReleaseEvent":
                        print(f"- {action} in {name} at {date}")
                    case "PublicEvent":
                        print(f"- {action} in {name} at {date}")
                    case _:
                        print(f"- Event {event} not managed")


