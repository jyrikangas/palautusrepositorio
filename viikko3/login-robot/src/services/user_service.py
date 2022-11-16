from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not  bool(self._user_repository.find_by_username(username)):
            if not username or not password:
                raise UserInputError("Username and password are required")
            if (not re.match("[a-z]+$", username)) or len(username)<3:
                raise UserInputError(f"Username {username} is not valid")
            if (not re.match(r"^(?=.*[\d])[a-zA-Z0-9]{8,}$", password)):
                raise UserInputError("Password is not valid")

            # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        else:
            raise UserInputError(f"User with username {username} already exists")
