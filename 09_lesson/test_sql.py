from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, update, delete
import pytest

DATABASE_URL = "postgresql://postgres:665@localhost:5432/postgres"
_DB_ENGINE = create_engine(DATABASE_URL, echo=True)


@pytest.fixture(scope="function")
def db():
    return _DB_ENGINE


# Добавление student
def test_add_new_student(db):
    metadata = MetaData()

    student_table = Table('student', metadata, autoload_with=db)

    primary_key_column = student_table.columns['user_id']

    user_id = 11795
    level = "Beginner"
    education_form = "personal"
    subject_id = 1

    insert = student_table.insert().values(
        user_id=user_id,
        level=level,
        education_form=education_form,
        subject_id=subject_id
    ).returning(primary_key_column)

    inserted_id = None
    with db.connect() as connection:
        result = connection.execute(insert)
        connection.commit()
        retrived_row = result.fetchone()
    if retrived_row is not None:
        inserted_id = retrived_row[0]
    assert inserted_id is not None

    select = student_table.select().where(
        student_table.columns['user_id'] == inserted_id)
    with db.connect() as connection:
        retrived = connection.execute(select).fetchone()
    assert retrived is not None
    assert retrived.user_id == user_id
    assert retrived.level == level


# Редактирование student
def test_update_student(db):
    metadata = MetaData()
    student_table = Table('student', metadata, autoload_with=db)
    primary_key_column = student_table.columns['user_id']

    user_id_to_update = 11795
    initial_level = "Beginner"
    initial_education_form = "personal"
    subject_id = 1

    insert = student_table.insert().values(
        user_id=user_id_to_update,
        level=initial_level,
        education_form=initial_education_form,
        subject_id=subject_id
    ).returning(primary_key_column)

    inserted_id = None

    with db.connect() as connection:
        result = connection.execute(insert)
        connection.commit()
        retrived_row = result.fetchone()
    if retrived_row is not None:
        inserted_id = retrived_row[0]
    assert inserted_id is not None

    new_education_form = "group"
    update_stmt = update(student_table).where(
        student_table.columns['user_id'] == inserted_id
    ).values(
        education_form=new_education_form
    )

    with db.connect() as connection:
        connection.execute(update_stmt)
        connection.commit()

    select_stmt = student_table.select().where(
        student_table.columns['user_id'] == inserted_id)

    with db.connect() as connection:
        retrived = connection.execute(select_stmt).fetchone()

    assert retrived is not None
    assert retrived.education_form == new_education_form
    assert retrived.level == initial_level


# Удаление student
def test_delete_student(db):

    metadata = MetaData()
    student_table = Table('student', metadata, autoload_with=db)

    user_id_to_delete = 11795
    level_to_insert = "Beginner"
    education_form_to_insert = "group"
    subject_id_to_insert = 1

    # Предварительная очистка
    cleanup_delete = delete(student_table).where(
        student_table.columns['user_id'] == user_id_to_delete
    )
    with db.connect() as connection:
        connection.execute(cleanup_delete)
        connection.commit()

    # Вставка записи для проверки
    insert = student_table.insert().values(
        user_id=user_id_to_delete,
        level=level_to_insert,
        education_form=education_form_to_insert,
        subject_id=subject_id_to_insert
    )
    with db.connect() as connection:
        connection.execute(insert)
        connection.commit()

    # Проверка наличия записи
    select_before = student_table.select().where(
        student_table.columns['user_id'] == user_id_to_delete)
    with db.connect() as connection:
        retrived_before = connection.execute(select_before).fetchall()

    assert len(retrived_before) >= 1

    # Удаление записи
    delete_stmt = delete(student_table).where(
        student_table.columns['user_id'] == user_id_to_delete
    ).returning(student_table.columns['user_id'])

    with db.connect() as connection:
        result = connection.execute(delete_stmt)
        connection.commit()

    deleted_rows = result.fetchall()

    # Проверка удаления всех найденных строк
    # т.к. выходила ошибка о неудалении дубликатов
    expected_deleted_count = len(retrived_before)
    assert len(deleted_rows) == expected_deleted_count

    # Проверка удаления
    select_after = student_table.select().where(
        student_table.columns['user_id'] == user_id_to_delete)
    with db.connect() as connection:
        retrived_after = connection.execute(select_after).fetchone()
        assert retrived_after is None
