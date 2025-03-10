import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test= json.load(file)
            return test
    except FileNotFoundError:
        return []
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    for index , video  in enumerate(videos,start=1):
        print(f'{index}. Name: {video['name']}, Duration : {video['time']}')

def add_video(videos):
    name=input('Enter Video Name: ')
    time=input('Enter Video Duration: ')
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)
def update_video(videos):
    list_all_videos(videos)
    index=int(input('Enter video no for update: '))
    if 1<=index<=len(videos):
        name=input('Enter New Name: ')
        time=input('Enter New Duration: ')
        videos[index-1]={'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print('Invalid video number.')


def delete_video(videos):
    list_all_videos(videos)
    index=int(input('Enter video no for deletion: '))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print('Invalid video number.')
def main():
    videos=load_data()
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
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print('Goodbye!')
                break
            case _:
                print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()