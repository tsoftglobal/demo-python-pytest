import pytest
from app.user_service import UserService, User


class TestUserService:
    def test_create_user(self):
        service = UserService()
        user = User("john@example.com", "John Doe")

        result = service.create_user(user)
        assert result is True

    def test_get_user(self):
        service = UserService()
        user = User("jane@example.com", "Jane Doe")
        service.create_user(user)

        retrieved = service.get_user("jane@example.com")
        assert retrieved is not None
        assert retrieved.email == "jane@example.com"
        assert retrieved.name == "Jane Doe"

    def test_get_user_not_found(self):
        service = UserService()

        retrieved = service.get_user("nonexistent@example.com")
        assert retrieved is None

    def test_update_user(self):
        service = UserService()
        user = User("john@example.com", "John Doe")
        service.create_user(user)

        updated = User("john@example.com", "John Smith")
        result = service.update_user(updated)
        assert result is True

        retrieved = service.get_user("john@example.com")
        assert retrieved.name == "John Smith"

    def test_delete_user(self):
        service = UserService()
        user = User("john@example.com", "John Doe")
        service.create_user(user)

        result = service.delete_user("john@example.com")
        assert result is True

        retrieved = service.get_user("john@example.com")
        assert retrieved is None