from website import create_app
from website.models import create_fake_users, create_img_table, create_admin

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        create_fake_users()
        create_img_table()
        create_admin()
    app.run(debug=True)