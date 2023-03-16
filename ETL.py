import DBMS 
import Songs_Dataset as SData

## Part 1 - Moving SongsDataset to database

def Process_ETL():
    DBMS.create_table(DBMS.cursor)

    if DBMS.songs_double_check():
        print('Warning For Duplicate Records!')
    else:
        for i in SData.dataSet.index:
            values = [SData.dataSet['artist_id'][i], SData.dataSet['serial_id'][i], SData.dataSet['song'][i], SData.dataSet['title'][i]]
            if SData.dataSet.index[i] % 1000 == 0:
                print(f'{SData.dataSet.index[i]}, Has Been Loaded!')
            DBMS.songs_insert(DBMS.cursor, values)
            DBMS.commit()