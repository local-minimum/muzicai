#!/usr/bin/env python3
from subprocess import Popen, PIPE
from io import BytesIO
import soundfile as sf
import attr


Audio = attr.make_class('Audio', ['bitrate', 'data'])


def mp3towav(path):
    with Popen(['mpg123', '-q', '-w-', path], stdout=PIPE) as proc:
        proc.wait()
        return BytesIO(proc.stdout.read())



def get_audio(path):
    if not path.endswith('.wav'):
        data = mp3mp3towav(path)
        return Audio(*sf.read(data))
    return Audio(*sf.read(path))
