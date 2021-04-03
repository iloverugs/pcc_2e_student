# copy of user_profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# build profile of self, use first/last name, three other key-value pairs
user_profile = build_profile('bryan', 'merges',
                            location='new hampshire',
                            age='33',
                            studying='programming')
print(user_profile)