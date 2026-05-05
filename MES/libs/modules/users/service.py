from .schemas import UserCreate, UserResponse

class UserService:
    def __init__(self):
        # Tạm thời dùng dict để làm mock database
        self.mock_db = []
        self.current_id = 1

    def create_user(self, user_in: UserCreate) -> UserResponse:
        # Mock logic lưu vào database
        new_user = UserResponse(
            id=self.current_id,
            username=user_in.username,
            email=user_in.email,
            is_active=True
        )
        self.mock_db.append(new_user)
        self.current_id += 1
        return new_user

    def get_users(self) -> list[UserResponse]:
        return self.mock_db
