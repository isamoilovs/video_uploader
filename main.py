import ffmpeg_streaming
import sys
import os
import datetime
import shutil

from ffmpeg_streaming import Representation, Size, Bitrate, Formats
from vtt_maker import get_vtt
from upload import upload_video
from cms_player import get_code_for_cms_player


def monitor(ffmpeg, duration, time_, time_left, process):
    per = round(time_ / duration * 100)
    sys.stdout.write(
        "\rТранскодируем видео...(%s%%) %s left [%s%s]" %
        (per, datetime.timedelta(seconds=int(time_left)), '#' * per, '-' * (100 - per))
    )
    sys.stdout.flush()


def transcode_video(class_id: str):
    video = ffmpeg_streaming.input(class_id + '.mp4')
    _270p_160kbps = Representation(Size(480, 480), Bitrate(160 * 1024, 128 * 1024))
    _360p_700kbps = Representation(Size(640, 640), Bitrate(700 * 1024, 128 * 1024))
    _360p_1500kbps = Representation(Size(640, 640), Bitrate(1500 * 1024, 192 * 1024))
    _540p_2000kbps = Representation(Size(960, 960), Bitrate(2000 * 1024, 192 * 1024))
    _720p_5000kbps = Representation(Size(1280, 1280), Bitrate(5000 * 1024, 320 * 1024))
    _1080p_7500kbps = Representation(Size(1920, 1920), Bitrate(7500 * 1024, 320 * 1024))

    hls = video.hls(Formats.h264())

    hls.representations(_270p_160kbps,
                        _360p_700kbps,
                        _360p_1500kbps,
                        _540p_2000kbps,
                        _720p_5000kbps,
                        _1080p_7500kbps)

    hls.output('./output/' + str(class_id) + '/media/' + str(class_id), monitor=monitor)
    get_vtt(10, class_id)
    shutil.make_archive('./output/' + str(class_id), 'tar', './output/' + str(class_id))
    shutil.rmtree('./output/' + str(class_id))
    upload_video(class_id)
    os.remove('./output/' + str(class_id) + '.tar')
    get_code_for_cms_player(class_id)


video_id = input('Введите номер урока: ')
transcode_video(video_id)
