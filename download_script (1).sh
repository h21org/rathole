#!/bin/bash

# لینک فایل
URL="https://github.com/ubuntu/yaru/archive/refs/heads/master.zip"

# نام فایل موقت
TEMP_FILE="temp_file.mp4"

# تعداد دفعات دانلود
DOWNLOAD_COUNT=100  # تعداد دفعات دانلود دلخواه را تنظیم کنید

for ((i=1; i<=DOWNLOAD_COUNT; i++)); do
    echo "دانلود فایل شماره $i از $DOWNLOAD_COUNT ..."
    
    # دانلود فایل
    curl -L -o "$TEMP_FILE" "$URL"

    if [ $? -eq 0 ]; then
        echo "دانلود کامل شد. حذف فایل ..."
        rm -f "$TEMP_FILE"
    else
        echo "خطایی در دانلود رخ داد! دانلود متوقف می‌شود."
        break
    fi
done

echo "دانلود و حذف فایل‌ها به پایان رسید."
