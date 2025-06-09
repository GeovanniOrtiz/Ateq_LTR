from datetime import datetime

import mysql.connector as MySQLdb
from PySide6.QtWidgets import QTableWidgetItem
from mysql.connector import Error

class managerDataBase:
    def __init__(self, station):
        """
        acceder a db desde terminal: mysql -u root -p
        Seleccionar db: Use LTR_Production;
        Ver tablas: SHOW TABLES
        ver Estructura de tablas: DESCRIBE Radiator_LTR;
        ver contenido de tabla: SELECT * FROM Radiator_LTR;
        ver contenido limitado: SELECT * FROM Radiator_LTR LIMIT 10;
        ver contenido con state: SELECT * FROM Radiator_LTR WHERE state = '0';
        ver solo algunas Columnas: SELECT id, n_part, n_serie FROM Radiator_LTR;
        ordenar resultados: SELECT * FROM Radiator_LTR ORDER BY id ASC;
                          : SELECT * FROM Radiator_LTR ORDER BY id DESC;
        salir de db: EXIT;
        """
        self.station = station

        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'passwd': 'Airtemp',
            'db': 'LTR_Production'
        }
        self.connection = None
        self.connect()

        self.Device_Table = f"LTR_Estacion_{self.station}"

        self.CreateTableUser("Usuarios")

        if self.station != 6:
            self.CreateTable(self.Device_Table)

        else:
            self.CreateTable_RePrintLabel(self.Device_Table)

        self.addUser("usuarios", "Aldo Ortiz", "7172")

        self.db_backup = f"backup_{self.station}"
        self.CreateTableData(self.db_backup)

    def connect(self):
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = MySQLdb.connect(
                    host=self.db_config['host'],
                    user=self.db_config['user'],
                    passwd=self.db_config['passwd']
                )
                with self.connection.cursor() as cursor:
                    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_config['db']};")
                    cursor.execute(f"USE {self.db_config['db']};")
            except Error as e:
                print(f"Error connecting to database: {e}")
                self.connection = None
            else:
                print("Successfully connected to the database")
    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None
    def reconnect_if_needed(self):
        if self.connection is None or not self.connection.is_connected():
            self.connect()
    def execute_query(self, query, values=None):
        self.reconnect_if_needed()
        if self.connection:
            try:
                with self.connection.cursor(buffered=True) as cursor:
                    cursor.execute(query, values)
                    self.connection.commit()
                    return cursor
            except Error as e:
                print(f"Error executing query: {e}")
                # Ensure there are no unread results before reconnecting
                self.connection.reset_session()
                self.connect()
                return None
        return None
    def CreateTable(self, model):
        self.execute_query(
            f"CREATE TABLE IF NOT EXISTS Radiator_{model}("
                  "id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,"
                  "supplier VARCHAR(3) NOT NULL,"
                  "date DATETIME DEFAULT current_timestamp,"
                  "chamber VARCHAR(1) NOT NULL,"
                  "n_part VARCHAR(10),"
                  "n_serie VARCHAR(10) NOT NULL,"
                  "leak VARCHAR(4) NOT NULL,"
                  "operator VARCHAR(5),"
                  "state VARCHAR(2))"
        )

    def CreateTable_RePrintLabel(self, model):
        self.execute_query(
            f"CREATE TABLE IF NOT EXISTS Radiator_{model}("
                  "id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,"
                  "date DATETIME DEFAULT current_timestamp,"
                  "old_label VARCHAR(60) NOT NULL,"
                  "new_label VARCHAR(60) NOT NULL)"
        )
    def CreateTableUser(self, table):
        self.execute_query(
            f"CREATE TABLE IF NOT EXISTS {table}(" 
            "id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT," 
            "user VARCHAR(40) NOT NULL," 
            "identi VARCHAR(255) NOT NULL);"
        )
    def CreateTableData(self, table):
        self.execute_query(
            f"CREATE TABLE IF NOT EXISTS {table} ("
            "id INT UNSIGNED PRIMARY KEY, "
            "PartNo VARCHAR(40) NOT NULL, "
            "SerialNum INT UNSIGNED NOT NULL);"
        )
        self.execute_query(
            f"INSERT IGNORE INTO {table} (id, PartNo, SerialNum) VALUES "
            "(1, '5QM121251P', 0), "
            "(2, '5QM121251Q', 0), "
            "(3, '5QM121251R', 0), "
            "(4, '5QM121251Q', 0)"
        )

    def GetSerialBackUp(self, part_no):
        cursor = self.execute_query(
            f"SELECT * FROM {self.db_backup} WHERE PartNo = %s",
            (part_no,)
        )
        if cursor:
            result = cursor.fetchone()
            if result:
                return list(result)
        return None

    def GetDataBackUp(self):
        cursor = self.execute_query(
            f"SELECT * FROM {self.db_backup} WHERE id = %s",
            (4,)
        )
        if cursor:
            result = cursor.fetchone()
            if result:
                return list(result)
        return None

    def updateData(self, PartNo, SerialNum):
        table = self.db_backup  # Nombre de la tabla
        query = f"""
            UPDATE {table}
            SET PartNo = %s, SerialNum = %s
            WHERE id = 4
        """

        self.execute_query(query, (PartNo, SerialNum))

    def updateTable_BackUp(self, PartNo, SerialNum):
        table = self.db_backup  # Nombre de la tabla
        query = f"""
            UPDATE {table}
            SET SerialNum = %s
            WHERE PartNo = %s
        """

        self.execute_query(query, (SerialNum, PartNo))
    def addUser(self, table, user, identi):
        try:
            query = f"SELECT * FROM {table} WHERE user = %s"
            values = (user,)
            cursor = self.execute_query(query, values)
            result = cursor.fetchone()

            if result is None:
                # El usuario no existe, insertarlo en la tabla
                insert = f"INSERT INTO {table} (user, identi) VALUES (%s, %s)"
                values = (user, identi)
                self.execute_query(insert, values)
                print("Usuario agregado exitosamente")
            else:
                print("El usuario ya existe en la base de datos")

        except Exception as error:
            print("Error al ejecutar la consulta:", error)

    def Check_nSerie(self, model, partNo, nserie):
        nserie = str(nserie).zfill(7)
        query = f"SELECT COUNT(*) FROM Radiator_{model} WHERE n_serie = %s AND n_part = %s"
        values = (nserie,partNo)
        cursor = self.execute_query(query, values)
        count = cursor.fetchone()[0]
        return count > 0

    def Check_label_Exist(self,model, DMC):
        query = f"SELECT COUNT(*) FROM Radiator_{model} WHERE old_label = %s OR new_label = %s"
        values = (DMC, DMC)
        cursor = self.execute_query(query, values)
        count = cursor.fetchone()[0]
        return count > 0

    def addlabel(self, model, old_lbl, new_lbl):
        try:
            insert = f"INSERT INTO Radiator_{model} (old_label, new_label) VALUES (%s, %s)"
            values = (old_lbl, new_lbl)
            self.execute_query(insert, values)

        except Exception as error:
            print("Error al ejecutar la consulta:", error)

    def addModule(self, supplier_code, chamber, nPart, nSerie, leak, user, nStatus, device):
        try:
            insert = f"INSERT INTO Radiator_{device} (supplier, chamber, n_part, n_serie, leak, operator, state) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (supplier_code, chamber, nPart, nSerie, leak, user, nStatus)
            self.execute_query(insert, values)

        except Exception as error:
            print("Error al ejecutar la consulta:", error)

    def PrintTable(self, model):
        query = f"SELECT * FROM Radiator_%s"
        value = (model,)
        cursor = self.execute_query(query, value)
        table = cursor.fetchall()
        for member in table:
            print(member)

    def DeleteTable(self, model):
        query = f"DROP TABLE IF EXISTS Radiator_{model}"
        self.execute_query(query)

    def ShowLast_data(self, model, qty):
        query= f"SELECT * FROM Radiator_%s ORDER BY id DESC LIMIT %s"
        cursor = self.execute_query(query, (model, qty))
        table = cursor.fetchall()
        return table
    def ShowRange(self, model, inicio, final):
        query = "SELECT * FROM Radiator_%s WHERE id BETWEEN %s AND %s"
        values = (model, inicio, final)
        cursor = self.execute_query(query, values)
        table = cursor.fetchall()
        return table
    def CheckUser(self, table, user):
        query = f"SELECT COUNT(*) FROM {table} WHERE identi = %s"
        values = (user,)
        cursor = self.execute_query(query, values)
        count = cursor.fetchone()[0]
        return count > 0

    def get_data_by_n_serie(self, n_serie, model, part_number):
        n_serie = str(n_serie).zfill(6)
        query = f"SELECT * FROM Radiator_{model} WHERE n_serie = %s AND n_part = %s"
        values = (n_serie, part_number)
        cursor = self.execute_query(query, values)
        result = cursor.fetchone()

        if result:
            # Convertir la tupla a una lista antes de devolverla
            return list(result)
        else:
            return None

    from datetime import datetime

    def count_records_today_original(self, model):
        query = f"""
            SELECT COUNT(*) 
            FROM Radiator_{model} 
            WHERE DATE(date) = %s
        """
        today = datetime.now().date()
        cursor = self.execute_query(query, (today,))

        if cursor:
            count = cursor.fetchone()[0]
            return count
        return 0

    def count_records_today(self, model, part_number=None, station=None):
        query = f"""
            SELECT COUNT(*) 
            FROM Radiator_{model} 
            WHERE DATE(date) = %s
        """
        params = [datetime.now().date()]

        if part_number is not None:
            query += " AND n_part = %s"
            params.append(part_number)

        if station is not None:
            query += " AND chamber = %s"
            params.append(station)

        cursor = self.execute_query(query, tuple(params))

        if cursor:
            count = cursor.fetchone()[0]
            return count
        return 0

    def InsertinTable(self, req, table, qty, partNo):
        print("Insertando datos en tabla")
        if req == 1:
            query = f"""
                SELECT * FROM Radiator_{self.Device_Table}
                WHERE old_label LIKE '%{partNo}%'
                ORDER BY id DESC LIMIT {qty}
            """

            #query = f"SELECT * FROM Radiator_{self.Device_Table} ORDER BY id DESC LIMIT {qty}"
        else:
            print("Solicitud no válida")
            return

        cursor = self.execute_query(query)
        if cursor:
            table.clearContents()
            table.setRowCount(0)
            index = 0

            for row in cursor.fetchall():
                table.setRowCount(index + 1)
                for col, value in enumerate(row):
                    table.setItem(index, col, QTableWidgetItem(str(value)))
                index += 1

            self.invertir_tabla(table)

    def invertir_tabla(self, tabla):
        row_count = tabla.rowCount()
        for i in range(row_count // 2):
            top_row = []
            bottom_row = []

            for column in range(tabla.columnCount()):
                item = tabla.takeItem(i, column)
                if item is not None:
                    top_row.append(item)

            for column in range(tabla.columnCount()):
                item = tabla.takeItem(row_count - 1 - i, column)
                if item is not None:
                    bottom_row.append(item)

            for column in range(tabla.columnCount()):
                if top_row:
                    tabla.setItem(row_count - 1 - i, column, top_row.pop(0))
                if bottom_row:
                    tabla.setItem(i, column, bottom_row.pop(0))