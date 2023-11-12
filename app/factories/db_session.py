from sqlalchemy.orm import scoped_session, sessionmaker

ScopedFactorySession = scoped_session(
    session_factory=sessionmaker(autocommit=False, autoflush=False),
)
