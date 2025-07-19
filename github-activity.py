import sys

from githud import Githud


def manage_event_githud():
    try:
        if len(sys.argv) < 2:
            print("Please enter a username.")
            return

        githud = Githud()
        username = sys.argv[1].lower()

        githud.get_events(username)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    manage_event_githud()