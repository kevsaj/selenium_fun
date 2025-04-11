def format_price(price_str):
    return float(price_str.replace('$', '').replace(',', '').strip())

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper

def clean_card_name(name):
    return name.strip()