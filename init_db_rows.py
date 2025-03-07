import sqlite3

import numpy as np
import pandas as pd

connection = sqlite3.connect("reflex.db")
crsr = connection.cursor()


def insert_user_status():
    df = pd.read_csv("assets/tables_db_init/user_status.csv", sep=':')
    d = df.to_numpy()
    crsr.executemany("INSERT INTO user_status (name, color) VALUES (?, ?)", d)
    connection.commit()

def insert_user_rights():
    df = pd.read_csv("assets/tables_db_init/user_rights.csv", sep=':')
    d = df.to_numpy()
    d[0,0] = 'None'
    crsr.executemany("INSERT INTO user_right (name) VALUES (?)", d)
    connection.commit()

def insert_item_status():
    df = pd.read_csv("assets/tables_db_init/item_status.csv", sep=':')
    d = df.to_numpy()
    crsr.executemany("INSERT INTO item_status (name, color) VALUES (?, ?)", d)
    connection.commit()

def insert_pictogram_paths():
    df = pd.read_csv("assets/tables_db_init/Piktogramy.csv", sep=':')
    d = df.to_numpy()
    crsr.executemany("INSERT INTO pictogram (path) VALUES (?)", d)
    connection.commit()

def insert_code_statuses():
    d = ['U', 'N']
    crsr.executemany("INSERT INTO ph_code_status (status_name) VALUES (?)", d)
    connection.commit()

def insert_ph_codes():
    df = pd.read_csv("assets/tables_db_init/P.csv", sep=':')
    df['status'] = "U"
    df = df.drop(columns=['Informacje dodatkowe'])
    d = df.to_numpy()

    stat_ids = {}
    for row in crsr.execute("SELECT * FROM ph_code_status"):
        stat_ids[row[1]] = row[0]

    for i in range(len(d)):
        d[i, -1] = stat_ids[d[i, -1]]
        d[i, 0] = d[i, 0].replace(" ", "")

    crsr.executemany("INSERT INTO ph_code (code, warning_text_en, warning_text_pl, id_status) VALUES (?, ?, ?, ?)", d)


    df = pd.read_csv("assets/tables_db_init/H.csv", sep=':')
    df = df.drop(columns=['INFORMACJE DODATKOWE'])
    pictograms = df[['Numer H ', 'NUMER PIKTOGRAMU ']]
    df = df.drop(columns=['NUMER PIKTOGRAMU '])
    d = df.to_numpy()

    for i in range(len(d)):
        d[i, -1] = d[i, -1].replace(" ", "")
        d[i, -1] = stat_ids[d[i, -1]]

        d[i, 0] = d[i, 0].replace(" ", "")

    crsr.executemany("INSERT INTO ph_code (code, warning_text_pl, warning_text_en, id_status) VALUES (?, ?, ?, ?)", d)
    connection.commit()

    dang_classes = ['Działanie Rakotwórcze', 'Działanie Mutagenne', 'Działanie eeprotoksyczne']






    ids_to_connect = []
    d = pictograms.to_numpy()
    # print(d[0,1].split(','))
    for i in range(len(d)):
        if type(d[i, 1])  != str :
            continue

        code_id = -1
        for row in crsr.execute("SELECT id FROM ph_code WHERE ph_code.code == (?)", [d[i, 0].replace(" ", "")]):
            code_id = row[0]

        if code_id == -1:
            continue


        pic_names = d[i, 1].replace(" ", "").replace(";", ",").split(',')

        for p in pic_names:
            for row in crsr.execute("SELECT id FROM pictogram WHERE pictogram.path == (?)", [p]):
                pic_id = row[0]
                crsr.execute("INSERT INTO pictogram_ph_code (id_PH_code, id_pictogram) VALUES (?, ?)", [code_id, pic_id])

    # connection.commit()


def insert_classification(ph_ids: list):
    crsr.execute("INSERT INTO classification DEFAULT values")
    connection.commit()

    c_id = crsr.lastrowid
    c_id = [c_id]*len(ph_ids)
    d = np.array([c_id, ph_ids]).T
    crsr.executemany("INSERT INTO classification_code (id_classification, id_ph_code) values (?, ?) ", d.tolist())
    connection.commit()
    return c_id[0]

def insert_locations():
    crsr.execute("INSERT INTO room (name, department_id) values ('-', 1)")
    connection.commit()

    crsr.execute("INSERT INTO location (name, room_id) values ('-', ?) ",[crsr.lastrowid])
    connection.commit()

def insert_items():
    df = pd.read_csv("assets/tables_db_init/items.csv", sep=':')
    classification_ids = []
    ph_codes = df[['KODY H – oddzielone przecinkami', 'KODY P – oddzielone przecinkami']]
    ph_codes = ph_codes.to_numpy()

    # departments = df['Katedra/Zakład/Instytut']
    # departments = departments.to_numpy()
    # department_ids = []
    # for _d in departments:
    #     for row in crsr.execute("SELECT id from faculty f where f.name == (?)", [_d]):
    #         department_ids.append(row[0])

    for row in crsr.execute("SELECT id from location l where l.name == '-' "):
        loc_id = row[0]

    df = df[['Nazwa Substancji','Numer CAS', 'Producent', 'Ilość substancji']]

    for d in ph_codes:
        d[0] = d[0].replace(" ", "").replace(";", ",").split(',')
        d[1] = d[1].replace(" ", "").replace(";", ",").split(',')

        ph_code_ids = []

        for _d in d[0]:
            for row in crsr.execute("SELECT id FROM ph_code WHERE ph_code.code == (?)", [_d]):
                ph_code_ids.append(row[0])

        for _d in d[1]:
            for row in crsr.execute("SELECT id FROM ph_code WHERE ph_code.code == (?)", [_d]):
                ph_code_ids.append(row[0])

        ids = []
        for row in crsr.execute("SELECT c.id, pc.id FROM classification c JOIN classification_code cc ON cc.id_classification == c.id JOIN ph_code pc ON pc.id  == cc.id_ph_code "):
            ids.append((row[0], row[1]))


        classification_id = -1
        ids = np.array(ids)

        if len(ids) > 0:
            for _id in np.unique(ids[:, 0]):
                buf = ids[ids[:,0] == _id]
                if np.sort(buf[:, 1]).tolist() == np.sort(ph_code_ids).tolist():
                    classification_id = _id
                    break

        if classification_id == -1:
            classification_id = insert_classification(ph_code_ids)

        classification_ids.append(classification_id)

    df['classification'] = classification_ids
    df['exp_date'] = " "
    df['status'] = 2
    df['user_id'] = 1
    df['location'] = loc_id

    d = df.to_numpy()

    crsr.executemany("INSERT INTO item (name, cas, producent, amount, classification_id, exp_date, status_id, user_id, location_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", d.tolist())
    connection.commit()


        # for row in crsr.execute("SELECT id FROM classification WHERE ph_code.code == (?)", [d[i, 0].replace(" ", "")]):
        #     classification_id = row[0]


def main():
    # insert_user_status()
    # insert_item_status()
    # insert_user_rights()
    # insert_pictogram_paths()
    # insert_code_statuses()
    insert_ph_codes()
    # insert_locations()
    # insert_items()

if __name__ == "__main__":
    main()

connection.close()
