# import module with one function
#import user_profile_02
#from user_profile_02 import build_profile
#from user_profile_02 import build_profile as bp
#import user_profile_02 as up
from user_profile_02 import *

user_profile = build_profile('bryan', 'merges',
        age=33, location='new hampshire')

print(user_profile)