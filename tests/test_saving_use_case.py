from unittest.mock import Mock

from src.saving_use_case import SavingUseCase
from src.user import User
from src.user_repository_interface import UserRepositoryInterface


def test_saving_user_save_the_user_in_the_repository():
    # Arrange
    user : User = User('salhi', 'abdou')
    spy_user_repository =Mock(spec =UserRepositoryInterface)
    spy_user_repository.save = Mock()
    saving_use_case :SavingUseCase= SavingUseCase(spy_user_repository)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once_with(user)

