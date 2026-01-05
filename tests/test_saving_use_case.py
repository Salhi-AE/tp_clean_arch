from dataclasses import dataclass
from unittest.mock import Mock
from abc import ABCMeta, abstractmethod

@dataclass
class User:
    first_name: str
    last_name: str


class UserRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def save(self,user:User)->None:
        pass


class SavingUseCase:
   def __init__(self, user_repository:UserRepositoryInterface):
       self.user_repository = UserRepositoryInterface =user_repository
   def execute(self,user:User)-> None:
        self.user_repository.save()



def test_saving_user_is_calling_delegated_repository():
    user :User =User(first_name='salhi',last_name='abdou')
    spy_user_repository =Mock(spec = UserRepositoryInterface)
    saving_use_case:SavingUseCase =SavingUseCase(user_repository=spy_user_repository)
    saving_use_case.execute(user)


    spy_user_repository.save.assert_called_once()
