# CourseDataBase
Курсовая работа по базам данных. Удачи, солнышко

---
# Кто, что может в моей работе
## Начальная страница
На весь экран окно с авторизацией (регистрацию пока отложим) 

![image](https://user-images.githubusercontent.com/54107546/105728742-8db49d00-5f3d-11eb-8332-384dfe922bae.png)

![image](https://user-images.githubusercontent.com/54107546/105747922-7502b200-5f52-11eb-8be1-c716168a2411.png)


```
Что-то по типу этого. Причем вкладки сверху - Охотник / егерь 
(ЛИБО сказать, что у егерей и охотников по-разному строятся логины, к примеру, егерь_0001, охотник_1234, и уже на этапе 
обработки следить, кто это и выдавать соответствующие права и тогда вторую вкладку сверху можно отдать под регистрацию)

Если забить на деление сверху на охотников и егерей, то в таком случае, у егерей, которые также являются охотниками, 
будет по два логина (как егерь, и как охотник, иначе я не разделю права)
```

---

# Если ты охотник
Охотник может:
- просмотреть все свои путёвки, которые есть в базе данных (никто не говорит тут пор актуальность)
- купить новую путёвку
- прайс лист путёвок только в секторе под номером (номер вводится самим охотником)
- просмотреть все зарегистрированные за ним ружья

![image](https://user-images.githubusercontent.com/54107546/105752863-e04f8280-5f58-11eb-9217-75982f33a25a.png)

![image](https://user-images.githubusercontent.com/54107546/105753932-79cb6400-5f5a-11eb-92ab-2b8f1c5183ae.png)

(Аналогично с оружием, только будет добавить и всё)

---

# Если ты егерь
Егерь может:
- касаемо путёвок
  - выдать новую
  - посмотреть заявки на путёвки
  - удалить (закрыть)
  - увидеть все путёвки только в ЕГО секторе
  - прайс лист путёвок только в ЕГО секторе 
  - отредактировать прайс лист путёвок в ЕГО секторе
  - добавить позицию в прайс лист
  - получить информацию следующего вида: название хозяйства -- номер сектора -- название животного -- количество выданных путёвок -- средняя цена
- касаемо охотников
  - найти охотника по ФИО и получить подробнейшую инфу о нём (включая все путёвки, которые у него есть)
  - получить всех охотников, которых охотятся в ЕГО секторе
  - скорректировать (добавить/удалить) ружьё у конкретного охотника
- касаемо общей инфы
  - получить информацию вида: название хозяйства -- номер сектора -- ФИО егеря + контакты

---

# Продумать
0. Что делать с регистрацией егерей/охотников
0. Что делать, если забыли логин/пароль
