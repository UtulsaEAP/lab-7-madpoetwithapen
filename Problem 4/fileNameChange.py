def fileNameChange(input_file):
    #type your code here

    with open(input_file, 'r') as file:
        for line in file:
            # Remove leading/trailing whitespaces and replace "_photo.jpg" with "_info.txt"
            photo_name = line.strip().replace('_photo.jpg', '_info.txt')
            print(photo_name)

    return

if __name__ == '__main__':
    fileNameChange(input())