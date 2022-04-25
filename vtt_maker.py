import numpy as np
import cv2
import os

#Просто запустить в одной директории с видео и картинкой empty.bmp
#(белый прямоугольником размером
#как константы ниже). На выходе .vtt файл и спрайты.
#Обратите внимание, что мы режем скриншоты по вертикали надвое,
#так как видео склеено с двух камер.

THUMBNAIL_WIDTH = 160
THUMBNAIL_HEIGHT = 90


# seconds to 00:00:00
def sec_to_time(t):
    h = t // 3600
    m = (t // 60) % 60
    s = t % 60
    if h < 10:
        h = '0' + str(h)
    if m < 10:
        m = '0' + str(m)
    else:
        m = str(m)
    if s < 10:
        s = '0' + str(s)
    else:
        s = str(s)
    t = h + ':' + m + ':' + s
    return t


def build_vtt(timeline_step, output_vtt_file_name, remote_output_src):
    VttFile = open('./output/' + output_vtt_file_name+'/vtt/' + output_vtt_file_name + '.vtt', 'w')
    VttFile.write('WEBVTT\n')
    sprites = ['jpeg']
    timer = 0
    for root, dirs, files in os.walk(r'.'):
        for file in files:
            if file[-4:] in sprites:
                for row in range(5):
                    for col in range(5):
                        VttFile.write(str(sec_to_time(timer)) + ' --> ' + str(sec_to_time(timer + timeline_step)) + '\n')
                        VttFile.write(remote_output_src + file + '#xywh=' + str(col * THUMBNAIL_WIDTH) + ',' + str(row * THUMBNAIL_HEIGHT) + ',160,90\n')

                        timer += timeline_step


def thumbnails(file, timeline_step, output_vtt_file_name):
    file = file
    print('Создаем Thumbnails. Подождите...')
    path = r'.'
    os.chdir(path)
    vidcap = cv2.VideoCapture(os.path.abspath(path)+'/'+file)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    time_line_step = timeline_step
    total_frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    time_line = int(total_frames // fps)
    n = time_line//time_line_step
    frames_step = total_frames//n
    a = []
    b = []

    for i in range(n):
        vidcap.set(1, i * frames_step)
        success, image = vidcap.read()
        width = THUMBNAIL_WIDTH
        height = THUMBNAIL_HEIGHT
        image = cv2.resize(image, (width, height * 2))
        image = image[0:int(height), 0:width]
        cv2.imwrite('image' + str(i) + '.jpg', image)
        a.append('image' + str(i) + '.jpg')

    vidcap.release()

    for i in range(((n + 24) // 25 * 25) - n):
        a.append('./assets/empty.bmp')

    #склеиваем видео по 5 по горизонтали
    def glue(img1, img2, img3, img4, img5, x):
        i1 = cv2.imread(img1)
        i2 = cv2.imread(img2)
        i3 = cv2.imread(img3)
        i4 = cv2.imread(img4)
        i5 = cv2.imread(img5)
        vis = np.concatenate((i1, i2, i3, i4, i5), axis = 1)
        cv2.imwrite('out' + str(x) + '.png', vis)
        b.append('out' + str(x) + '.png')

    x = 0
    while x < len(a):
        glue(a[x], a[x+1], a[x+2], a[x+3], a[x+4], x)
        x += 5

    #склеиваем видео по 5 по вертикали
    def glue2(img1, img2, img3, img4, img5, y):
        i1 = cv2.imread(img1)
        i2 = cv2.imread(img2)
        i3 = cv2.imread(img3)
        i4 = cv2.imread(img4)
        i5 = cv2.imread(img5)
        vis = np.concatenate((i1, i2, i3, i4, i5), axis=0)
        cv2.imwrite('./output/' + output_vtt_file_name + '/vtt/sprite' + str(y // 5 + 1) + '.jpeg', vis)
    y = 0
    while y < len(b):
        glue2(b[y], b[y+1], b[y+2], b[y+3], b[y+4], y)
        y += 5

    #уборка
    c = ['jpg', 'png']
    for root, dirs, files in os.walk(path):    
        for file in files:
            if file[-3:] in c:
                os.remove(file)
    print('Готово! Thumbnails собраны!')


video = ['wmv', 'mp4', 'avi', 'mov', 'MP4', '.rm', 'mkv']


def get_vtt(timeline_step: int, output_vtt_file_name: str):
    remote_output_src = 'https://16402e8c-8037-46dd-8c51-bfd292a294ea.selcdn.net/' + output_vtt_file_name + '/vtt/'  # ссылка на папку на хосте (обязательно httpS!)
    for root, dirs, files in os.walk(r'.'):
        for file in files:
            if file[-3:] in video:
                print()
                print('В обработке файл: ' + file)
                if not os.path.isdir('./output/' + output_vtt_file_name + '/vtt'):
                    os.mkdir('./output/' + output_vtt_file_name + '/vtt')
                thumbnails(file, timeline_step, output_vtt_file_name)
                build_vtt(timeline_step, output_vtt_file_name, remote_output_src)
