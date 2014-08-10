from flask.ext.principal import Principal,Permission,RoleNeed
from flask.ext.login import LoginManager
from flask_seed import app

# load the extension
principals = Principal(app)

# Create a permission with a single Need,in this case a RoleNeed
admin_permission = Permission(RoleNeed('admin'))


#{ Flask-Login
login_manager = LoginManager(app)

#}



