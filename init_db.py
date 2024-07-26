
import psycopg2

def init_db(cursor):

    print('reading from csv')
    with open('scripts/patient.csv') as f:
        next(f)
        cursor.copy_from(f, 'patient',sep=',')

    with open('scripts/ncbi_variant.csv') as f:
        next(f)
        cursor.copy_from(f, 'ncbi_variant',sep=',')

    with open('scripts/patient_variant.csv') as f:
        next(f)
        cursor.copy_from(f, 'patient_variant',sep=',')


if __name__ == '__main__':

    conn = psycopg2.connect(
        database="MYDB", user='postgres', password='postgres', host='localhost', port='5433'
    )

    conn.autocommit = True
    cursor = conn.cursor()

    truncate_sql=f"""
        truncate patient;
        truncate ncbi_variant;
        truncate patient_variant;
    """

    init_db(cursor)



