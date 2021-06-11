# CourseDataBase
Курсовая работа по базам данных. Удачи, солнышко

---
# Кто что может в моей работе
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
- [x] просмотреть все свои путёвки, которые есть в базе данных
- [ ] купить новую путёвку
- [x] прайс лист путёвок только в секторе под номером (номер вводится самим охотником)

![image](https://user-images.githubusercontent.com/54107546/105752863-e04f8280-5f58-11eb-9217-75982f33a25a.png)

![image](https://user-images.githubusercontent.com/54107546/105753932-79cb6400-5f5a-11eb-92ab-2b8f1c5183ae.png)

---

# Если ты егерь
Егерь может:
- касаемо путёвок
  - [x] выдать новую
  - [ ] посмотреть заявки на путёвки
  - [x] удалить (закрыть)
  - [x] увидеть все путёвки только в ЕГО секторе
  - [x] прайс лист путёвок только в ЕГО секторе 
  - [x] пометить позицию в прайс листе ЕГО сектора как неактуальную
  - [X] добавить позицию в прайс лист
  - [X] получить информацию следующего вида: название хозяйства -- номер сектора -- название животного -- количество выданных путёвок -- средняя цена
- касаемо охотников
  - [x] найти охотника по ФИО и получить подробнейшую инфу о нём (включая все путёвки, которые у него есть)
  - [x] получить всех охотников, которых охотятся в ЕГО секторе
  - // скорректировать (добавить/удалить) ружьё у конкретного охотника


Все пользователи могут:
  - [x] получить информацию вида: название хозяйства -- номер сектора -- ФИО егеря + контакты

---

# Продумать
0. Что делать с регистрацией егерей/охотников
0. Что делать, если забыли логин/пароль

---
---
# Это было ожидание, а теперь РЕАЛЬНОСТЬ
## 1. Вход
![image](https://user-images.githubusercontent.com/54107546/121745442-f7a89a00-cb0c-11eb-9c6e-1e73dfcc27c0.png)

## 2. Регистрация
![image](https://user-images.githubusercontent.com/54107546/121745475-042cf280-cb0d-11eb-8ae7-485c1c7dfcba.png)

### 2.1 охотника
![image](https://user-images.githubusercontent.com/54107546/121745003-70f3bd00-cb0c-11eb-9a97-38230d246ef2.png)

### 2.2 егеря
![image](https://user-images.githubusercontent.com/54107546/121745175-bca66680-cb0c-11eb-97a2-3f8c5e6a9d90.png)

### 2.3 администратора
![image](https://user-images.githubusercontent.com/54107546/121744823-24a87d00-cb0c-11eb-9cf3-0dc2bfe7fcb5.png)

# И ещё очень-очень много страниц
