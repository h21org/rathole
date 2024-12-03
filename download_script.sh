
#!/bin/bash

# لینک فایل
URL="https://caspian18.cdn.asset.aparat.com/aparat-video/1fae4849f72d1f754c4c1ddcc06dd4d061973396-720p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImY0M2M0NmM1YTE2ZjNkMTlkYjgxYjhhM2U3ZDVmNzBlIiwiZXhwIjoxNzMzMjgxNDg1LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.ynZsMVPG4gHpjP0GQd1XKe6GR_gyte3qBGS4CfEnISI"

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
