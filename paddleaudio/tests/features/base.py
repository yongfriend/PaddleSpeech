# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import unittest

import numpy as np
import paddle

from paddleaudio import load

file_dir = os.path.dirname(os.path.realpath(__file__))


class FeatTest(unittest.TestCase):
    def setUp(self):
        self.initParmas()
        self.initWavInput()
        self.setUpDevice()

    def setUpDevice(self, device='cpu'):
        paddle.set_device(device)

    def initWavInput(self):
        self.waveform, self.sr = load(
            os.path.abspath(os.path.join(file_dir, '../wav/zh.wav')))
        self.waveform = self.waveform.astype(
            np.float32
        )  # paddlespeech.s2t.transform.spectrogram only supports float32 
        dim = len(self.waveform.shape)

        assert dim in [1, 2]
        if dim == 1:
            self.waveform = np.expand_dims(self.waveform, 0)

    def initParmas(self):
        raise NotImplementedError
