from collections import namedtuple
from functools import partial
from flask.ext.principal import Principal,Permission,RoleNeed,UserNeed,ItemNeed,identity_loaded
from flask.ext.login import LoginManager,current_user
from flask_seed import app

# load the extension
principals = Principal(app)
PostNeed = namedtuple('post',['method','value'])
EditPostNeed = partial(PostNeed,'edit')
class EditPostPermission(Permission):
    def __init__(self,post_id):
        need = EditPostNeed(unicode(post_id))
        super(EditPostPermission,self).__init__(need)
#
@identity_loaded.connect_via(app)
def on_identity_loaded(sender,identity):
    # Set the identity user object
    identity.user = current_user
    # Add the UserNeed to the identity
    if hasattr(current_user,'id'):
        identity.provides.add(UserNeed(current_user.id))

    #Assuming the User model has a list of roles, update the
    #identity with the roles that the user provides
    if hasattr(current_user,'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.name))

    if hasattr(current_user,'posts'):
        for post in current_user.posts:
            identity.provides.add(EditPostNeed(post.id))

# Create a permission with a single Need,in this case a RoleNeed
admin_permission = Permission(RoleNeed('admin'))


#{ Flask-Login
login_manager = LoginManager(app)

#}



