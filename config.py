import os

basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard to guess string'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DOFLASK_MAIL_SUBJECT_PREFIX = '[DoFlask]'
    DOFLASK_MAIL_SENDER = 'DoFlask Admin<50037521@qq.com>'
    DOFLASK_ADMIN = os.environ.get('DOFLASK_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI =os.environ.get('DEV_DATABASE_URL') or  'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class TestingConfig(Config):
    TESTING=True

config={
    'development': DevelopmentConfig,
    'testing':TestingConfig,

    'default': DevelopmentConfig
}