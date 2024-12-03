#!/bin/bash

# لینک فایل بزرگ برای دانلود
url="https://speed.hetzner.de/10GB.bin" # تغییر دهید به فایل دلخواه

# تعداد دفعات دانلود
download_count=10

# دانلود و حذف فایل‌ها
for ((i=1; i<=download_count; i++))
do
  echo "در حال دانلود فایل شماره $i..."
  curl -o /dev/null "$url"
  
  if [ $? -eq 0 ]; then
    echo "دانلود موفقیت‌آمیز بود."
  else
    echo "خطا در دانلود."
    break
  fi
done

echo "دانلود به پایان رسید."
