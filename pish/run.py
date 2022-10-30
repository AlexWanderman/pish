from app import create_app

app = create_app({
    'DEBUG': True,
    'SECRET_KEY': 'dev',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
})

if __name__ == '__main__':
    app.run()
