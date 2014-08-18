#-*- coding:utf-8 -*-
import logging
import os.path
import codecs
from flask import ( current_app, Response,request,redirect,url_for,abort,
                   session,render_template,send_from_directory,jsonify
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

logger = logging.getLogger(__name__)
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
    return app.send_static_file('index.html')

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

ALLOWED_EXTENTIONS = {'png','jpg','gif','jpeg'}
@app.route('/umeditor')
def umeditor():
    '''
    editor 需要这么一个接受请求的sever_url,但是umeditor没有
    '''
    action = request.args.get('action')
    if action == 'config':
        return jsonify(
            imageMaxSize=1*1024*1024,
            imageAllwFiles=['.'+ext for ext in  ALLOWED_EXTENTIONS],
        )
    else:
        logger.error('Unkonw action'+str(action))

#### View for upload file
def allowd_file(filename):
    return '.' in filename and  filename.rsplit('.')[1] in ALLOWED_EXTENTIONS


@app.route('/upload', methods=['GET','POST'])
def upload_file():
    import os.path
    from werkzeug.utils import secure_filename
    if request.method == 'POST':
        file = request.files['upfile']
        if file and allowd_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['IMG_UPLOAD_FOLDER'],filename))
            return jsonify(state='SUCCESS',
                           url=url_for('uploaded_file',filename=filename),
                           title=filename,
                           original=file.filename
                           )
    return '''
        <form action="" method="POST" enctype="multipart/form-data">
            <p>
                <input type="file" name="file" />
                <input type="submit" value="Upload"/>
            </p>
        </form>

    '''

@app.route('/files/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['IMG_UPLOAD_FOLDER'],filename)

@app.route('/questions/',methods=['GET','POST'])
def questions():
    if request.method == 'GET':
        path = app.config['QUESTIONS_UPLOAD_FOLDER']
        filenames = [fname for fname in os.listdir(path) if fname.endswith('.json')]
        return jsonify(ok=True,question_files=filenames)
    import time
    import random
    import json
    import codecs
    form = request.form
    filename = time.strftime('%Y-%m-%d_%H_%M_%S') + str(random.randint(1,1000000))+'.json'
    r = dict(
        filename = filename,
        content = form.get('content'),
        timestamp = int(time.time())
    )
    content = json.dumps(r)
    filepath = os.path.join(app.config['QUESTIONS_UPLOAD_FOLDER'],filename)
    with codecs.open(filepath,'w',encoding='utf-8') as f:
        f.write(content)
    return redirect('/static/show_questions.html?question_file='+filename)

@app.route('/show_question/<question_file>')
def show_question(question_file):
    filepath = os.path.join(app.config['QUESTIONS_UPLOAD_FOLDER'],question_file)
    with codecs.open(filepath,'r',encoding='utf-8') as f:
        content = f.read()
    return content


@app.route('/questions/<question_file>',methods=['GET','PUT'])
def question(question_file):
    if request.method == 'GET':
        return send_from_directory(app.config['QUESTIONS_UPLOAD_FOLDER'],question_file)
    else:
        pass


