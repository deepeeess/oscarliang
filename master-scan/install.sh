#!/bin/bash
sync
platformio run --target upload
i2cdetect -y 1
