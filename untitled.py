import zipfile

# مسیر فایل زیپ
zip_file_path = 'Chessman.zip'

# مسیر مقصد برای اکسترکت فایل‌ها
extracted_folder_path = 'datasets/'

# اکسترکت فایل‌ها از زیپ
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)

print('فایل‌ها با موفقیت اکسترکت شدند.')
exit()
import requests

# URL تصویر مورد نظر
image_url = 'https://archive.ics.uci.edu/static/public/124/cmu+face+images.zip'

# ارسال درخواست GET برای دریافت تصویر
response = requests.get(image_url)

# بررسی وضعیت درخواست
if response.status_code == 200:
    # ذخیره تصویر در یک فایل محلی
    with open('cmc.zip', 'wb') as file:
        file.write(response.content)
    print('تصویر با موفقیت دانلود شد.')
else:
    print('خطا در دانلود تصویر. وضعیت درخواست:', response.status_code)
