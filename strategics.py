import time
import datetime
import io

from random import randint, choice

from Bot import Bot
from ImageTriggers import ImageTriggers

from loguru import logger

import telebot


class Telebot:
    def __init__(self, token, tg_user):
        self.bot = telebot.TeleBot(token)
        self.tg_user = tg_user

    def send_message(self, text):
        self.bot.send_message(self.tg_user, text)

    def send_image(self, img):
        self.bot.send_photo(self.tg_user, img)

    def send_debag(self):
        pass

    def restart_bot(self):
        self.bot.send_message(self.tg_user, 'The bot has been restarted.')


class Strategics:
    def __init__(self, batlle_mode, open_chest, requested_card, port, changed_account, number_account, total_accounts, id_card, play_clan_war, connection_to_parent, change_deck, number_fights_deck_change, send_emotion, reboot_index, android, forever_elexir, number_of_finish, time_break, open_PR, debug, token, tg_user, activ_tg_bot, use_chest_key):
        logger.debug( f'{(batlle_mode, open_chest, requested_card, port, changed_account, number_account, total_accounts, id_card, play_clan_war, connection_to_parent, change_deck, number_fights_deck_change, send_emotion, reboot_index, android, forever_elexir, number_of_finish, time_break, open_PR, debug, token, tg_user, activ_tg_bot, use_chest_key)}')
        self.port = port
        self.bot = Bot(port=port, android=android)
        self.triggers = ImageTriggers(open_chest, requested_card, open_PR, debug)
        self.index = 0
        self.index124 = 0
        self.index280 = 0
        self.cycleStart = False
        self.batlle_mode = batlle_mode
        self.number_account = number_account
        self.changed_account = changed_account
        self.total_accounts = total_accounts
        self.connection_to_parent = connection_to_parent
        self.request_card = requested_card
        self.id_card = id_card
        self.play_clan_war = play_clan_war
        self.CW = play_clan_war
        self.change_deck = change_deck
        self.number_fights_deck_change = number_fights_deck_change
        self.index_change_deck = 0
        self._number_fights_deck_change = self.number_fights_deck_change
        self.send_emotion = send_emotion
        self.reboot_index = reboot_index
        self.reboot_index_2 = reboot_index
        self._reboot_index = 0
        self.forever_elexir = forever_elexir
        self._forever_elexir = self.forever_elexir
        self.index_forever_elexir = 0
        self.number_of_finish = number_of_finish
        self.time_break = time_break
        self.sleep = True
        self.debug = debug
        self.t = time.time()
        self.use_chest_key = use_chest_key
        #self.tlgbot = Telebot(token, tg_user)


    def main(self):

        if self.bot.ADB.cheakInstallCR() == False:
            self.cycleStart = False

        if self.bot.ADB.cheakRunCR() == False:
            self.bot.openCR()

        sl = 2 if self.send_emotion else 0

        slowdown_in_menu = True

        index_batlle = 0
        t = time.time()
        self.t = time.time()
        #self.tlgbot.send_message('Запущен бот')
        while self.cycleStart:
            #self.tlgbot.send_message('проход по циклу бот')
            self.t = time.time()
            try:
                image = self.bot.getScreen()
            except:
                time.sleep(1)
                continue
            triggers = self.triggers.getTrigger(image)
            trigger = triggers[0]
            logger.debug(str(triggers) + ' ' + str(time.time() - t))
            #self.connection_to_parent._textBrowser_3 = f'{triggers}\n' + self.connection_to_parent._textBrowser_3

            if self.index == 50:
                self.bot.reboot()
                self.index = 0
                logger.debug(str(triggers))
                continue

            if self.index % 5 == 4:
                self.bot.choose_reward(randint(0, 1))
                self.bot.returnHome()
                logger.debug(str(triggers))

            if self.index124 >= 25:
                self.bot.goToShop()
                self.bot.returnHome()
                self.bot.reboot()
                self.index124 = 0
                logger.debug(str(triggers))
                continue

            if trigger == 124:
                self.index124 += 1
                logger.debug(str(triggers))
                continue
            self.index124 = 0

            if not (trigger == 0):
                logger.debug(str(triggers))
                self.index = 0

            if trigger == 500:
                logger.debug(str(triggers))
                self.bot.openCR()

            if trigger == 501:
                self.connection_to_parent._textBrowser_3 = 'INCORRECT SCREEN RESOLUTION IS SET!'
                self.stopFarm()
                logger.debug(str(triggers))

            if trigger == 0:
                self.index += 1
                logger.debug('Не найден триггер')
                self.connection_to_parent._textBrowser_3 = 'Trigger not found\n' + self.connection_to_parent._textBrowser_3
                time.sleep(3)
                logger.debug(str(triggers))
                continue
            else:
                logger.debug(str(triggers))
                self.index = 0


            if trigger == 100:
                if self.batlle_mode == 'Drop Trophy':
                    self.connection_to_parent._textBrowser_3 = f'Drop Trophy\n' + self.connection_to_parent._textBrowser_3
                    continue

                self.connection_to_parent._textBrowser_3 = f'In battle Card: {triggers[2]} Elixir: {triggers[1]}  \n' + self.connection_to_parent._textBrowser_3
                logger.debug(str(triggers))

                if self._forever_elexir:
                    self.bot.random_placing_card()
                    continue

                if triggers[1] >= 9:
                    self.index_forever_elexir += 1
                    if self.index_forever_elexir >= 3:
                        self._forever_elexir = True

                if triggers[1] <= 4:
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                        time.sleep(2)
                    continue

                if 'Goblin_Barrel' in triggers[2]:
                    if triggers[1] >= 3:
                        self.bot.selectCard(triggers[2].index('Goblin_Barrel'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                        continue
                    else:
                        continue

                if 'Goblin_Drill' in triggers[2]:
                    if triggers[1] >= 3:
                        self.bot.selectCard(triggers[2].index('Goblin_Drill'))
                        self.bot.placingCard1X1(choice((440, 103)), 220)
                        continue
                    else:
                        continue

                if 'Balloon' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Balloon'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                        continue
                    else:
                        continue

                if 'Graveyard' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Graveyard'))
                        self.bot.placingCard1X1(choice((440, 103)), 220)
                        continue
                    else:
                        continue

                if 'Miner' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Miner'))
                        self.bot.placingCard1X1(choice((440, 103)), 220)
                        continue
                    else:
                        continue

                if 'Mortar' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Mortar'))
                        self.bot.placingCard1X1(choice((125, 416)), 470)
                        continue
                    else:
                        continue
                if 'X-Bow' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('X-Bow'))
                        self.bot.placingCard1X1(choice((125, 416)), 470)
                        continue
                    else:
                        continue


                if 'Skeleton_Barrel' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Skeleton_Barrel'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                        continue
                    else:
                        continue

                if 'Three_Musketeers' in triggers[2]:
                    if triggers[1] >= 9:
                        self.bot.selectCard(triggers[2].index('Three_Musketeers'))
                        self.bot.placingCard1X1(260, 700)
                        continue
                    else:
                        continue

                if 'Zappies' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Zappies'))
                        self.bot.placingCard1X1(260, 700)
                        continue
                    else:
                        continue

                if 'Ram_Rider' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Ram_Rider'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                        continue
                    else:
                        continue

                if 'Elixir_Collector' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Elixir_Collector'))
                        self.bot.placingCard1X1(choice((71, 176, 211, 280, 359, 481)), 673)
                        continue
                    else:
                        continue

                if 'Prince' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Prince'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                        continue
                    else:
                        continue

                if 'Dark_Prince' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Dark_Prince'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                        continue
                    else:
                        continue

                if 'Royal_Hogs' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Royal_Hogs'))
                        self.bot.placingCard1X1(choice((410, 268, 105)), 202)
                        continue
                    else:
                        continue

                if 'Golem' in triggers[2]:
                    if triggers[1] >= 8:
                        self.bot.selectCard(triggers[2].index('Golem'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(6)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Golem'))
                        self.bot.placingCard1X1(275, 700)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(4)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(475, 550)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(4)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(390, 450)
                    continue

                if 'Giant' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Giant'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(4+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Giant'))
                        self.bot.placingCard1X1(275, 700)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(3+sl)
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(475, 550)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(3+sl)
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(390, 450)
                    continue

                if 'Goblin_Giant' in triggers[2]:
                    if triggers[1] >= 7:
                        self.bot.selectCard(triggers[2].index('Goblin_Giant'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(5+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Goblin_Giant'))
                        self.bot.placingCard1X1(275, 700)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(3 + sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(475, 550)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(3+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(390, 450)
                    continue

                if 'Lava_Hound' in triggers[2]:
                    if triggers[1] >= 8:
                        self.bot.selectCard(triggers[2].index('Lava_Hound'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(5+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Lava_Hound'))
                        self.bot.placingCard1X1(275, 700)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(3+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(475, 550)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(4+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(390, 450)
                    continue

                if 'Electro_Giant' in triggers[2]:
                    if triggers[1] >= 8:
                        self.bot.selectCard(triggers[2].index('Electro_Giant'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(5+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Electro_Giant'))
                        self.bot.placingCard1X1(275, 700)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(3+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(475, 550)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(4+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(390, 450)
                    continue

                if 'Elixir_Golem' in triggers[2]:
                    if triggers[1] >= 7:
                        self.bot.selectCard(triggers[2].index('Elixir_Golem'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(2+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Battle_Healer' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Battle_Healer'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Elite_Barbarians' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Elite_Barbarians'))
                        self.bot.placingCard1X1(330, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Electro_Dragon' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Electro_Dragon'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Elixir_Golem'))
                        self.bot.placingCard1X1(275, 700)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(3+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(475, 550)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    time.sleep(4+sl)
                    if self.send_emotion:
                        self.bot.send_emotion(randint(0, 3))
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(390, 450)
                    continue

                if 'Goblin_Gang' in triggers[2]:
                    if triggers[1] >= 3:
                        self.bot.selectCard(triggers[2].index('Goblin_Gang'))
                        self.bot.placingCard1X1(260, 700)
                        continue
                    else:
                        continue

                if 'Princess' in triggers[2]:
                    if triggers[1] >= 3:
                        self.bot.selectCard(triggers[2].index('Princess'))
                        self.bot.placingCard1X1(260, 700)
                        continue
                    else:
                        continue

                if 'Hog_Rider' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Hog_Rider'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                        continue
                    else:
                        continue

                if 'Cannon' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Cannon'))
                        self.bot.placingCard1X1(250, 515)
                        continue
                    else:
                        continue

                if 'Goblin_Hut' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Goblin_Hut'))
                        self.bot.placingCard1X1(250, 515)
                        continue
                    else:
                        continue

                if 'Goblin_Cage' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Goblin_Cage'))
                        self.bot.placingCard1X1(250, 515)
                        continue
                    else:
                        continue

                if 'Barbarian_Hut' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Barbarian_Hut'))
                        self.bot.placingCard1X1(250, 515)
                        continue
                    else:
                        continue

                if 'Furnace' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Furnace'))
                        self.bot.placingCard1X1(250, 515)
                        continue
                    else:
                        continue

                if 'Bomb_Tower' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Bomb_Tower'))
                        self.bot.placingCard1X1(250, 515)
                        continue
                    else:
                        continue

                if 'Tesla' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Tesla'))
                        self.bot.placingCard1X1(250, 515)
                        continue
                    else:
                        continue
                    #######################

                if 'Tornado' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Tornado'))
                        self.bot.placingCard1X1(randint(110, 420), 300)
                        continue
                    else:
                        continue

                if 'Royal_Delivery' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Royal_Delivery'))
                        self.bot.placingCard1X1(choice((100, 130, 160, 380, 410, 440)), randint(430, 500))
                        continue
                    else:
                        continue

                if 'Barbarian_Barrel' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Barbarian_Barrel'))
                        self.bot.placingCard1X1(choice((100, 130, 160, 380, 410, 440)), 430)
                        continue
                    else:
                        continue

                if 'The_Log' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('The_Log'))
                        self.bot.placingCard1X1(choice((100, 130, 160, 380, 410, 440)), 430)
                        continue
                    else:
                        continue

                if 'Earthquake' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Earthquake'))
                        self.bot.placingCard1X1(choice((75, 105, 130, 160, 180, 330, 360, 390, 400)), 250)
                        continue
                    else:
                        continue

                if 'Lightnimg' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Lightnimg'))
                        self.bot.placingCard1X1(choice((75, 105, 130, 160, 180, 330, 360, 390, 400)), 250)
                        continue
                    else:
                        continue

                if 'Poison' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Poison'))
                        self.bot.placingCard1X1(choice((75, 105, 130, 160, 180, 360, 390, 400)), 250)
                        continue
                    else:
                        continue

                if 'Arrows' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Arrows'))
                        self.bot.placingCard1X1(choice((75, 105, 130, 160, 180, 330, 360, 390, 400)), 250)
                        continue
                    else:
                        continue

                if 'Fireball' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Fireball'))
                        self.bot.placingCard1X1(choice((75, 100, 128, 150, 175, 350, 385, 410, 440)), 270)
                        continue
                    else:
                        continue

                if 'Giant_Snowball' in triggers[2]:
                    if triggers[1] >= 3:
                        self.bot.selectCard(triggers[2].index('Giant_Snowball'))
                        self.bot.placingCard1X1(choice((75, 100, 128, 150, 175, 350, 385, 410, 440)), 270)
                        continue
                    else:
                        continue

                if 'Freeze' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Freeze'))
                        self.bot.placingCard1X1(choice((75, 100, 128, 150, 175, 350, 385, 410, 440)), 270)
                        continue
                    else:
                        continue

                if 'Rocket' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Rocket'))
                        self.bot.placingCard1X1(choice((75, 105, 130, 160, 180, 330, 360, 390, 400)), 250)
                        continue
                    else:
                        continue

                if 'Zap' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Zap'))
                        self.bot.placingCard1X1(choice((75, 100, 128, 150, 175, 350, 385, 410, 440)), 270)
                        continue
                    else:
                        continue

                if 'Rage' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Rage'))
                        self.bot.placingCard1X1(choice((105, 130, 160, 180, 330, 360, 390)), 520)
                        continue
                    else:
                        continue

                if 'МУСОР' in triggers[2] and False:
                    l = triggers[2].index('МУСОР')
                    if l == 3:
                        self.bot.selectCard(randint(0, 2))
                        self.bot.placingCard1X1(randint(275, 475), randint(426, 700))
                    else:
                        self.bot.selectCard(4)
                        self.bot.placingCard1X1(randint(275, 475), randint(426, 700))
                else:
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(randint(275, 475), randint(426, 700))
                t = time.time()
                continue


            elif trigger == 121:
                self.bot.send_emotion(randint(0, 3))
                logger.debug(str(triggers))
                index_batlle += 1
                self.connection_to_parent.totall_batlles += 1
                self.index_change_deck += 1
                self.connection_to_parent.got_crowns += triggers[1]
                self.connection_to_parent._textBrowser_2 = f'The result of the battle: {datetime.datetime.now():%Y-%m-%d %H:%M:%S} crows:{triggers[1]}\n' + self.connection_to_parent._textBrowser_2
                self.connection_to_parent._textBrowser_3 = 'End of the fight\n'
                self._reboot_index += 1
                self._forever_elexir = self.forever_elexir
                self.index_forever_elexir = 0

                if self.time_break > 0 and self.number_of_finish > 0:
                    if index_batlle >= self.number_of_finish:
                        logger.debug(str(triggers))
                        self.bot.closeCR()
                        self.sleep = False
                        time.sleep(self.time_break * 60 + 1)
                        self.sleep = True
                        index_batlle = 0
                        self.bot.openCR()

                if self._reboot_index >= self.reboot_index_2 and False:
                    logger.debug(str(triggers))
                    self.bot.reboot_android()
                    self._reboot_index = 0
                    self.reboot_index_2 = self.reboot_index + randint(1, 6)
                    continue

                self.bot.exitBatle1X1()
                logger.debug(str(triggers))



            elif trigger == 122:
                self.bot.send_emotion(randint(0, 3))
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'End of the fight\n'
                index_batlle += 1
                self.connection_to_parent.totall_batlles += 1
                self.connection_to_parent.got_crowns += triggers[1]
                self.index_change_deck += 1
                self.connection_to_parent._textBrowser_2 = f'The result of the battle: {datetime.datetime.now():%Y-%m-%d %H:%M:%S} crows:{triggers[1]}\n' + self.connection_to_parent._textBrowser_2
                self.connection_to_parent._textBrowser_3 = f'{triggers}\n'
                self._reboot_index += 1
                if self.time_break > 0 and self.number_of_finish > 0:
                    if index_batlle >= self.number_of_finish:
                        logger.debug(str(triggers))
                        self.bot.closeCR()
                        self.sleep = False
                        time.sleep(self.time_break * 60 + 1)
                        self.sleep = True
                        index_batlle = 0
                        self.bot.openCR()
                time.sleep(3)
                self._forever_elexir = self.forever_elexir
                self.index_forever_elexir = 0

                if self._reboot_index >= self.reboot_index_2 and False:
                    logger.debug(str(triggers))
                    self.bot.reboot_android()
                    self._reboot_index = 0
                    self.reboot_index_2 = self.reboot_index + randint(1, 6)
                    continue

                self.bot.exitBatle2X2()


            elif trigger == 124:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Loading a fight\n' + self.connection_to_parent._textBrowser_3
                self.bot.send_emotion(randint(0, 3))
                time.sleep(2)

            elif trigger == 125:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Send emotion\n' + self.connection_to_parent._textBrowser_3
                self.bot.send_emotion(randint(0, 3))

            elif trigger == 200:
                #self.tlgbot.send_image(io.BytesIO(image))
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'The bot is in the menu\n' + self.connection_to_parent._textBrowser_3
                if self.CW:
                    logger.debug(str(triggers))
                    self.connection_to_parent._textBrowser_3 = 'Checking for sending to battle on square\n' + self.connection_to_parent._textBrowser_3
                    self.bot.goToClanChat()
                    time.sleep(5)
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        continue
                    triggers = self.triggers.getTrigger(image)
                    trigger = triggers[0]

                    if trigger == 216:
                        logger.debug(str(triggers))
                        self.connection_to_parent._textBrowser_3 = 'You are not in a clan\n' + self.connection_to_parent._textBrowser_3
                        self.CW = False
                        self.bot.returnHome()

                    if trigger == 239:
                        logger.debug(str(triggers))
                        self.connection_to_parent._textBrowser_3 = 'Get reward clan war\n' + self.connection_to_parent._textBrowser_3
                        self.bot.get_reward_clan_war()
                        continue

                    if trigger == 218:
                        logger.debug(str(triggers))
                        self.connection_to_parent._textBrowser_3 = 'Close statistics clan war\n' + self.connection_to_parent._textBrowser_3
                        self.bot.close_statistics_clan_war()
                        continue

                    if trigger == 260:
                        logger.debug(str(triggers))
                        self.connection_to_parent._textBrowser_3 = 'Scroll to recognize\n' + self.connection_to_parent._textBrowser_3
                        self.bot.go_batlle_clan_war(0)
                        continue

                    if trigger == 261:
                        logger.debug(str(triggers))
                        self.connection_to_parent._textBrowser_3 = 'Scroll to recognize\n' + self.connection_to_parent._textBrowser_3
                        self.bot.go_batlle_clan_war(1)
                        continue

                    if trigger == 215 and True in triggers[1]:
                        index = 0
                        logger.debug(str(triggers))
                        while True:
                            logger.debug(str(triggers))
                            self.connection_to_parent._textBrowser_3 = 'Scroll to send go batlle\n' + self.connection_to_parent._textBrowser_3
                            index += 1
                            self.bot.swipe_clan_war()
                            time.sleep(2)
                            try:
                                image = self.bot.getScreen()
                            except:
                                time.sleep(1)
                                continue
                            triggers = self.triggers.getTrigger(image)
                            trigger = triggers[0]
                            if trigger == 260:
                                logger.debug(str(triggers))
                                self.connection_to_parent._textBrowser_3 = 'Go batlle\n' + self.connection_to_parent._textBrowser_3
                                self.bot.go_batlle_clan_war(0)
                                break
                            if trigger == 261 or index >= 7:
                                logger.debug(str(triggers))
                                self.connection_to_parent._textBrowser_3 = 'Go batlle\n' + self.connection_to_parent._textBrowser_3
                                self.bot.go_batlle_clan_war(1)
                                break

                            continue

                    elif trigger == 212:
                        logger.debug(str(triggers))
                        self.connection_to_parent._textBrowser_3 = 'Go batlle\n' + self.connection_to_parent._textBrowser_3
                        self.bot.goToClanChat()
                        time.sleep(1)
                        self.bot.returnHome()
                        continue

                    if trigger == 215 and not (True in triggers[1]):
                        logger.debug(str(triggers))
                        self.connection_to_parent._textBrowser_3 = 'Switching to the clan wars menu\n' + self.connection_to_parent._textBrowser_3
                        self.CW = False
                        self.bot.returnHome()
                        continue
                    
                    self.bot.close_statistics_clan_war()
                    self.bot.get_reward_clan_war()

                    continue


                if slowdown_in_menu:
                    logger.debug(str(triggers))
                    slowdown_in_menu = False
                    time.sleep(3)
                    continue
                slowdown_in_menu = True

                if self._number_fights_deck_change <= self.index_change_deck:
                    logger.debug(str(triggers))
                    self.connection_to_parent._textBrowser_3 = 'Change deck 1/2\n' + self.connection_to_parent._textBrowser_3
                    self.bot.goToDeck()
                    time.sleep(5)
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        self.bot.reboot()
                        continue
                    triggers = self.triggers.getTrigger(image)
                    trigger = triggers[0]

                    if trigger == 209:
                        logger.debug(str(triggers))
                        self.bot.get_reward_masteries()
                        time.sleep(5)
                        try:
                            try:
                                image = self.bot.getScreen()
                            except:
                                time.sleep(1)
                                self.bot.reboot()
                                continue
                        except:
                            time.sleep(1)
                            continue
                        triggers = self.triggers.getTrigger(image)
                        trigger = triggers[0]

                        if trigger == 290:
                            logger.debug(str(triggers))
                            self.bot.close_reward_masteries()
                        elif trigger == 291:
                            logger.debug(str(triggers))
                            self.bot.get_reward_masteries_2(trigger)
                        elif trigger == 292:
                            logger.debug(str(triggers))
                            self.bot.get_reward_masteries_2(trigger)
                        elif trigger == 293:
                            logger.debug(str(triggers))
                            self.bot.get_reward_masteries_2(trigger)
                        elif trigger == 294:
                            logger.debug(str(triggers))
                            self.bot.get_reward_masteries_2(trigger)

                        logger.debug(str(triggers))
                        time.sleep(5)
                        try:
                            image = self.bot.getScreen()
                        except:
                            time.sleep(1)
                            self.bot.reboot()
                            continue
                        triggers = self.triggers.getTrigger(image)
                        trigger = triggers[0]

                        if trigger == 289:
                            logger.debug(str(triggers))
                            self.connection_to_parent._textBrowser_3 = 'Selling an award\n' + self.connection_to_parent._textBrowser_3
                            self.bot.sale_reward()
                        continue

                    if trigger == 202 and self.change_deck:
                        logger.debug(str(triggers))
                        self.connection_to_parent._textBrowser_3 = 'Change deck 2/2\n' + self.connection_to_parent._textBrowser_3
                        self.connection_to_parent.number_deck += 1
                        if self.connection_to_parent.number_deck >= 5:
                            logger.debug(str(triggers))
                            self.connection_to_parent.number_deck = 0
                        self.bot.change_deck(self.connection_to_parent.number_deck)

                    time.sleep(5)

                    logger.debug(str(triggers))
                    self.index_change_deck = 0
                    self._number_fights_deck_change = self.number_fights_deck_change + randint(1, 2)

                    self.bot.returnHome()
                    time.sleep(2)

                if 'Until Chest Slots Full':
                    logger.debug(str(triggers))
                    if self.batlle_mode in('global', 'Drop Trophy'):
                        self.bot.runBattleGlobal()
                        self.connection_to_parent._textBrowser_3 = 'Run Battle Global\n' + self.connection_to_parent._textBrowser_3
                    elif self.batlle_mode == 'disabled':
                        logger.debug(str(triggers))
                        if self.changed_account:
                            logger.debug(str(triggers))
                            self.bot.returnHome()
                            self.increasing_account_number()
                            time.sleep(5)
                            self.bot.changeAccount(self.number_account, self.total_accounts)
                            self.connection_to_parent.number_account = self.number_account
                            self.CW = self.play_clan_war
                        else:
                            logger.debug(str(triggers))
                            self.bot.closeCR()
                            self.sleep = False
                            time.sleep(60 * self.time_break + 1)
                            self.sleep = True
                            self.bot.openCR()
                    else:
                        logger.debug(str(triggers))
                        self.connection_to_parent._textBrowser_3 = f'Run Battle mode {self.batlle_mode} \n' + self.connection_to_parent._textBrowser_3
                        self.bot.runBattleMode(self.batlle_mode)
                    time.sleep(1)

            elif trigger == 202 or trigger == 209:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Return home\n' + self.connection_to_parent._textBrowser_3
                self.bot.returnHome()

            elif trigger == 210:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Checking messages in clan chat\n' + self.connection_to_parent._textBrowser_3
                self.bot.goToClanChat()
                time.sleep(2)
                try:
                    image = self.bot.getScreen()
                except:
                    time.sleep(1)
                    self.bot.reboot()
                    continue
                triggers = self.triggers.getTrigger(image)
                time.sleep(2)
                trigger = triggers[0]
                if trigger != 212:
                    logger.debug(str(triggers))
                    self.connection_to_parent._textBrowser_3 = 'Checking messages in clan chat\n' + self.connection_to_parent._textBrowser_3
                    self.bot.choose_reward(randint(0, 1))
                    self.bot.goToClanChat()
                    time.sleep(2)
                elif trigger == 239:
                    logger.debug(str(triggers))
                    self.connection_to_parent._textBrowser_3 = 'Get reward clan war\n' + self.connection_to_parent._textBrowser_3
                    self.bot.get_reward_clan_war()
                elif trigger == 218:
                    logger.debug(str(triggers))
                    self.connection_to_parent._textBrowser_3 = 'Close statistics clan war\n' + self.connection_to_parent._textBrowser_3
                    self.bot.close_statistics_clan_war()
                    continue
                if trigger == 28:
                    logger.debug(str(triggers))
                    self.connection_to_parent._textBrowser_3 = 'Request Card\n' + self.connection_to_parent._textBrowser_3
                    continue
                    pass
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Request Card\n' + self.connection_to_parent._textBrowser_3
                self.bot.requestCard(self.id_card)
                time.sleep(4)

            elif trigger == 211:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Checking messages in clan chat\n' + self.connection_to_parent._textBrowser_3
                self.bot.goToClanChat()
                time.sleep(2)
                try:
                    image = self.bot.getScreen()
                except:
                    time.sleep(1)
                    self.bot.reboot()
                    continue
                triggers = self.triggers.getTrigger(image)
                trigger = triggers[0]
                time.sleep(2)
                if trigger == 239:
                    logger.debug(str(triggers))
                    self.connection_to_parent._textBrowser_3 = 'Get reward clan war\n' + self.connection_to_parent._textBrowser_3
                    self.bot.get_reward_clan_war()
                    continue
                elif trigger == 218:
                    logger.debug(str(triggers))
                    self.connection_to_parent._textBrowser_3 = 'Close statistics clan war\n' + self.connection_to_parent._textBrowser_3
                    self.bot.close_statistics_clan_war()
                    continue
                if trigger != 212:
                    logger.debug(str(triggers))
                    self.connection_to_parent._textBrowser_3 = 'pass\n' + self.connection_to_parent._textBrowser_3
                    self.bot.choose_reward(randint(0, 1))
                    self.bot.goToClanChat()
                    time.sleep(2)
                self.bot.returnHome()

            elif trigger == 212:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Return home\n' + self.connection_to_parent._textBrowser_3
                self.bot.returnHome()

            elif trigger == 215:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Return home\n' + self.connection_to_parent._textBrowser_3
                self.bot.returnHome()

            elif trigger == 218:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Сlose statistics clan war\n' + self.connection_to_parent._textBrowser_3
                self.bot.close_statistics_clan_war()
                continue

            elif trigger == 219:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Unable to request a card\n' + self.connection_to_parent._textBrowser_3
                self.id_card += 1
                self.bot.reboot()

            elif trigger > 220 and trigger < 225:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Get reward chest\n' + self.connection_to_parent._textBrowser_3
                self.bot.getRewardChest(trigger - 220)

            elif trigger == 225:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Return home\n' + self.connection_to_parent._textBrowser_3
                self.bot.returnHome()
                time.sleep(0.5)

            elif trigger == 226:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Choose reward\n' + self.connection_to_parent._textBrowser_3
                self.bot.choose_reward(randint(0, 1))
                time.sleep(0.5)

            elif trigger > 230 and trigger < 235:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = f'Open Chest {trigger - 231}\n' + self.connection_to_parent._textBrowser_3
                self.bot.openChest(trigger - 230)
                image = self.bot.getScreen()
                triggers = self.triggers.getTrigger(image)
                trigger = triggers[0]
                if trigger == 229:
                    if self.use_chest_key:
                        self.bot.openChest_2(True)
                self.bot.openChest_2(False)

            elif trigger == 235:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Open pass royale\n' + self.connection_to_parent._textBrowser_3
                self.bot.open_pass_royale()

            elif trigger == 236:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Get shop reward 1/3\n' + self.connection_to_parent._textBrowser_3
                self.bot.goToShop()
                x = 0
                while True:
                    logger.debug(str(triggers))
                    self.connection_to_parent._textBrowser_3 = 'Get shop reward 2/3\n' + self.connection_to_parent._textBrowser_3
                    x += 1
                    self.bot.swipe_shop()
                    try:
                        image = self.bot.getScreen()
                    except:
                        time.sleep(1)
                        self.bot.reboot()
                        continue
                    triggers = self.triggers.getTrigger(image)
                    trigger = triggers[0]
                    if (trigger == 237 and x >=4) or x >= 7:
                        logger.debug(str(triggers))
                        break
                self.connection_to_parent._textBrowser_3 = 'Get shop reward 3/3\n' + self.connection_to_parent._textBrowser_3
                self.bot.get_shop_reward()
                self.bot.returnHome()
                logger.debug(str(triggers))
                continue

            elif trigger == 238:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Skip shop\n' + self.connection_to_parent._textBrowser_3
                self.bot.goToShop()
                self.bot.returnHome()

            elif trigger == 239:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Get reward clan war\n' + self.connection_to_parent._textBrowser_3
                self.bot.get_reward_clan_war()

            elif trigger == 250:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Reward limit\n' + self.connection_to_parent._textBrowser_3
                if self.changed_account:
                    logger.debug(str(triggers))
                    self.increasing_account_number()
                    self.connection_to_parent._textBrowser_3 = 'Changed account 1/2\n' + self.connection_to_parent._textBrowser_3
                    if self.batlle_mode == 'global':
                        logger.debug(str(triggers))
                        self.bot.skipLimit()
                    else:
                        logger.debug(str(triggers))
                        self.bot.returnHome()

                    logger.debug(str(triggers))
                    triggers = self.triggers.getTrigger(image)
                    trigger = triggers[0]
                    self.connection_to_parent._textBrowser_3 = 'Changed account 2/2\n' + self.connection_to_parent._textBrowser_3
                    if trigger == 200:
                        logger.debug(str(triggers))
                        self.bot.changeAccount(self.number_account, self.total_accounts)
                        self.connection_to_parent.number_account = self.number_account
                    else:
                        logger.debug(str(triggers))
                        self.bot.returnHome()
                        self.bot.changeAccount(self.number_account, self.total_accounts)
                        self.connection_to_parent.number_account = self.number_account
                    continue
                else:
                    self.bot.rewardLimit()

            elif trigger == 260:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Return Home\n' + self.connection_to_parent._textBrowser_3
                self.bot.returnHome()

            elif trigger == 261:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Return Home\n' + self.connection_to_parent._textBrowser_3
                self.bot.returnHome()

            elif trigger == 270:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Language set incorrectly\n' + self.connection_to_parent._textBrowser_3
                self.index += 1
                if self.index >= 5:
                    logger.debug(str(triggers))
                    self.bot.setEnglishLanguage()
                else:
                    logger.debug(str(triggers))
                    self.bot.returnHome()
                    time.sleep(2)
                    continue

            elif trigger == 280:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Receiving an award\n' + self.connection_to_parent._textBrowser_3
                self.index280 += 1
                if self.index280 >= 10:
                    logger.debug(str(triggers))
                    self.bot.reboot()
                    self.index280 = 0
                logger.debug(str(triggers))
                self.bot.ADB.click(triggers[1], triggers[2])
                time.sleep(3)
                self.bot.sale_reward()

            elif trigger == 281:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Receiving an award\n' + self.connection_to_parent._textBrowser_3
                self.bot.ADB.click(triggers[1], triggers[2])
                time.sleep(3)
                self.bot.sale_reward()

            elif trigger == 289:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Selling an award\n' + self.connection_to_parent._textBrowser_3
                self.bot.sale_reward()

            elif trigger >= 290 and trigger <= 294:
                logger.debug(str(triggers))
                self.bot.close_reward_masteries()
                self.bot.returnHome()


            elif trigger == 400:
                logger.debug(str(triggers))
                self.connection_to_parent._textBrowser_3 = 'Loss of connection\n' + self.connection_to_parent._textBrowser_3
                self.sleep = False
                time.sleep(300)
                self.sleep = True
                self.bot.exitBatle1X1()

            t = time.time()
            logger.debug(str(triggers))

    def increasing_account_number(self):
        logger.debug('increasing_account_number')
        self.number_account += 1
        if self.number_account >= self.total_accounts:
            self.number_account = 0

    def startFarm(self):
        logger.debug('startFarm')
        self.cycleStart = True
        self.main()

    def stopFarm(self):
        logger.debug('stopFarm')
        self.cycleStart = False