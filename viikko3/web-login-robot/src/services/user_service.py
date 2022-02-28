<<<<<<< HEAD
import re
=======
>>>>>>> 2c81d6214f66db8309e5f44b13e0b967905a7f41
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if user:
            raise UserInputError("Username is already in use")

        if not re.match("^[a-z]{3,}$", username):
            raise UserInputError("Username has to consist of characters a-z and be at least 3 characters")

        if not re.search("[^a-zA-Z]", password) or len(password) < 8:
            raise UserInputError("Password has to be at least 8 characters and contain at least one non-letter")

        if not password == password_confirmation:
            raise UserInputError("Passwords don't match")

user_service = UserService()
