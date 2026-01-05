from unittest.mock import Mock

from src.saving_use_case import SavingUseCase
from src.user import User
from src.user_repository_interface import UserRepositoryInterface


def test_saving_user_is_calling_delegated_repository():
    # Arrange
    user : User = User(first_name='salhi', last_name='abdou')
    spy_user_repository =Mock(spec =UserRepositoryInterface)
    saving_use_case: SavingUseCase = SavingUseCase(user_repository=spy_user_repository)
    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once()
