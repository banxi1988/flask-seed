from flask  import Response
from flask.ext.principal import Principal,Permission,RoleNeed
from flask_seed import app

# load the extension
principals = Principal(app)

# Create a permission with a single Need,in this case a RoleNeed
admin_permission = Permission(RoleNeed('admin'))


