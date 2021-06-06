class AuthorisedErr(BaseException): pass
class WrongRoleErr(BaseException): pass

class CreateBLObjectAccountErr(BaseException): pass
class LoginAccountNotExists(BaseException): pass
class UpdateAccountErr(BaseException): pass
class AcceptAccountErr(BaseException): pass
class DeleteAccountErr(BaseException): pass

class WrongCode(BaseException): pass
class DifferPasswords(BaseException): pass
