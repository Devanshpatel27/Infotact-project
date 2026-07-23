from config import DATABASE_PATH
from database import DatabaseManager


def main() -> None:
    database = DatabaseManager(DATABASE_PATH)
    try:
        for frame in database.read_frames().frames:
            print(frame)
    finally:
        database.close()


if __name__ == "__main__":
    main()
