# ** accepts as many key-value pairs as calling statement provides
# **user_info Python creates empty dict user_info, pack name-value pairs
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# **kwargs is often used to collect non-specific keyword arguments