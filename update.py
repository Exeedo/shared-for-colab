def update_class(original_class):
    def wrapper(new_class):
        for key, value in new_class.__dict__.items():
            if key != '__dict__':
                setattr(original_class, key, value)
        return original_class
    return wrapper
