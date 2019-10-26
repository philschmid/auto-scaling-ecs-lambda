

def evaluate_scale(message_number):
    try:
        return int(round(int(message_number) / 5,0))
    except ValueError:
        raise ValueError("Got no Number")


