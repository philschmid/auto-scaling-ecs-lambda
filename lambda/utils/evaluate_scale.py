

def evaluate_scale(message_number):
    try:
        return message_number/2
    except ValueError:
        raise ValueError("Got no Number")


