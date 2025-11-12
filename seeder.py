from app import app
from models.db import db
from models.user_model import User 
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from datetime import datetime, date

def seed_data():
    with app.app_context():
        try:
            print("Starting database seeding")
            
            def parse_birthday(date_string):
                return datetime.strptime(date_string, '%B %d, %Y').date()

            seed_users = [
                User(
                    id=1,
                    first_name="Belle",
                    middle_name="L",
                    last_name="Reambonanza",
                    email="belle@example.com",
                    password=generate_password_hash("beller123"),
                    birthday=parse_birthday("August 22, 2005"),
                    gender="Female",
                    phone_number="09674566985",
                    address="Cavite City",
                    student_id="2020-08787"
                ),
                User(
                    id=2,
                    first_name="Eli",
                    middle_name="B", 
                    last_name="Minaj",
                    email="eli@example.com",
                    password=generate_password_hash("eli123"),
                    birthday=parse_birthday("August 28, 2004"),
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