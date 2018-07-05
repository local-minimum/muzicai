#!/usr/bin/env python3
from subprocess import run
from io import BytesIO
import soundfile as sf
import attr
import os
import numpy as np
from tempfile import TemporaryDirectory

Audio = attr.make_class('Audio', ['data', 'bitrate'])


def mp3towav(mp3, wav):
    args = ['mpg123', '-q', '-w', wav, mp3]
    run(args)



def get_audio(path):
    try:
        a = Audio(*sf.read(path))
    except RuntimeError:
        with TemporaryDirectory() as tmpdir:
            wav = os.path.join(tmpdir, os.path.basename(path))
            mp3towav(path, wav)
            a = Audio(*sf.read(wav))
    return a


def mono_as_stereo(audio):
    if audio.shape[1] == 1:
        return Audio(
            np.vstack((audio.data[:, 0], audio.data[:, 0])).T,
            audio.bitrate,
        )
    return audio
