import pyautogui
import sys
import random
from colorama import *
import time

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

start_time = time.time()

# Создаем подключение к базе данных
engine = create_engine("sqlite:///War_DATA.db")

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()



# Работа с БД
Base = declarative_base()


# # Определяем класс модели для таблиц


class Army(Base):
    __tablename__ = "Армия"

    id = Column("ID", Integer, primary_key=True)
    lvl = Column("Класс", Integer)
    type = Column("Тип", Text)
    power = Column("Сила", Text)
    xp = Column("Здоровье", Text)
    speed = Column("Скорость", Text)
    money = Column("Стоимость_за_10к", Integer)
    


# class Stavki_Rulet(Base):
#     __tablename__ = "Ставки_на_рулетку"

#     id = Column("ID", Integer, primary_key=True)
#     table_number = Column("Номер_стола", Integer)
#     name = Column("Игрок", Text)
#     kingdom = Column("Королевство", Text)
#     stavka = Column("Ставка", Integer)
#     combination = Column("Комбинация", Text)
#     sector = Column("Шарик_закатился_на_сектор", Text)
#     stavka_win = Column("Ставка_Игрока_Зашла", Text)
#     balance = Column("Текущий_Баланс_Рулетки", Integer)

# class Rulet(Base):
#     __tablename__ = "Рулетка"

#     id = Column("ID", Integer, primary_key=True)
#     table_number = Column("Номер_стола", Integer)
#     start_balance = Column("Стартовый_Баланс", Integer)
#     now_balance = Column("Текущий_Баланс", Integer)
#     comment = Column("Комментарий", Text)
#     results_of_day = Column("Итоги_дня", Integer)

# class Avtomat(Base):
#     __tablename__ = "Игровые_Автоматы"

#     id = Column("ID", Integer, primary_key=True)
#     avtomat_number = Column("Номер_автомата", Integer)
#     start_balance = Column("Стартовый_Баланс", Integer)
#     # start_balance = Column("Стартовый_Баланс", Integer, default=0)
#     now_balance = Column("Текущий_Баланс", Integer)
#     comment = Column("Комментарий", Text)
#     results_of_day = Column("Итоги_дня", Integer)


# class BANK(Base):
#     __tablename__ = "Банк"

#     id = Column("ID", Integer, primary_key=True)
#     day = Column("День", Integer)
#     avtomat_profit = Column("Доход_с_автоматов", Integer)
#     ruletka_profit = Column("Доход_с_рулеток", Integer)
#     results_of_day = Column("Итоги_дня", Integer)
#     storage = Column("Хранилище", Integer)


# class Debtors(Base):
#     __tablename__ = "Должники"

#     id = Column("ID", Integer, primary_key=True)
#     day = Column("День", Integer)
#     id_player = Column("ID_Игрока", Integer)
#     name = Column("Имя", Text)
#     kingdom = Column("Королевство", Text)
#     duty = Column("Долг", Integer)
#     comment = Column("Комментарий", Text)


# class Winners(Base):
#     __tablename__ = "Победители"

#     id = Column("ID", Integer, primary_key=True)
#     day = Column("День", Integer)
#     id_player = Column("ID_Игрока", Integer)
#     name = Column("Имя", Text)
#     kingdom = Column("Королевство", Text)
#     jackpot = Column("Джекпот", Integer)
#     comment = Column("Комментарий", Text)


# Создаем таблицу
# Base.metadata.create_all(engine)


# table_name = "Армия"
# Base.metadata.tables[table_name].drop(engine)
# table_name = "Рулетка"
# Base.metadata.tables[table_name].drop(engine)
# table_name = "Игровые_Автоматы"
# Base.metadata.tables[table_name].drop(engine)
# table_name = "Банк"
# Base.metadata.tables[table_name].drop(engine)
# table_name = "Должники"
# Base.metadata.tables[table_name].drop(engine)
# table_name = "Победители"
# Base.metadata.tables[table_name].drop(engine)
# table_name = "Ставки_на_рулетку"
# Base.metadata.tables[table_name].drop(engine)






# ------------------------------------------------
# Удалить все записи
session.query(Army).delete()
# session.query(Igroki).delete()
# session.query(BANK).delete()
# session.query(Debtors).delete()

# Добавили записи 
# try:
#     army_update = Army(id=1, lvl=1, type="Пехота", power = "(1 - 4)", xp=7, speed="(1 - 6)", money = 100)
#     session.add(army_update)
#     army_update = Army(id=2, lvl=1, type="Кавалерия", power = "(1 - 5)", xp=5, speed="(1 - 6)(1 - 6)", money = 100)
#     session.add(army_update)
#     army_update = Army(id=3, lvl=1, type="Стрелки", power = "(1 - 4)", xp=5, speed="(1 - 6)", money = 300)
#     session.add(army_update)
#     army_update = Army(id=4, lvl=1, type="Осадные оружия", power = "(0 - 2) / (1 - 6)*5", xp=20, speed="(1 - 6)", money = 1000)
#     session.add(army_update)

#     army_update = Army(id=5, lvl=2, type="Пехота", power = "(3 - 8)", xp=15, speed="(1 - 6)", money = 200)
#     session.add(army_update)
#     army_update = Army(id=6, lvl=2, type="Кавалерия", power = "(4 - 10)", xp=8, speed="(1 - 6)(1 - 6)", money = 1000)
#     session.add(army_update)
#     army_update = Army(id=7, lvl=2, type="Стрелки", power = "(3 - 7)", xp=6, speed="(1 - 6)", money = 300)
#     session.add(army_update)
#     army_update = Army(id=8, lvl=2, type="Осадные оружия", power = "(1 - 4) / (1 - 6)*10", xp=50, speed="(1 - 4)", money = 5000)
#     session.add(army_update)

#     army_update = Army(id=9, lvl=3, type="Пехота", power = "(10 - 25)", xp=70, speed="(1 - 4)", money = 2000)
#     session.add(army_update)
#     army_update = Army(id=10, lvl=3, type="Кавалерия", power = "(15 - 35)", xp=30, speed="(1 - 4)(1 - 4)", money = 5000)
#     session.add(army_update)
#     army_update = Army(id=11, lvl=3, type="Стрелки", power = "(15 - 25)", xp=10, speed="(1 - 4)", money = 3000)
#     session.add(army_update)
#     army_update = Army(id=12, lvl=3, type="Осадные оружия", power = "(1 - 6) / (1 - 4)*50", xp=1000, speed="2", money = 10000)
#     session.add(army_update)


#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибкААААААААААА: {e}")

# Добавили записи Должникам
# try:
#     debtor_update = Debtors(id=0, day=0, id_player=0, name="Test 1", kingdom="Neverland", duty = 1000, comment = "Не вернет")
#     session.add(debtor_update)
#     debtor_update = Debtors(id=1, day=0, id_player=1, name="Test 2", kingdom="Neverland", duty = 1000, comment = "Не вернет")
#     session.add(debtor_update)
#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")

# try:
#     for i in range(2, 11):
#         avtomat_update = Avtomat(id=i, avtomat_number=i, start_balance=0, now_balance = 0, comment = "", results_of_day = 0)
#         session.add(avtomat_update)

#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")


# try:
#     for i in range(1, 11):
#         rulet_update = Rulet(id=i, table_number=i, start_balance=10000, now_balance = 0, comment = "", results_of_day = 0)
#         session.add(rulet_update)

#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")

# Добавили записи Банку
# try:
#     bank_update_start = BANK(
#         id=0,
#         day=0,
#         avtomat_profit=0,
#         ruletka_profit=0,
#         results_of_day=0,
#         storage=10000,
#     )
#     session.add(bank_update_start)
#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")

# Список для игроков
# players_list = []
# names = ["Артур", "Ланселот", "Гвиневра", "Мерлин", "Изольда", "Тристан", "Персиваль", "Морган", "Галахад", "Гавейн", "Элоуэн", "Элиан", "Игрейна", "Герайнт", "Гавейн", "Моргана", "Гахерис", "Нимуэ", "Агравейн", "Моргауза", "Тристан", "Игрена", "Бедивер", "Элейна", "Леонтес", "Вивьен", "Элен", "Утер", "Этельстан", "Изолт", "Игрейна", "Лоэнгрин", "Раньель", "Галахальт", "Диндран", "Борс", "Моргауз", "Гвендолин", "Мордред", "Гвейн", "Саграмор", "Карадок", "Селидант", "Динас", "Гахариет", "Гавен", "Липпи", "Абелард", "Бекет", "Колман", "Изабо", "Элоиза", "Игрейн", "Женевьева", "Говен", "Изолт", "Рианнон", "Диндрана", "Серидвен", "Элен", "Раньель", "Вивиан", "Бланшфлер", "Эсклармонда", "Айбрик", "Мэлори", "Изольда", "Изоуд", "Борс", "Бедвир", "Кай", "Кулхч", "Эктор", "Горлойс", "Гвальчмей", "Гвин", "Иорверт", "Уриен", "Ивен", "Персиваль", "Пеллеас", "Паламед", "Леодегран", "Ллачеу", "Карадок", "Галахад", "Кей", "Увайн", "Ронабви", "Бреунор", "Мирддин", "Рис", "Бледдри", "Кол", "Эдейрн", "Элиан", "Эмир", "Морфран", "Падарн", "Тегир"
#         "Янита", "Йоханна", "Таисия", "Жаклин", "Диана", "Федосья", "Фаина", "Цвета", "Зоя", "Анастасия", "Галина", "Жаклин", "Елизавета", "Шарлота", "Злата", "Лидия", "Чеслава", "Цилла", "Федосья", "Гелла", "Диана", "Фаина", "Лидия", "Цилла", "Алёна", "Зоя", "Янита", "Зоя", "Беатриса", "Шушана", "Оксана", "София", "Прасковья", "Изольда", "Розалина", "Беатриса", "Яна", "Устинья", "Йосифа", "Цвета", "Евгения", "Жаклин", "София", "Злата", "Христина", "Янита", "Янита", "Антонина", "Майя", "Таисия", "Ульяна", "Ольга", "Ульяна", "Яна", "Беатриса", "Ольга", "Яна", "Юна", "София", "Злата", "Ульяна", "Эльвира", "Марина", "Оксана", "Диана", "Регина", "Цилла", "Шушана", "Алла", "Злата", "Янита", "Гертруда", "Зинаида", "Злата", "Чечилия", "Зинаида", "Алёна", "Шушана", "Надежда", "Злата", "Йана", "Злата", "Эллада", "Лидия", "Варвара", "Таисия", "Федосья", "Элина", "Регина", "Майя", "Эльвира", "Йоланта", "Регина", "Зоя", "Цара", "Надежда", "Оксана", "Злата", "Евгения", "Борислава", "Гюзель", "Наталья", "Ждан", "Семён", "Платон", "Олег", "Прохор", 
#         "Роман", "Устин", "Никодим", "Руслан", "Ярослав", "Родион", "Роман", "Илья", "Эдуард", "Степан", "Фёдор", "Юрий", "Фёдор", "Роберт", "Марат", "Ярослав", "Шерлок", "Пётр", "Сава", "Иосиф", "Никодим", "Йоган", "Марат", "Иосиф", "Бронислав", "Тит", "Борис", "Жерар", "Устин", "Ираклий", "Йоханес", "Борис", "Ждан", "Юлий", "Бронислав", "Устин", "Закир", "Всеволод", "Роберт", "Родион", "Цефас", "Трофим", "Роман", "Богдан", "Евсей", "Тимур", "Альберт", "Трофим", "Фёдор", "Эрик", "Шарль", "Огюст", "Ждан", "Донат", "Семён", "Цефас", "Роман", "Ярослав", "Борис", "Гордей", "Эрик", "Емельян", "Йосып", "Гордей", "Емельян", "Герасим", "Кузьма", "Закир", "Кузьма", "Борис", "Леопольд", "Орест", "Ефим", "Шерлок", "Ждан", "Бронислав", "Заур", "Ярослав", "Феликс", "Игнатий", "Савва", "Семён", "Тимофей", "Роберт", "Марат", "Прохор", "Кузьма", "Огюст", "Жигер", "Устин", "Шамиль", "Вячеслав", "Сава", "Цицерон", "Жерар", "Шамиль", "Ян", "Эрик", "Богдан", "Феликс", "Сергей", "Йоханес", "Чеслав", "Харитон", "Родион", "Тит", "Тимофей", "Цицерон", "Шерлок", 
#         "Устин", "Жерар", "Жигер", "Орест", "Закир", "Харитон", "Фёдор", "Ефим", "Йоханес", "Тит", "Огюст", "Лев", "Мирослав", "Радислав", "Борис", "Никодим", "Чеслав", "Фёдор", "Тимур", "Йосып", "Жерар", "Платон", "Лукьян", "Шарль", "Семён", "Илларион", "Лев", "Богдан", "Харитон", "Назар", "Лев", "Харитон", "Леон", "Тимофей", "Шерлок", "Тарас", "Пётр", "Ярослав", "Эдуард", "Цефас", "Йоханес", "Устин", "Фёдор", "Болеслав", "Прохор", "Вадим", "Стефан", "Харитон", "Эрик", "Вадим", "Прохор", "Огюст", "Еремей", "Тит", "Закир", "Шерлок", "Тимофей", "Вадим", "Евдоким", "Ярослав", "Бронислав", "Илья", "Марат", "Марат", "Вадим", "Устин", "Юлий", "Игнат", "Шерлок", "Борис", "Ярослав", "Устин", "Бронислав", "Тимур", "Феликс", "Цефас", "Валерий", "Глеб", "Мирослав", "Жерар", "Жерар", "Кузьма", "Фёдор", "Марат", "Людовик", "Руслан", "Филипп", "Лукьян", "Йоханес", "Фёдор", "Прохор", "Ярослав", "Харитон", "Михаил", "Лев", "Андрей", "Осип", "Ярослав", "Шерлок", "Эдуард", "Юрий", "Шарль", "Тит", "Ярослав", "Ираклий", "Чарльз", "Устин", "Ян", "Харитон", "Йомер", 
#         "Артём", "Огюст", "Тит", "Матвей", "Семён", "Мирослав", "Эрик", "Йоханес", "Геннадий", "Оскар", "Добрыня", "Устин", "Феликс", "Эрик", "Станислав", "Данила", "Зенон", "Йоган", "Еремей", "Трофим", "Руслан", "Йоган", "Данила", "Лукиллиан", "Фёдор", "Геннадий", "Фёдор", "Камиль", "Чеслав", "Устин", "Станислав", "Добрыня", "Фёдор", "Борис", "Йоханес", "Цицерон", "Людовик", "Цефас", "Герман", "Валериан", "Гарри", "Жигер", "Сергей", "Максим", "Конрад", "Йозеф", "Святослав", "Никодим", "Добрыня", "Оскар" ]
# kingdoms = ["Камелот", "Редания", "Цинтра", "Венгерберг", "Нильфгаард"]

# try:
#     # Создаём 100 игроков
#     for i in range(1, 401):

#     # while not Exception:

#         generate_name = random.choice(names)
#         names.remove(generate_name)
#         generate_balance = random.randint(1, 100) * (random.randint(1, 10) * 100) * 10
#         generate_kingdom = random.choice(kingdoms)

#         player = Igroki(id = i, name=generate_name, kingdom=generate_kingdom, balance=generate_balance, azart=70, comment="")
#         players_list.append(player)
#         # print(generate_name)

#     session.add_all(players_list)
#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")



# ------------------------------------------------



# Igroki_FULL_list = session.query(Igroki).all()
# Igroki_list = [player for player in Igroki_FULL_list if player.balance > 100]


# # Берем из Хранилища стартовый баланс для каждого автомата и рулетки
# Avtomat_1_BANK = 0
# Avtomat_now_balance = 0
# Avtomat_1 = (
#     session.query(Avtomat).filter_by(avtomat_number=1).first()
# )  # в этой переменной тперь значение из БД
# try:
#     Avtomat_now_balance = Avtomat_1.start_balance  # = 10 000
#     # Сразу же вычитаем из Хранилища эту сумму
#     max_value = session.query(func.max(BANK.storage)).scalar()
#     start_mony = session.query(BANK).filter_by(storage=max_value).first()
#     start_mony.storage -= Avtomat_1.start_balance

# except Exception as e:
#     print(f"Произошла ошибка: {e}")
# # session.commit()




# # Берем из Хранилища стартовый баланс для рулетки
# Ruletka_1_BANK = 0
# Ruletka_now_balance = 0
# Ruletka_1 = (
#     session.query(Rulet).filter_by(table_number=1).first()
# )
# try:
#     Ruletka_now_balance = Ruletka_1.start_balance  # = 10 000
#     # Сразу же вычитаем из Хранилища эту сумму
#     max_value = session.query(func.max(BANK.storage)).scalar()
#     start_mony = session.query(BANK).filter_by(storage=max_value).first()
#     start_mony.storage -= Ruletka_1.start_balance

# except Exception as e:
#     print(f"Произошла ошибка: {e}")





# # Ищем последний день
# n_day = 0
# try:
#     max_day_subquery = session.query(func.max(BANK.day)).as_scalar()
#     bank_buffer = session.query(BANK).filter(BANK.day == max_day_subquery).first()
#     n_day = bank_buffer.day + 1
#     print(f"\n\nБанк день: {n_day}, хранилище: {bank_buffer.storage}\n\n")
# except Exception as e:
#     print(f"Произошла ошибка(bank_buffer): {e}")


# n_winner_id = 0
# try:
#     max_value = session.query(func.max(Winners.id)).scalar()
#     winners_buffer = session.query(Winners).filter_by(id=max_value).first()
#     # winners_buffer = session.query(Winners).filter(Winners.id == func.max(Winners.id)).first()
#     n_winner_id = winners_buffer.id + 1
#     print(f"\n\nПобедители(поиск id): ID: {n_winner_id}\n\n")
# except Exception as e:
#     print(f"Победители(поиск id): Произошла ошибка: {e}")







# ----------------------------------------------------------------------------------------------------------





# def load_players_from_db():
#     players = session.query(Igroki).filter(Igroki.balance > 100).all()
#     return players

# Igroki_list = load_players_from_db()

# Igroki_FULL_list = session.query(Igroki).all()
# Igroki_list = [player for player in Igroki_FULL_list if player.balance > 100]

# def Serch_active_players():
#     try:
#         active_player = random.choice(Igroki_list)
#         active_player.azart = 70
#         return active_player
#     except Exception as e:
#         print(f"Произошла ошибка(поиск играков): {e}")
#         return None
    


# Сохраняем изменения в базе данных
session.commit()

# Закрываем соединение с базой данных
session.close()