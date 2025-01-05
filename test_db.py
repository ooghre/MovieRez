from app.database import engine, Base, db
from sqlalchemy import Column, Integer, String, text
import datetime

# Create a test model
class TestMovie(Base):
    __tablename__ = "test_movies"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    director = Column(String)

def test_connection():
    try:
        # Try to connect and execute a simple query
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ Database connection successful!")
            
            # Print database details
            db_info = connection.execute(
                text("SELECT current_database(), current_user")
            ).fetchone()
            print(f"Connected to database: {db_info[0]}")
            print(f"Connected as user: {db_info[1]}")
            
    except Exception as e:
        print("❌ Database connection failed!")
        print(f"Error: {str(e)}")

def test_sqlalchemy_operations():
    print("\nTesting SQLAlchemy operations:")
    try:
        # Create the test table
        Base.metadata.create_all(bind=engine)
        print("✅ Created test_movies table")
        
        # Create a test movie
        test_movie = TestMovie(
            title="Test Movie",
            director="Test Director"
        )
        
        # Add and commit the test movie
        db.session.add(test_movie)
        db.commit()
        print("✅ Added test movie to database")
        
        # Query the test movie
        queried_movie = db.session.query(TestMovie).first()
        print(f"✅ Retrieved test movie: {queried_movie.title} by {queried_movie.director}")
        
        # Clean up - delete the test movie and table
        db.session.delete(queried_movie)
        db.commit()
        TestMovie.__table__.drop(engine)
        print("✅ Cleaned up test data")
        
    except Exception as e:
        print("❌ SQLAlchemy operations failed!")
        print(f"Error: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    test_connection()
    test_sqlalchemy_operations()
