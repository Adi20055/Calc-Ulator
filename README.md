# Calc-Ulator

A FastAPI-based user authentication service with SQLite database integration.

## Features

- User registration and authentication
- JWT-based token authentication
- SQLite database for persistent storage
- FastAPI with automatic API documentation
- Secure password hashing with bcrypt

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd Calc-Ulator
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/MacOS
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   cd backend/user_service
   pip install -r requirements.txt
   ```

## Running the Application

1. Navigate to the user service directory:
   ```bash
   cd backend/user_service
   ```

2. Run the application:
   ```bash
   python -m app.main
   ```

The server will start at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

### Available Endpoints

- `POST /register` - Register a new user
  - Required fields: username, password
  - Optional fields: email, full_name

- `POST /token` - Login and get access token
  - Required fields: username, password

- `GET /users/me` - Get current user information
  - Requires authentication token

## Development

### Project Structure
```
backend/
└── user_service/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py        # FastAPI application
    │   ├── models.py      # SQLAlchemy models
    │   └── database.py    # Database configuration
    └── requirements.txt    # Project dependencies
```

### Database

The application uses SQLite as the database. The database file (`users.db`) is automatically created in the app directory when the application first runs.

### Security

- Passwords are hashed using bcrypt
- Authentication uses JWT tokens
- Database file is excluded from version control

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Submit a pull request

## License

[Your chosen license]
