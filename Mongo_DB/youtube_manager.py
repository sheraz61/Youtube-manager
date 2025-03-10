import pymongo
from bson import ObjectId

# create a connection
client = pymongo.MongoClient("use connection string")
# create a database
mydb = client["youtubeManager"]
# create a collection
mycol = mydb["videos"]
def list_all_videos():
    for video in mycol.find():
        print(f'ID: {video['_id']}, Title: {video['name']}, Time: {video['time']}')

def add_video(name, time):
    mycol.insert_one({'name':name,'time':time})

def update_video(id, name, time):
    mycol.update_one({'_id':ObjectId(id)},{'$set':{'name':name,'time':time}})

def delete_video(id):
    mycol.delete_one({'_id':ObjectId(id)})


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
          


if __name__ == '__main__':
    main()