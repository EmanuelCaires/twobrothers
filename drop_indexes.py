import psycopg2

def drop_duplicate_indexes():
    try:
        # Connect to your PostgreSQL database
        connection = psycopg2.connect(
            dbname='your_db_name',
            user='your_username',
            password='your_password',
            host='localhost',  # or your database host
            port='5432'        # or your database port
        )
        cursor = connection.cursor()

        # SQL commands to drop duplicate indexes
        drop_commands = [
            "DROP INDEX IF EXISTS account_emailaddress_user_id_2c513194;",
            "DROP INDEX IF EXISTS auth_group_permissions_group_id_b120cbf9;",
            "DROP INDEX IF EXISTS auth_permission_content_type_id_2f476e4b;",
            "DROP INDEX IF EXISTS auth_user_groups_user_id_6a12ed8b;",
            "DROP INDEX IF EXISTS auth_user_user_permissions_user_id_a95ead1b;",
            "DROP INDEX IF EXISTS core_order_items_order_id_c5dde6c1;",
            "DROP INDEX IF EXISTS socialaccount_socialapp_sites_socialapp_id_97fb6e7d;",
            "DROP INDEX IF EXISTS socialaccount_socialtoken_app_id_636a42d7;"
        ]

        for command in drop_commands:
            cursor.execute(command)

        connection.commit()
        print("Duplicate indexes dropped successfully.")

    except Exception as error:
        print(f"Error occurred: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    drop_duplicate_indexes()
