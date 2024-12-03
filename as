#!/bin/bash

# لینک فایل برای دانلود
url="https://dla.p30day.ir/movie/98-09/J-r.2019.2160p.UHD.BluRay.x265-AAAUHD-www.P30Day.com.mkv?66499"

# مسیر ذخیره موقت فایل
save_path="./temp_file.mkv"

# تعداد دفعات دانلود
download_count=100

# دانلود و حذف فایل‌ها
for ((i=1; i<=download_count; i++))
do
  echo "در حال دانلود فایل شماره $i..."
  curl -o "$save_path" "$url"

  if [ $? -eq 0 ]; then
    echo "فایل دانلود شد. حذف فایل..."
    rm -f "$save_path"
  else
    echo "خطا در دانلود فایل."
    break
  fi
done

echo "دانلود و حذف فایل‌ها به پایان رسید."
