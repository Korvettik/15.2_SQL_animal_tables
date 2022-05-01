import sqlite3

with sqlite3.connect("animal.db") as con:
    cur = con.cursor()



# Создаем ВНЕШНИЕ таблицы c первичными ключами, смотрящими наружу, ID_type

    sqlite_query1 = """
        CREATE TABLE IF NOT EXISTS types
            (
            ID_type INTEGER PRIMARY KEY AUTOINCREMENT, 
            animal_type TEXT 
            )
        """
    sqlite_query2 = """
        CREATE TABLE IF NOT EXISTS breeds 
            (
            ID_breed INTEGER PRIMARY KEY AUTOINCREMENT, 
            breed TEXT
            ) 
        """
    sqlite_query3 = """
        CREATE TABLE IF NOT EXISTS outcome_types 
            (
            ID_outcome_types INTEGER PRIMARY KEY AUTOINCREMENT, 
            outcome_types TEXT
            ) 
        """
    sqlite_query4 = """
        CREATE TABLE IF NOT EXISTS colors 
            (
            ID_color INTEGER PRIMARY KEY AUTOINCREMENT, 
            color1 TEXT
            ) 
        """
    sqlite_query5 = """
        CREATE TABLE IF NOT EXISTS outcome_subtype 
            (
            ID_outcome_subtype INTEGER PRIMARY KEY AUTOINCREMENT, 
            outcome_subtype TEXT
            ) 
        """


# создаем ГЛАВНУЮ таблицу, часть полей обычные, часть полей type_id зарезервированы
# под внешние ключи, соединение с внешними таблицами

    sqlite_query6 = """
        CREATE TABLE IF NOT EXISTS animals_new
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age_upon_outcome TEXT,
            animal_id TEXT,
            name TEXT,
            date_of_birth TEXT,
            outcome_month INTEGER,
            outcome_year INTEGER,
            
            
            type_id INTEGER,
            breed_id INTEGER,
            color_id INTEGER,
            outcome_subtype_id INTEGER,
            outcome_type_id INTEGER,
            
            FOREIGN KEY (type_id) REFERENCES types(ID_type) ON DELETE CASCADE,
            FOREIGN KEY (breed_id) REFERENCES breeds(ID_breed) ON DELETE CASCADE,
            FOREIGN KEY (color_id) REFERENCES colors(ID_color) ON DELETE CASCADE,
            FOREIGN KEY (outcome_subtype_id) REFERENCES outcome_subtypes(ID_outcome_subtype) ON DELETE CASCADE,
            FOREIGN KEY (outcome_type_id) REFERENCES outcome_type(ID_outcome_types) ON DELETE CASCADE
            )
        """


    # sqlite_query7 = """
    #     INSERT INTO animals_new(
    #     age_upon_outcome,
    #     animal_id,
    #     name,
    #     date_of_birth,
    #     outcome_month,
    #     outcome_year,
    #     id_type,
    #     id_breed,
    #     id_color,
    #     id_outcome_subtype,
    #     id_outcome_type
    #     )
    #
    #     SELECT
    #     age_upon_outcome,
    #     animal_id,
    #     name,
    #     date_of_birth,
    #     outcome_month,
    #     outcome_year,
    #     animal_type,
    #     breed,
    #     color1,
    #     outcome_subtype,
    #     outcome_type
    #
    #     FROM animals
    #     """

# для заполнения полей таблиц содержанием, копируем данные ИЗ исходной таблицы animal,
# в которой вообще все поля заполнены



# заполняем внешние таблицы уникальными данными

    sqlite_query71 = """
        INSERT INTO types (
        animal_type
        )
        SELECT DISTINCT animal_type
        FROM animals
        """

    sqlite_query72 = """
        INSERT INTO breeds(
        breed
        ) 

        SELECT DISTINCT
        breed

        FROM animals
        """

    sqlite_query73 = """
        INSERT INTO colors(
        color1
        ) 

        SELECT DISTINCT
        color1

        FROM animals
        """

    sqlite_query74 = """
        INSERT INTO outcome_subtype(
        outcome_subtype
        ) 

        SELECT DISTINCT
        outcome_subtype

        FROM animals
        """


    sqlite_query75 = """
        INSERT INTO outcome_types(
        outcome_types
        ) 

        SELECT DISTINCT
        outcome_type

        FROM animals
        """




# теперь нам нужно ЗАПОЛНИТЬ Главную таблицу просто всеми данными
# нужных полей из исходной таблицы animal + ПРОПИСАТЬ СВЯЗИ С ВНЕШНИМИ ТАБЛИЦАМИ

    sqlite_query76 = """
        INSERT INTO animals_new
        (
        age_upon_outcome,
        animal_id,
        name,
        date_of_birth,
        outcome_month,
        outcome_year,
        
        type_id,
        breed_id,
        color_id,
        outcome_subtype_id,
        outcome_type_id
        ) 


        SELECT
        age_upon_outcome,
        animal_id,
        name,
        date_of_birth,
        outcome_month,
        outcome_year,
        
        ID_type,
        ID_breed,
        ID_color,
        ID_outcome_subtype,
        ID_outcome_types


        FROM animals
        
        LEFT JOIN types
        ON animals.animal_type = types.animal_type
        
        LEFT JOIN breeds
        ON animals.breed = breeds.breed
        
        LEFT JOIN colors
        ON animals.color1 = colors.color1
        
        LEFT JOIN outcome_subtype
        ON animals.outcome_subtype = outcome_subtype.outcome_subtype
        
        LEFT JOIN outcome_types
        ON animals.outcome_type = outcome_types.outcome_types
        
        """




if __name__ == '__main__':
    cur.execute(sqlite_query1)
    cur.execute(sqlite_query2)
    cur.execute(sqlite_query3)
    cur.execute(sqlite_query4)
    cur.execute(sqlite_query5)
    cur.execute(sqlite_query6)
    cur.execute(sqlite_query71)
    cur.execute(sqlite_query72)
    cur.execute(sqlite_query73)
    cur.execute(sqlite_query74)
    cur.execute(sqlite_query75)
    cur.execute(sqlite_query76)
