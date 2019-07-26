import smtplib
import os
mail_login = os.getenv('MAIL_LOGIN')
mail_password = os.getenv('MAIL_PASSWORD')

my_letter = ("""From: yan.bordousov@yandex.ru
To: shinodyan@yandex.ru 
Subject: Invite
Content-Type: text/plain; charset="UTF-8"; 

Привет, {0}! {1} приглашает тебя на сайт {2}!

{2} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {2}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {2}  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format('Вальдемар', 'Ян', 'devman.org'))

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(mail_login, mail_password)
server.sendmail('yan.bordousov@yandex.ru','shinodyan@yandex.ru', my_letter.encode("UTF-8"))
server.quit()

my_letter.encode("UTF-8")
