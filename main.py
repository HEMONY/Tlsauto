import os

import telebot

from telebot import TeleBot, types 

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import time

import random

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

import undetected_chromedriver as uc





# معلومات تسجيل الدخول

token = 'TOKEN'

LOGIN = "EMAIL"#بريدك الالكنروني

PASSWORD = "PASSWORD"#كلمة السر

bot = telebot.TeleBot(token)

admin = [6760970896, 588461026]

# إعداد خيارات المتصفح

CHANNEL_ID = '@tls_no'

#centers 



centerInfo= {  'TlsGermanyRabat_FamilyVisit': {

    'code': 'maRBA2de',    'country': 'de',

    'aptType': 'court_sejour',    'issueCountry': 'ma',

    'title': 'TLS Allemagne à Rabat',    'prefix': 'visas-'

  },  'TlsGermanyRabat_Tourism': {

    'code': 'maRBA2de',    'country': 'de',

    'aptType': 'tourism',    'issueCountry': 'ma',

    'title': 'TLS Allemagne à Rabat',    'prefix': 'visas-'

  },  'TlsGermanyRabat_BlueCard': {

    'code': 'maRBA2de',    'country': 'de',

    'aptType': 'Public_other',    'issueCountry': 'ma',

    'title': 'TLS Allemagne à Rabat',    'prefix': 'visas-'

  },  'TlsFranceFes_Case1': {

    'code': 'maFEZ2fr',    'country': 'fr',

    'aptType': 'Primo',    'issueCountry': 'ma',

    'title': 'TLS France à Fès',    'prefix': ''

  },  'TlsFranceFes_Case2': {

    'code': 'maFEZ2fr',

    'country': 'fr',    'aptType': 'Renouvellement',

    'issueCountry': 'ma',    'title': 'TLS France à Fès',

    'prefix': ''  },

  'TlsFranceFes_Case3': {    'code': 'maFEZ2fr',

    'country': 'fr',    'aptType': 'Circulation',

    'issueCountry': 'ma',    'title': 'TLS France à Fès',

    'prefix': ''  },

  'TlsFranceFes_AscendantFrancais': {    'code': 'maFEZ2fr',

    'country': 'fr',    'aptType': 'Ascendant%20de%20Francais%20CS',

    'issueCountry': 'ma',    'title': 'TLS France à Fès',

    'prefix': ''  },

  'TlsFranceOujda_Case1': {    'code': 'maOUD2fr',

    'country': 'fr',    'aptType': 'Primo',

    'issueCountry': 'ma',    'title': 'TLS France à Oujda',

    'prefix': ''  },

  'TlsFranceOujda_Case2': {    'code': 'maOUD2fr',

    'country': 'fr',    'aptType': 'Renouvellement',

    'issueCountry': 'ma',    'title': 'TLS France à Oujda',

    'prefix': ''  },

  'TlsFranceOujda_Case3': {    'code': 'maOUD2fr',

    'country': 'fr',    'aptType': 'Circulation',

    'issueCountry': 'ma',    'title': 'TLS France à Oujda',

    'prefix': ''  },

  'TlsFranceOujda_AscendantFrancais': {    'code': 'maOUD2fr',

    'country': 'fr',    'aptType': 'Ascendant%20de%20Francais%20CS',

    'issueCountry': 'ma',    'title': 'TLS France à Oujda',

    'prefix': ''

  },  'TlsFranceCasablanca_Case1': {

    'code': 'maCAS2fr',    'country': 'fr',

    'aptType': 'Grand%20Public%20PRIMO',    'issueCountry': 'ma',

    'title': 'TLS France à Casablanca',    'prefix': ''

  },  'TlsFranceCasablanca_Case2': {

    'code': 'maCAS2fr',    'country': 'fr',

    'aptType': 'Grand%20Public%20VISE',    'issueCountry': 'ma',

    'title': 'TLS France à Casablanca',    'prefix': ''

  },  'TlsFranceCasablanca_Case3': {

    'code': 'maCAS2fr',    'country': 'fr',

    'aptType': 'Grand%20Public%20CIRCULATION',    'issueCountry': 'ma',

    'title': 'TLS France à Casablanca',    'prefix': ''

  },  'TlsFranceCasablanca_AscendantFrancais': {

    'code': 'maCAS2fr',    'country': 'fr',

    'aptType': 'Ascendant%20de%20Francais%20CS',    'issueCountry': 'ma',

    'title': 'TLS France à Casablanca',    'prefix': ''

  },  'TlsFranceTanger_Case1': {

    'code': 'maTNG2fr',    'country': 'fr',

    'aptType': 'PRIMO',    'issueCountry': 'ma',

    'title': 'TLS France à Tanger',    'prefix': ''

  },  'TlsFranceTanger_Case2': {

    'code': 'maTNG2fr',    'country': 'fr',

    'aptType': 'Renouvellement',    'issueCountry': 'ma',

    'title': 'TLS France à Tanger',    'prefix': ''

  },  'TlsFranceTanger_Case3': {

    'code': 'maTNG2fr',    'country': 'fr',

    'aptType': 'Circulation',    'issueCountry': 'ma',

    'title': 'TLS France à Tanger',    'prefix': ''

  },  'TlsFranceTanger_AscendantFrancais': {

    'code': 'maTNG2fr',    'country': 'fr',

    'aptType': 'Ascendant%20de%20Francais%20CS',    'issueCountry': 'ma',

    'title': 'TLS France à Tanger',    'prefix': ''

  },  'TlsFranceAgadir_Case1': {

    'code': 'maAGA2fr',    'country': 'fr',

    'aptType': 'Grand%20Public%20PRIMO',    'issueCountry': 'ma',

    'title': 'TLS France à Agadir',    'prefix': ''

  },  'TlsFranceAgadir_Case2': {

    'code': 'maAGA2fr',    'country': 'fr',

    'aptType': 'Grand%20Public%20VISE',    'issueCountry': 'ma',

    'title': 'TLS France à Agadir',    'prefix': ''

  },



'TlsFranceAgadir_Case3': {

    'code': 'maAGA2fr',    'country': 'fr',

    'aptType': 'Grand%20Public%20CIRCULATION',    'issueCountry': 'ma',

    'title': 'TLS France à Agadir',    'prefix': ''

  },  'TlsFranceAgadir_AscendantFrancais': {

    'code': 'maAGA2fr',    'country': 'fr',

    'aptType': 'Ascendant%20de%20Francais%20CS',    'issueCountry': 'ma',

    'title': 'TLS France à Agadir',    'prefix': ''

  },  'TlsFranceMarrakech_Case1': {

    'code': 'maRAK2fr',    'country': 'fr',

    'aptType': 'Grand%20Public%20PRIMO',

    'issueCountry': 'ma',    'title': 'TLS France à Marrakech',

    'prefix': ''  },

  'TlsFranceMarrakech_Case2': {    'code': 'maRAK2fr',

    'country': 'fr',    'aptType': 'Grand%20Public%20VISE',

    'issueCountry': 'ma',    'title': 'TLS France à Marrakech',

    'prefix': ''  },

  'TlsFranceMarrakech_Case3': {    'code': 'maRAK2fr',

    'country': 'fr',    'aptType': 'Grand%20Public%20CIRCULATION',

    'issueCountry': 'ma',    'title': 'TLS France à Marrakech',

    'prefix': ''  },

  'TlsFranceMarrakech_AscendantFrancais': {    'code': 'maRAK2fr',

    'country': 'fr',    'aptType': 'Ascendant%20de%20Francais%20CS',

    'issueCountry': 'ma',    'title': 'TLS France à Marrakech',

    'prefix': ''  },

  'TlsFranceRabat_Case1': {    'code': 'maRBA2fr',

    'country': 'fr',    'aptType': 'Primo',

    'issueCountry': 'ma',    'title': 'TLS France à Rabat',

    'prefix': ''  },

  'TlsFranceRabat_Case2': {    'code': 'maRBA2fr',

    'country': 'fr',    'aptType': 'Renouvellement',

    'issueCountry': 'ma',    'title': 'TLS France à Rabat',

    'prefix': ''  },

  'TlsFranceRabat_Case3': {    'code': 'maRBA2fr',

    'country': 'fr',    'aptType': 'Circulation',

    'issueCountry': 'ma',

    'title': 'TLS France à Rabat',    'prefix': ''

  },  'TlsFranceRabat_AscendantFrancais': {

    'code': 'maRBA2fr',    'country': 'fr',

    'aptType': 'Ascendant%20de%20Francais%20CS',    'issueCountry': 'ma',

    'title': 'TLS France à Rabat',    'prefix': ''

  },  'TlsFranceRabat_StudentLongTerm': {

    'code': 'maRBA2fr',    'country': 'fr',

    'aptType': 'long%20sejour%20etudiant',    'issueCountry': 'ma',

    'title': 'TLS France à Rabat',    'prefix': ''

  },  'TlsFranceAnnaba_Case1': {

    'code': 'dzAAE2fr',    'country': 'fr',

    'aptType': 'premiere_demande',    'issueCountry': 'dz',

    'title': 'TLS France à Annaba',    'prefix': ''

  },  'TlsFranceAnnaba_Case2': {

    'code': 'dzAAE2fr',    'country': 'fr',

    'aptType': 'Frequent',    'issueCountry': 'dz',

    'title': 'TLS France à Annaba',    'prefix': ''

  },  'TlsFranceAnnaba_Case3': {

    'code': 'dzAAE2fr',    'country': 'fr',

    'aptType': 'Circulation',    'issueCountry': 'dz',

    'title': 'TLS France à Annaba',    'prefix': ''

  },}

center_code = {'Annaba': 'dzAAE2fr', 



                'Fes': ' maFEZ2fr',



                'Oujda': ' maOUD2fr',



                'Casablanca': ' maCAS2fr',



                'Tanger': ' maTNG2fr',



                'Agadir': ' maAGA2fr',



                'Marrakech': ' maRAK2fr', 





                'Rabat': ' maRBA2fr',

                'Oran': 'dzORN2fr'}

# دالة البداية

# دالة إنشاء لوحة الأزرار بناءً على البيانات

def generate_buttons():

    markup = InlineKeyboardMarkup(row_width=2)

    buttons = []

    for key, value in center_code.items():

        title = f"{key}"

        buttons.append(InlineKeyboardButton(text=key, callback_data=value))

    markup.add(*buttons)

    return markup

@bot.message_handler(commands=['start'])

def send_welcome(message):

    if message.chat.id not in admin:

        bot.send_message(message.chat.id, f'Sorry {moa} :( you are not able to use bot ')

        

   

        return 

    moa = message.from_user.first_name

    bot.send_message(message.chat.id, f'Hi {moa} :) I am bot for you to check you account activity every sec...\n!! only you and developer can use bot command!!')

    markup = generate_buttons()

    bot.send_message(message.chat.id, "اختر المركز  من الخيارات التالية:", reply_markup=markup)



    

    #main_operation()

    

# التعامل مع اختيار الزر

@bot.callback_query_handler(func=lambda call: True)

def callback_handler(call):

    c_code = f'{call.data}'

    Type = None

    if c_code in ['dzAAE2fr', 'dzORN2fr']:

        

        Type = 'premier_demand'

    else:

        Type = 'Cas1\nCas2\nCas3'

    bot.send_message(call.message.chat.id, "Loadind...")

    bot.send_message(CHANNEL_ID, main_operation(c_code, Type))

    

def main_operation(code, t):

    # إعداد المتصفح

    # إعداد الخيارات للمتصفح

    

    driver = uc.Chrome()



    try:

        # الانتقال إلى صفحة تسجيل الدخول

        print("فتح صفحة تسجيل الدخول...")

        driver.get(f"https://fr.tlscontact.com/login/dz/{code}/")



        # الانتظار حتى يتم تحميل العنصر الأول

        WebDriverWait(driver, 30).until(

            EC.presence_of_element_located((By.XPATH, '//*[@id="tls-navbar"]/div/div[2]/div[5]/div[1]/a'))

        )

        

        # انقر على زر تسجيل الدخول

        driver.find_element(By.XPATH, '//*[@id="tls-navbar"]/div/div[2]/div[5]/div[1]/a').click()

        time.sleep(15)

        time.sleep(random.uniform(2, 4))  # تأخير عشوائي لمحاكاة الإنسان

        driver.execute_script("window.scrollBy(0, 1500);")



        # إدخال بيانات تسجيل الدخول

        print("إدخال بيانات تسجيل الدخول...")

        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(LOGIN)

        time.sleep(random.uniform(1, 2))

        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(PASSWORD)

        time.sleep(random.uniform(1, 2))

        driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

        

        # الانتظار حتى يتم تحميل الصفحة بعد تسجيل الدخول

        print("انتظار تحميل الصفحة الرئيسية...")

        time.sleep(10)

        WebDriverWait(driver, 20).until(

            EC.presence_of_element_located((By.CLASS_NAME, "tls-heading-1"))

        )

        print("تم تسجيل الدخول بنجاح!")



        # تنفيذ الإجراء التالي إذا لزم الأمر

        driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div/div/div[1]/table/tr/th[2]/td[3]/button').click()

        time.sleep(10)

        driver.execute_script("window.scrollBy(0, 3000);")

        WebDriverWait(driver, 20).until(

            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/button'))

        )

        driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[2]/button').click()

        #driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div[3]/div[2]/div/div/div[2]/div[4]/div/button').click()

        time.sleep(10)

        driver.execute_script("window.scrollBy(0, 3000);")

        # checking loop



        try:

            # التحقق من وجود العنصر الأساسي

            driver.find_element(By.CLASS_NAME, 'tls-time-group')

            cc_code = ''

            for i in center_code:

                if center_code[i] == code:

                    cc_code += i

            res = f"Type = {t}\nCenter = {cc_code}\n\n"

            op = False  # للتحقق من إكمال العملية بنجاح

            

            



            while not op:

                try:

                    # استخراج جميع العناصر التي تحمل الفئة "tls-time-group"

                    time_groups = driver.find_elements(By.CLASS_NAME, "tls-time-group--slot")



                    for group in time_groups:

                        # استخراج التاريخ واسم اليوم

                        date_element = group.find_element(By.CLASS_NAME, "tls-time-group--header-title")

                        day_element = group.find_element(By.CLASS_NAME, "tls-time-group--header-sub-title")

                        date = date_element.text.strip()

                        day = day_element.text.strip()



                        # استخراج جميع الأوقات المتوفرة

                        time_buttons = group.find_elements(By.CLASS_NAME, "tls-time-unit")

                        times = [button.text.strip() for button in time_buttons if button.text.strip()]



                        # تنسيق النتائج

                        res += f"📅 **{date} ({day})**\n"

                        if times:

                            res += "🕒 Available Times: " + ", ".join(times) + "\n\n"

                        else:

                            res += "❌ No available times for this day.\n\n"

                    

                    # إنهاء الحلقة عند النجاح

                    try:

                        dures = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div[2]/div[2]/div[2]/button')

                        while dures:

                            dures.click()

                            time.sleep(5)

                            time_groups = driver.find_elements(By.CLASS_NAME, "tls-time-group--slot")



                            for group in time_groups:

                                # استخراج التاريخ واسم اليوم

                                date_element = group.find_element(By.CLASS_NAME, "tls-time-group--header-title")

                                day_element = group.find_element(By.CLASS_NAME, "tls-time-group--header-sub-title")

                                date = date_element.text.strip()

                                day = day_element.text.strip()



                                # استخراج جميع الأوقات المتوفرة

                                time_buttons = group.find_elements(By.CLASS_NAME, "tls-time-unit")

                                times = [button.text.strip() for button in time_buttons if button.text.strip()]



                                # تنسيق النتائج

                                res += f"📅 **{date} ({day})**\n"

                                if times:

                                    res += "🕒 Available Times: " + ", ".join(times) + "\n\n"

                                else:

                                    res += "❌ No available times for this day.\n\n"

                    

                    except:

                        bot.send_message(CHANNEL_ID, f'{res}')

                        time.sleep(random.uniform(100, 180))

                        driver.refresh()

                        time.sleep(random.uniform(1, 10))

                        try:

                          # استخراج جميع العناصر التي تحمل الفئة "tls-time-group"

                          time_groups = driver.find_elements(By.CLASS_NAME, "tls-time-group--slot")



                          for group in time_groups:

                              # استخراج التاريخ واسم اليوم

                              date_element = group.find_element(By.CLASS_NAME, "tls-time-group--header-title")

                              day_element = group.find_element(By.CLASS_NAME, "tls-time-group--header-sub-title")

                              date = date_element.text.strip()

                              day = day_element.text.strip()



                              # استخراج جميع الأوقات المتوفرة

                              time_buttons = group.find_elements(By.CLASS_NAME, "tls-time-unit")

                              times = [button.text.strip() for button in time_buttons if button.text.strip()]



                              # تنسيق النتائج

                              res += f"📅 **{date} ({day})**\n"

                              if times:

                                  res += "🕒 Available Times: " + ", ".join(times) + "\n\n"

                              else:

                                  res += "❌ No available times for this day.\n\n"

                          

                          # إنهاء الحلقة عند النجاح

                          try:

                              dures = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div[2]/div[2]/div[2]/button')

                              while dures:

                                  dures.click()

                                  time.sleep(5)

                                  time_groups = driver.find_elements(By.CLASS_NAME, "tls-time-group--slot")



                                  for group in time_groups:

                                      # استخراج التاريخ واسم اليوم

                                      date_element = group.find_element(By.CLASS_NAME, "tls-time-group--header-title")

                                      day_element = group.find_element(By.CLASS_NAME, "tls-time-group--header-sub-title")

                                      date = date_element.text.strip()

                                      day = day_element.text.strip()



                                      # استخراج جميع الأوقات المتوفرة

                                      time_buttons = group.find_elements(By.CLASS_NAME, "tls-time-unit")

                                      times = [button.text.strip() for button in time_buttons if button.text.strip()]



                                      # تنسيق النتائج

                                      res += f"📅 **{date} ({day})**\n"

                                      if times:

                                          res += "🕒 Available Times: " + ", ".join(times) + "\n\n"

                                      else:

                                          res += "❌ No available times for this day.\n\n"

                            #if res == res:

                          except:pass

                        except:pass



                        

                        



                except Exception as e:

                    print(f"حدث خطأ غير متوقع: {e}")

                    while True:

                      try:

                        # استخراج جميع العناصر التي تحمل الفئة "tls-time-group"

                        time_groups = driver.find_elements(By.CLASS_NAME, "tls-time-group--slot")



                        for group in time_groups:

                            # استخراج التاريخ واسم اليوم

                            date_element = group.find_element(By.CLASS_NAME, "tls-time-group--header-title")

                            day_element = group.find_element(By.CLASS_NAME, "tls-time-group--header-sub-title")

                            date = date_element.text.strip()

                            day = day_element.text.strip()



                            # استخراج جميع الأوقات المتوفرة

                            time_buttons = group.find_elements(By.CLASS_NAME, "tls-time-unit")

                            times = [button.text.strip() for button in time_buttons if button.text.strip()]



                            # تنسيق النتائج

                            res += f"📅 **{date} ({day})**\n"

                            if times:

                                res += "🕒 Available Times: " + ", ".join(times) + "\n\n"

                            else:

                                res += "❌ No available times for this day.\n\n"

                      

                        # إنهاء الحلقة عند النجاح
