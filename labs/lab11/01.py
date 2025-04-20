import psycopg2


conn = psycopg2.connect( # creating a connection
    host="localhost",
    database="postgres",
    user="postgres",
    password="dana3262"
)


####################
#       1
####################


create_func_filter_by_pattern = """
    CREATE OR REPLACE FUNCTION filter_by_pattern(pattern VARCHAR)
    RETURNS TABLE (id INTEGER, name VARCHAR(255), phone_number VARCHAR(20))
    AS
    $$
    BEGIN
        RETURN QUERY
        SELECT * FROM phonebook WHERE phonebook.name LIKE pattern || '%';
    END;
    $$
    LANGUAGE plpgsql;

"""



####################
#       2
####################



create_proc_insert_new_user = """
    CREATE OR REPLACE PROCEDURE insert_new_user(new_name VARCHAR, new_phone_number VARCHAR)
    AS
    $$
    BEGIN
        IF EXISTS (SELECT 1 FROM phonebook WHERE phonebook.name = new_name) THEN
            UPDATE phonebook SET phonebook.phone_number = new_phone_number WHERE phonebook.name = new_name;
        ELSE
            INSERT INTO phonebook(name, phone_number) VALUES(new_name, new_phone_number);
        END IF;
    END;
    $$
    LANGUAGE plpgsql;
"""





####################
#       4
####################




create_func_query_data = """
    CREATE OR REPLACE FUNCTION query_data(n_limit INTEGER, n_offset INTEGER)
    RETURNS TABLE(id INTEGER, name VARCHAR(255), phone_number VARCHAR(20))
    AS
    $$
    BEGIN
        RETURN QUERY
            SELECT * FROM phonebook ORDER BY id LIMIT n_limit OFFSET n_offset;
    END;
    $$
    LANGUAGE plpgsql;
"""



####################
#       5
####################



create_proc_delete_by_phone_number = """
    CREATE OR REPLACE PROCEDURE delete_by_phone_number(phone_number_to_delete VARCHAR)
    AS
    $$
    BEGIN
        DELETE FROM phonebook WHERE phonebook.phone_number = phone_number_to_delete;
    END;
    $$
    LANGUAGE plpgsql;
"""







def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)



def call_function_w_args(function_name, args):
    try:
        with conn.cursor() as cur:
            cur.callproc(function_name, args)
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)




def call_insert_new_user(name, phone):
    command = "CALL insert_new_user(%s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name, phone))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def call_delete_by_phone_number(phone):
    command = "CALL delete_by_phone_number(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (phone, ))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)



#execute_query(create_func_filter_by_pattern)
#print(call_function_w_args('filter_by_pattern', ('D',)))


#execute_query(create_proc_insert_new_user)
#call_insert_new_user("anna", "8707562")

#execute_query(create_func_query_data)
#print(call_function_w_args('query_data', (3, 1)))


execute_query(create_proc_delete_by_phone_number)
call_delete_by_phone_number("8777909")