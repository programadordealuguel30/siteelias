from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# crsf_token()
app.config['SECRET_KEY'] = 'bff26e704c4ec87ae5a9232095ba5b2380ecdfec' # no terminal, digitar pyhton, depois import secrets, depois secrets.token_hex(20). No fim, digite exit para voltar.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodadosflask.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # nome da função para onde você quer que o usuário seja direcionado
login_manager.login_message_category = 'alert-info'

from site_elias import routes # essa importação precisa ser depois, pois o app tem que ser criado antes
