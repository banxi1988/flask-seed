#-*- coding:utf-8 -*-
from flask import ( current_app, Response,request,redirect,url_for,abort,
                   session,render_template
                   )
from flask.ext.login import (
 login_user,logout_user,current_user,login_required
)
from flask.ext.principal import (
            Identity,AnonymousIdentity,identity_changed
)
from flask_seed import app
from .plugins import admin_permission,EditPostPermission
from .plugins import login_manager
from .users import User

login_manager.login_view = 'login'
login_manager.login_message = u"请登录"


@login_manager.user_loader
def load_user(user_id):
    return User.by_id(user_id)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return """
            <form action=""  method="post">
                <input name="username" type="text" placeholder="username"/>
                <input name="password" type="password" placeholder="password"/>
                <button type="submit" >Login</button>
            </form>
    """
    else:
        form = request.form
        username = form.get('username')
        password = form.get('password')
        ok,user = User.check_login(username,password)
        if ok:
            login_user(user)
            # Tell Flask-Principal the identity changed
            identity = Identity(user.id)
            identity_changed.send(current_app._get_current_object(),identity=identity)
            redirect_url = request.args.get('next') or url_for('index')
        else:
            redirect_url = url_for('login')
        return redirect(redirect_url)


@app.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    # Remove session key set by Flask-Principal
    for key in ('identity.name','identity.auth_type'):
        session.pop(key,None)
    # Tell Flask-Principal the user is anonymous
    identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return Response("Only if you are an user")

@app.route('/settings')
@login_required
def settings():
    return "Settings OK"

# protect a permission with a single Need, in this case a RoleNeed
@app.route('/admin')
@login_required
@admin_permission.require()
def admin():
    return Response('Only if you are an admin')
# this time protect with a context mananger
@app.route('/articles')
def do_articles():
    with admin_permission.require():
        return Response('Only if you are admin')

@app.route('/posts/<post_id>', methods=['PUT','PATCH'])
def edit_post(post_id):
    permission =  EditPostPermission(post_id)
    if permission.can():
        # Save the edits
        return render_template('edit_post.html')
    abort(403)






