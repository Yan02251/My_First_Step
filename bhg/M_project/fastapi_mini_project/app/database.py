from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 환경 변수에서 데이터베이스 URL 가져오기
DATABASE_URL = settings.DATABASE_URL

# SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# 세션 팩토리 생성
async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with async_session_maker() as session:
        yield session