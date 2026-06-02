import sys
import unittest
from unittest.mock import MagicMock, patch

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_sqlalchemy = MagicMock()
        cls.mock_orm = MagicMock()
        cls.mock_ext = MagicMock()
        cls.mock_declarative = MagicMock()

        cls.modules_patcher = patch.dict('sys.modules', {
            'sqlalchemy': cls.mock_sqlalchemy,
            'sqlalchemy.orm': cls.mock_orm,
            'sqlalchemy.ext': cls.mock_ext,
            'sqlalchemy.ext.declarative': cls.mock_declarative
        })
        cls.modules_patcher.start()

        # Import after shimming
        from app.infrastructure.database import get_db, SessionLocal
        cls.get_db = staticmethod(get_db)
        cls.SessionLocal = SessionLocal

    @classmethod
    def tearDownClass(cls):
        cls.modules_patcher.stop()
        # Clean up the module from sys.modules to prevent test pollution
        sys.modules.pop('app.infrastructure.database', None)

    def test_get_db_yields_session_and_closes(self):
        mock_session = MagicMock()
        # Reset mock just in case
        self.SessionLocal.reset_mock()
        self.SessionLocal.return_value = mock_session

        db_gen = self.get_db()

        db = next(db_gen)
        self.assertIs(db, mock_session)

        mock_session.close.assert_not_called()

        with self.assertRaises(StopIteration):
            next(db_gen)

        mock_session.close.assert_called_once()

    def test_get_db_closes_on_exception(self):
        mock_session = MagicMock()
        self.SessionLocal.reset_mock()
        self.SessionLocal.return_value = mock_session

        db_gen = self.get_db()

        db = next(db_gen)
        self.assertIs(db, mock_session)
        mock_session.close.assert_not_called()

        with self.assertRaises(ValueError):
            db_gen.throw(ValueError("Test exception"))

        mock_session.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
