import sqlite3
con=sqlite3.connect('youtube_vedio_db')
cursor=con.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY, 
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(id, name, time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?", (name, time, id))
    con.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id=?", (id,))
    con.commit()


def main():
   while True:
        print('YouTube Vedio Management Service: | Choose your chooices...')
        print('1. List all YouTube videos')
        print('2. Add a YouTube video')
        print('3. Update a YouTube video')
        print('4. Remove a YouTube video')
        print('5. Exit')
        choice = input('Enter your choice (1-5): ')

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name=input('Enter video name: ')
                time=input('Enter video duration: ')
                add_video(name,time)
            case '3':
                id=input('Enter id for updation: ')
                name=input('Enter video name: ')
                time=input('Enter video duration: ')
                update_video(id,name,time)
            case '4':
                id=input('Enter id for delete: ')
                delete_video(id)
            case '5':
                print('Goodbye!')
                break
            case _:
                print('Invalid choice. Please try again.')
   con.close()       


if __name__ == '__main__':
    main()