from app import app
from models.db import db
from models.user_model import User 
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def seed_data():
    with app.app_context():
        try:
            print("Starting database seeding")
            

            seed_users = [
                User(
                    id=1,
                    fname="Belle",
                    middle_name="L",
                    lname="Reambonanza",
                    email="belle@example.com",
                    pass_word=generate_password_hash("beller123"),
                    birthday="August 22, 2005",
                    gender="Female",
                    phone_number="09674566985",
                    address="Cavite City",
                    student_id="2020-08787"
                ),
                User(
                    id=2,
                    fname="Eli",
                    middle_name="B", 
                    lname="Minaj",
                    email="eli@example.com",
                    pass_word=generate_password_hash("eli123"),
                    birthday="April 28, 2005",
                    gender="Female",
                    phone_number="09674566986",
                    address="Quezon City",
                    student_id="2020-01724"
                )
            ]

            for user in seed_users:
                existing_user = User.query.filter_by(email=user.email).first()
                if existing_user:
                    print(f"Skipping existing user: {user.email}")
                    continue
                db.session.add(user)

            db.session.commit()
            print("Database seeded successfully")

        except IntegrityError as e:
            db.session.rollback()
            print(f"Integrity error: {e}")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"SQLAlchemy error: {e}")

        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error during seeding: {e}")

        finally:
            db.session.close()

if __name__ == "__main__":
    seed_data()