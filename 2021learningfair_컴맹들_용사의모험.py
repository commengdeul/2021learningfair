import os # pause 라이브러리
import random as rd # random 라이브러리
import time # time 라이브러리

# colorCode
BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'
BRIGHT_END = '\033[0m'

bannerMain ='''
'##:::::'##::::'###::::'########::'########::'####::'#######::'########::'####::'######::::::::'###::::'########::'##::::'##::::'###::::'##::: ##:'########:'##::::'##:'########::'########:
 ##:'##: ##:::'## ##::: ##.... ##: ##.... ##:. ##::'##.... ##: ##.... ##: ####:'##... ##::::::'## ##::: ##.... ##: ##:::: ##:::'## ##::: ###:: ##:... ##..:: ##:::: ##: ##.... ##: ##.....::
 ##: ##: ##::'##:. ##:: ##:::: ##: ##:::: ##:: ##:: ##:::: ##: ##:::: ##:. ##:: ##:::..::::::'##:. ##:: ##:::: ##: ##:::: ##::'##:. ##:: ####: ##:::: ##:::: ##:::: ##: ##:::: ##: ##:::::::
 ##: ##: ##:'##:::. ##: ########:: ########::: ##:: ##:::: ##: ########::'##:::. ######:::::'##:::. ##: ##:::: ##: ##:::: ##:'##:::. ##: ## ## ##:::: ##:::: ##:::: ##: ########:: ######:::
 ##: ##: ##: #########: ##.. ##::: ##.. ##:::: ##:: ##:::: ##: ##.. ##:::..:::::..... ##:::: #########: ##:::: ##:. ##:: ##:: #########: ##. ####:::: ##:::: ##:::: ##: ##.. ##::: ##...::::
 ##: ##: ##: ##.... ##: ##::. ##:: ##::. ##::: ##:: ##:::: ##: ##::. ##::::::::'##::: ##:::: ##.... ##: ##:::: ##::. ## ##::: ##.... ##: ##:. ###:::: ##:::: ##:::: ##: ##::. ##:: ##:::::::
. ###. ###:: ##:::: ##: ##:::. ##: ##:::. ##:'####:. #######:: ##:::. ##:::::::. ######::::: ##:::: ##: ########::::. ###:::: ##:::: ##: ##::. ##:::: ##::::. #######:: ##:::. ##: ########:
:...::...:::..:::::..::..:::::..::..:::::..::....:::.......:::..:::::..:::::::::......::::::..:::::..::........::::::...:::::..:::::..::..::::..:::::..::::::.......:::..:::::..::........::
'''

bannerStart = '''
 #                 ##    #                 #    
##                #  #   #                 #    
 #                 #    ###    ###  ###   ###   
 #                  #    #    #  #  #  #   #    
 #     ##         #  #   #    # ##  #      #    
###    ##          ##     ##   # #  #       ##                                                                                                                                   
'''

bannerHelp = '''
 ##               #  #        ##          
#  #              #  #         #          
   #              ####   ##    #    ###   
  #               #  #  # ##   #    #  #  
 #     ##         #  #  ##     #    #  #  
####   ##         #  #   ##   ###   ###   
                                    #     
'''

bannerExit = '''
####              ####         #     #    
   #              #                  #    
 ##               ###   #  #  ##    ###   
   #              #      ##    #     #    
#  #   ##         #      ##    #     #    
 ##    ##         ####  #  #  ###     ##                                                                                                      
'''

# 퀘스트 관련
playerQuestCount1 = 0
playerQuestCount2 = 0
playerQuestCount3 = 0
playerQuestCount4 = 0
playerQuestCount5 = 0

playerSP = 0

listPlayerQuest = []
dictionaryPlayerQuestMonster = {}

# 소모품 아이템 관련
dictionaryItemSmallHPPotion = {'이름' : '기초체력물약', '회복' : 100, '가격' : 5, '타입' : 'hp'}
dictionaryItemMediumHPPotion = {'이름' : '중급체력물약', '회복' : 500, '가격' : 15, '타입' : 'hp'}
dictionaryItemLargeHPPotion = {'이름' : '고급체력물약', '회복' : 1500, '가격' : 150, '타입' : 'hp'}

dictionaryItemSmallMPPotion = {'이름' : '기초마나물약', '회복' : 50, '가격' : 5, '타입' : 'mp'}
dictionaryItemMediumMPPotion = {'이름' : '중급마나물약', '회복' : 200, '가격' : 15, '타입' : 'mp'}
dictionaryItemLargeMPPotion = {'이름' : '고급마나물약', '회복' : 1000, '가격' : 150, '타입' : 'mp'}

dictionaryItemElixir= {'이름' : '엘릭서', '체력회복' : 999999, '가격' : 1999, '타입' : 'all'}

listExpendableItem = [dictionaryItemSmallHPPotion, dictionaryItemSmallMPPotion, dictionaryItemMediumHPPotion, dictionaryItemMediumMPPotion, dictionaryItemLargeHPPotion, dictionaryItemLargeMPPotion, dictionaryItemElixir]

# 장비 아이템 관련
dictionaryItemsWoodenSword = {'이름' : '수련용목검', '공격력' : 5, '가격' : 10, '타입' : '전사'}
dictionaryItemsAdventureSword = {'이름' : '의문의모험가의검', '공격력' : 80, '가격' : 450, '타입' : '전사'}
dictionaryItemsExcalibur = {'이름' : '엑스칼리버', '공격력' : 200, '가격' : 9000, '타입' : '전사'}
dictionaryItemsVoidBlade = {'이름' : '공허의검', '공격력' : 1999, '가격' : 999999, '타입' : '전사'}

dictionaryItemWoodenStaff = {'이름' : '나무지팡이', '공격력' : 10, '가격' : 10, '타입' : '마법사'}
dictionaryItemWizzardStaff = {'이름' : '의문의마법사의지팡이', '공격력' : 70, '가격' : 500, '타입' : '마법사'}
dictionaryItemGambleStaff = {'이름' : '도박사의지팡이', '공격력' : 200, '가격' : 10000, '타입' : '마법사'}
dictionaryItemVoidStaff = {'이름' : '공허의스태프', '공격력' : 1999, '가격' : 999999, '타입' : '마법사'}

listEquipmentItem = [dictionaryItemsWoodenSword, dictionaryItemWoodenStaff, dictionaryItemsAdventureSword, dictionaryItemWizzardStaff, dictionaryItemsExcalibur, dictionaryItemGambleStaff, dictionaryItemsVoidBlade, dictionaryItemVoidStaff]

# 스텟 관련
dictionaryPlayerStat = {'hp' : 0, 'mp' : 0, 'defense' : 0, 'power' : 0}
dictionaryStatsUpper = {'hpUpper' : 0, 'mpUpper' : 0, 'defenseUpper' : 0, 'powerUpper' : 0}

# 시스템 관련
logic = ''
page = ''
location = ''
type = ''
turn = ''

queue = 0
setTime = 0

# 플레이어 관련
playerEquipment = ''
playerGold = 10
playerJob = ''
playerName = ''
listPlayerInventory = []
listPlayerSkill = []

dungeonprogress = 0

dungeonPlayerHP = 0
dungeonPlayerMP = 0

# 직업 관련
dictionaryWarriorStat = {'hp' : 200, 'mp' : 50, 'defense' : 10, 'power' : 10} # 전사
dictionaryWizzardStat = {'hp' : 125, 'mp' : 125, 'defense' : 5, 'power' : 5} # 마법사

dictionaryWarriorSkillQ = {'스킬이름' : '신속베기', 'mp사용' : 25, '공격력' : 10}
dictionaryWizzardSkillQ = {'스킬이름' : '공간발화', 'mp사용' : 50, '공격력' : 20}

listWarriorSkill = [dictionaryWarriorSkillQ, '삼철도', '섬광궤적']
listWizzardSkill = [dictionaryWizzardSkillQ, '아이스버그', '라이트닝볼트']


# 튜토리얼 몬스터
dictionaryMonsterZombie = {"이름" : "좀비", "체력" : 21, "공격력" : 10, "골드" : 10, '타입' : '몬스터'}
listTutorialMonster = [dictionaryMonsterZombie]

# 1층 몬스터 목록
dictionaryMonsterSheep = {"이름" : "양", "체력" : 100, "공격력" : 3, "골드" : 5, '타입' : '몬스터'}
dictionaryMonsterChicken = {"이름" : "닭", "체력" : 50, "공격력" : 5, "골드" : 5, '타입' : '몬스터'}
dictionaryMonsterPig = {"이름" : "돼지", "체력" : 150, "공격력" : 5, "골드" : 5, '타입' : '몬스터'}
dictionaryMonsterCow = {"이름" : "소", "체력" : 200, "공격력" : 10, "골드" : 150, '타입' : '보스'}
listFirstFloorMonster = [dictionaryMonsterSheep, dictionaryMonsterChicken, dictionaryMonsterPig]
firstFloorBoss = dictionaryMonsterCow

# 2층 몬스터 목록
dictionaryMonsterRat = {"이름" : "랫", "체력" : 200, "공격력" : 10, "골드" : 20, '타입' : '몬스터'}
dictionaryMonsterBigRat = {"이름" : "빅 랫", "체력" : 600, "공격력" : 15, "골드" : 23, '타입' : '몬스터'}
dictionaryMonsterGiantRat = {"이름" : "자이언트 랫", "체력" : 1000, "공격력" : 30, "골드" : 400, '타입' : '보스'}
listSecondFloorMonster = [dictionaryMonsterRat, dictionaryMonsterBigRat]
secondFloorBoss = dictionaryMonsterGiantRat

# 3층 몬스터 목록
dictionaryMonsterGoblin = {"이름" : "고블린", "체력" : 1000, "공격력" : 20, "골드" : 45, '타입' : '몬스터'}
dictionaryMonsterSpearGoblin = {"이름" : "창 고블린", "체력" : 1100, "공격력" : 50, "골드" : 50, '타입' : '몬스터'}
dictionaryMonsterMagicianGoblin = {"이름" : "마법사 고블린", "체력" : 800, "공격력" : 70, "골드" : 52, '타입' : '몬스터'}
dictionaryMonsterWarriorGoblin = {"이름" : "전사 고블린", "체력" : 2000, "공격력" : 30, "골드" : 53, '타입' : '몬스터'}
dictionaryMonsterGoblinChampion = {"이름" : "고블린 챔피언", "체력" : 4000, "공격력" : 100, "골드" : 1000, '타입' : '보스'}
listThirdFloorMonster = [dictionaryMonsterGoblin, dictionaryMonsterSpearGoblin, dictionaryMonsterMagicianGoblin, dictionaryMonsterWarriorGoblin]
thirdloorBoss = dictionaryMonsterGoblinChampion

# 4층 몬스터 목록
dictionaryMonsterLizardMan = {"이름" : "리저드맨", "체력" : 3000, "공격력" : 50, "골드" : 110, '타입' : '몬스터'}
dictionaryMonsterSpearLizardMan = {"이름" : "창 리저드맨", "체력" : 3300, "공격력" : 150, "골드" : 137, '타입' : '몬스터'}
dictionaryMonsterWarriorLizardMan = {"이름" : "전사 리전드맨", "체력" : 5000, "공격력" : 100, "골드" : 154, '타입' : '몬스터'}
dictionaryMonsterLizardManKing = {"이름" : "리저드맨 킹", "체력" : 10000, "공격력" : 200, "골드" : 2555, '타입' : '보스'}
listForthFloorMonster = [dictionaryMonsterLizardMan, dictionaryMonsterSpearLizardMan, dictionaryMonsterWarriorLizardMan]
fourthFloorBoss = dictionaryMonsterLizardManKing

# 5층 몬스터 목록
dictionaryMonsterRedDragon = {"이름" : "레드 드래곤", "체력" : 15000, "공격력" : 400, "골드" : 273, '타입' : '몬스터'}
dictionaryMonsterBlueDragon = {"이름" : "블루 드래곤", "체력" : 13000, "공격력" : 500, "골드" : 254, '타입' : '몬스터'}
dictionaryMonsterGreenDragon = {"이름" : "그린 드래곤", "체력" : 30000, "공격력" : 300, "골드" : 264, '타입' : '몬스터'}
dictionaryMonsterGoldDragon = {"이름" : "골드 드래곤", "체력" : 100000, "공격력" : 600, "골드" : 10000, '타입' : '보스'}
listFifthFloorMonster = [dictionaryMonsterRedDragon, dictionaryMonsterBlueDragon, dictionaryMonsterGreenDragon]
fifthFloorBoss = dictionaryMonsterGoldDragon

# 몬스터 floor별 리스트 묶음
listFloorMonster = [listFirstFloorMonster, listSecondFloorMonster, listThirdFloorMonster, listForthFloorMonster, listFifthFloorMonster]
listFloorBossMonster = [firstFloorBoss, secondFloorBoss, thirdloorBoss, fourthFloorBoss, fifthFloorBoss]

# 인벤토리창
def infoInventory():
    global playerGold

    print("[플레이어가 소유한 아이템]")

    for i in range(1, len(listPlayerInventory) + 1):
        print("%d. %s" % (i, (listPlayerInventory[i - 1]['이름'])))
    
    print("(플레이어가 소유한 골드: %dG)" % playerGold)
    
    print("===============================")
    print("[현재 위치: %s]" % location)
    print("1. 소모품 상점으로 이동하기")
    print("2. 장비 상점으로 이동하기")
    print("3. 던전으로 이동하기")
    print("4. 모험가 길드로 이동하기")
    print("[I: 아이템창, E: 장비창, S: 스텟창, Q: 퀘스트창]")
    
# 장비창
def infoEquipment():
    print("[플레이어가 착용한 장비]")

    if len(playerEquipment) == 0:
        print(BRIGHT_RED + "장비를 착용하고 있지 않습니다." + BRIGHT_END)

    else:
        print("무기: %s" % playerEquipment['이름'])

# 퀘스트창
def infoQuest():
    print("[플레이어의 퀘스트 목록]")

    if len(listPlayerQuest) == 0:
        print(BRIGHT_RED + "수락한 퀘스트가 없습니다." + BRIGHT_END)

    else:
        for i in range(0, len(listPlayerQuest)):
            print(listPlayerQuest[i])

# 스텟창
def infoStat():
    print("[플레이어의 스텟]")
    print("체력: %d" % dictionaryPlayerStat['hp'])
    print("마나: %d" % dictionaryPlayerStat['mp'])
    print("방어력: %d" % dictionaryPlayerStat['defense'])
    if len(playerEquipment) == 0:
        print("공격력[플레이어 스텟 + (무기스텟)]: %d + (0)" % (dictionaryPlayerStat['power']))

    else:
        print("공격력[플레이어 스텟 + (무기스텟)]: %d + (%d)" % (dictionaryPlayerStat['power'], (playerEquipment['공격력'])))

# 스킬창
def infoSkill():
    print("[플레이어가 소유한 스킬]")
    
    for i in range(1, len(listPlayerSkill) + 1):
        print("%d. %s" % (i, (listPlayerSkill[i - 1]['이름'])))

# 메인 메뉴 설명 함수
def explanationManu():
    setTime = 3

    print("게임 '용사의 모험'은 텍스트 입출력 기반 RPG 게임입니다.")
    time.sleep(setTime)
    print("게임의 진행은 플레이어가 입력란에 명령어를 입력 시 짜여진 로직에 따라 게임이 작동되게 됩니다.")
    time.sleep(setTime)

# 스토리 설명 함수
def explanationStory():
    str = '<인류에게 갑자기 찾아온 공허 괴물.>'
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    time.sleep(1)
    print()

    str = '<그렇게 인류는 괴물들에게 지구를 침략당한다.>'
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    time.sleep(1)
    print()

    str = '<나약해서 괴물들에게 소중한 이를 계속 잃어가던 순간,>'
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    time.sleep(1)
    print()

    str = '<인류에게 힘을 기를 수 있는 기회가 찾아왔다.>'
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    time.sleep(1)
    print()

    str = '<인류는 괴물에게서 지구를 되찾고자 미궁에 들어간다.>'
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    time.sleep(1)
    print()

    print("===============================")

# 직업 생성 함수
def generateJob(logic):
    global playerJob # 전역변수 playerJob

    if logic == '전사':
        playerJob = '전사'
        return 0

    elif logic == '마법사':
        playerJob = '마법사'
        return 0

# 닉네임 생성 함수
def generateName(logic):
    global playerName # 전역변수 playerName

    playerName = logic
    return 0

# 스텟 랜덤 쉐이커
def generateStatRandomUpper():
    hpUpper = rd.randrange(0,5)
    mpUpper = rd.randrange(0,5)
    defenseUpper = rd.randrange(0,5)
    powerUpper = rd.randrange(0,5)

    return hpUpper, mpUpper, defenseUpper, powerUpper

# 스텟 생성 함수
def generateStatRandom():
    global dictionaryPlayerStat # 전역변수 dictionaryPlayerStat

    if playerJob == "전사":
        hp = dictionaryWarriorStat['hp']
        mp = dictionaryWarriorStat['mp']
        defense = dictionaryWarriorStat['defense']
        power = dictionaryWarriorStat['power']
    elif playerJob == "마법사":
        hp = dictionaryWizzardStat['hp']
        mp = dictionaryWizzardStat['mp']
        defense = dictionaryWizzardStat['defense']
        power = dictionaryWizzardStat['power']

    hpUpper, mpUpper, defenseUpper, powerUpper = generateStatRandomUpper()
    hp = hp + hp / 100 * hpUpper 
    mp = mp + mp / 100 * mpUpper
    defense = defense + defenseUpper
    power = power + powerUpper

    time.sleep(0.5)

    print((BRIGHT_GREEN + "[현재 상태: hp + %d%%, mp + %d%%, defense + %d, power + %d]" + BRIGHT_END) % (hpUpper, mpUpper, defenseUpper, powerUpper))
    dictionaryPlayerStat.update(hp = hp, mp = mp, defense = defense, power = power)

# 소모품 상점
def expendableStore():
    global playerGold

    print("(소모품 상점 주인)", end = ' ')
    str = '어서오세요~ 소모품 상점입니다.'
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    time.sleep(1)
    print()
    str = '다양한 물약을 취급하고 있으니, 마음에 드는 상품이 있으면 저한테 말 해주세요!'
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    time.sleep(1)
    print()

    for i in range(1, len(listExpendableItem) + 1):
        print("%d. %s (가격: %d)" % (i, listExpendableItem[i - 1]['이름'], listExpendableItem[i - 1]['가격']))
    print("0. 상점 나가기")
    print("===============================")
    print("[보유 자금: %d]" % playerGold)

    print("구매하고 싶은 아이템 숫자를 입력해주세요.")
    buy = int(logicInput())

    if buy > 0 and buy <= i:
        if playerGold < listExpendableItem[buy - 1]['가격']:
            print("돈이 부족합니다.")

        else:
            playerGold -= listExpendableItem[buy - 1]['가격']
            listPlayerInventory.append(listExpendableItem[buy - 1])
            print("구매가 완료되었습니다.")
    
    elif buy == 0:
        return 0

    else:
        print("잘못 입력하셨습니다.")
    
# 장비 상점
def equipmentStore():
    global playerGold
    global playerEquipment

    print("(장비 상점 주인)", end = ' ')
    str = '어서오세요, 장비상점입니다.'
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    time.sleep(1)
    print()
    str = '다양한 무기를 취급하고 있습니다. 편하게 둘러보세요.'
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    time.sleep(1)
    print()

    for i in range(1, len(listEquipmentItem) + 1):
        print("%d. %s (가격: %d)" % (i, listEquipmentItem[i - 1]['이름'], listEquipmentItem[i - 1]['가격']))
    print("0. 상점 나가기")
    print("===============================")
    print("[보유 자금: %d]" % playerGold)

    print("구매하고 싶은 아이템 숫자를 입력해주세요.")
    buy = int(logicInput())

    if buy > 0 and buy <= i:
        if playerGold < listEquipmentItem[buy - 1]['가격']:
            print("돈이 부족합니다.")
        
        elif playerJob != listEquipmentItem[buy - 1]['타입']:
            print("직업 타입이 다릅니다.")

        else:
            playerGold -= listEquipmentItem[buy - 1]['가격']
            playerEquipment = listEquipmentItem[buy - 1]

            print("구매 및 장착이 완료되었습니다.")


    elif buy == 0:
        print("===============================")
        print("[현재 위치: %s]" % location)
        print("1. 소모품 상점으로 이동하기")
        print("2. 장비 상점으로 이동하기")
        print("3. 던전으로 이동하기")
        print("4. 모험가 길드로 이동하기")
        print("[I: 아이템창, E: 장비창, S: 스텟창, Q: 퀘스트창]")
        return 0

    else:
        print("잘못 입력하셨습니다.")

# 튜토리얼
def tutorial():
    global playerGold # 전역변수 playerGold
    global dungeonPlayerHP
    global dungeonPlayerMP

    dungeonPlayerHP = dictionaryPlayerStat['hp']
    dungeonPlayerMP = dictionaryPlayerStat['mp']

    setTime = 3
    str = '[1. 전투에 관해 배워보기]'
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    time.sleep(1)
    print()
    print("던전을 탐험하다 보면 적을 만나기 일수입니다.")
    time.sleep(setTime)
    print("시작부터 전투를 진행하면 당황하실게 뻔하니,")
    time.sleep(setTime)
    print("이번 튜토리얼을 통해 가상의 몬스터인 '좀비'를 한 번 상대해보세요!")
    time.sleep(setTime)

    fight(listTutorialMonster[0])

    print("===============================")
    print("수고하셨습니다.")
    time.sleep(setTime)
    print("튜토리얼 보상으로 25G와 기초체력물약 1개를 드렸습니다.")
    time.sleep(setTime)
    print("즐거운 모험되세요!")
    time.sleep(setTime)
    print("===============================")

    listPlayerInventory.append(listExpendableItem[0])
    playerGold += 25

    return 0

# 던전
def dungeon():
    global playerGold
    global dungeonprogress
    global dungeonPlayerHP
    global dungeonPlayerMP

    setTime = 2

    print("던전에 입장하였습니다.")

    dungeonPlayerHP = dictionaryPlayerStat['hp']
    dungeonPlayerMP = dictionaryPlayerStat['mp']

    floor = 1
    situation = 0
    monster = ''
    boss = ''
    findBossRoom = False

    while 1:
        print("===============================")
        print((BRIGHT_GREEN + "[현재: %d 층]" + BRIGHT_END) % floor)
        print("1. 탐색하기")
        print("2. 보스룸으로 향하기")
        print("3. 위층으로 올라가기")
        print("4. 던전 나가기")

        act = logicInput()
        time.sleep(setTime)

        if act == '1':
            situation = rd.randint(1, 101)

            if situation <= 48:
                print("앞에서 부스럭거리는 소리가 들린다.")
                time.sleep(setTime)
                monster = rd.choice(listFloorMonster[floor - 1])
                fight(monster)
            
            elif situation <= 68:
                print("주변을 천천히 살펴보았다.")
                time.sleep(setTime)
                print("이 근처에는 아무것도 없는 것 같다.")
                time.sleep(setTime)
            
            elif situation <= 78:
                print(BRIGHT_RED + "정체불명의 물체에 맞았다." + BRIGHT_END)
                time.sleep(setTime)
                print("아무래도 몬스터의 장난인 것 같다.")
                time.sleep(setTime)

                trapDamage = 4 ** floor

                print((BRIGHT_RED + "HP가 %d만큼 감소하였습니다." + BRIGHT_END)% trapDamage)

                dungeonPlayerHP -= trapDamage
                time.sleep(setTime)

                if dungeonPlayerHP <= 0:
                    print(BRIGHT_RED + "눈 앞이 깜깜해졌다." + BRIGHT_END)
                    break
            
            elif situation <= 98:
                print(BRIGHT_GREEN + "보스룸을 찾았다!" + BRIGHT_END)
                time.sleep(setTime)
                findBossRoom = True
            
            else:
                print(BRIGHT_GREEN + "바닥에 무언가가 반짝거린다" + BRIGHT_END)
                time.sleep(setTime)
                situation = rd.randint(1, 3)
                if situation == 1:
                    print(BRIGHT_GREEN + "엘릭서를 주웠다!" + BRIGHT_END)
                    listPlayerInventory.append(listExpendableItem[6])
                    time.sleep(setTime)

                else:
                    situation = rd.randint(1, 1001)
                    playerGold += situation
                    print((BRIGHT_GREEN + "%d골드를 주웠다! (현재 보유 골드: %d)" + BRIGHT_END)% (situation, playerGold))
                    time.sleep(setTime)

        elif act == '2':
            if findBossRoom == True:
                print("보스룸에 입장하였습니다.")
                time.sleep(setTime)
                boss = listFloorBossMonster[floor - 1]
                fight(boss)
            
            elif findBossRoom == False:
                print("아직 보스룸을 찾지 못하였습니다.")
                time.sleep(setTime)
            
        elif act == '3':
            if dungeonprogress >= floor:
                print("다음 층으로 올라갑니다.")
                time.sleep(setTime)
                floor += 1
            
            else:
                print("아직 해당 층의 보스를 잡지 못하여 다음 층으로 올라갈 수 없습니다.")
                time.sleep(setTime)
        
        elif act == '4':
            print("던전을 나갑니다.")
            time.sleep(setTime)
            prints()
            break

        else:
            print("다시 입력해주세요.")
            continue

    if dungeonPlayerHP <= 0:
        lostGold = playerGold / 10
        print((BRIGHT_RED + "%d원을 잃었다!" + BRIGHT_END) % lostGold )
        playerGold -= lostGold
        print("===============================")
        print("[현재 위치: %s]" % location)
        print("1. 소모품 상점으로 이동하기")
        print("2. 장비 상점으로 이동하기")
        print("3. 던전으로 이동하기")
        print("4. 모험가 길드로 이동하기")
        print("[I: 아이템창, E: 장비창, S: 스텟창, Q: 퀘스트창]")
        return 0

# 퀘스트 수락 프린트
def questAcceptPrint():
    str = '퀘스트를 수락하였습니다.'
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    print()
    time.sleep(1)
    print("===============================")

# 퀘스트 완료 프린트
def questClearPrint(quest, gold, sp):
    str = ('퀘스트를 (%s) 완료하였습니다.' %(quest))
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    print()
    str = ('보상으로 %dG 와 %dsp 가 주어졌습니다.' %(gold, sp))
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    print()
    time.sleep(1)
    print("===============================")

# 길드
def guild():
    global location # 전역변수 location
    global playerGold # 전역변수 playerGold
    global playerSP
    global playerQuestCount1 # 전역변수 playerQuestCount1
    global playerQuestCount2 # 전역변수 playerQuestCount2
    global playerQuestCount3 # 전역변수 playerQuestCount3
    global playerQuestCount4 # 전역변수 playerQuestCount4
    global playerQuestCount5 # 전역변수 playerQuestCount5

    if playerEquipment == '':
        time.sleep(1)
        print(BRIGHT_GREEN + "[메인 퀘스트 -> 첫 장비를 구매하기 | 보상(골드 10 / 5 sp)]" + BRIGHT_END)
        time.sleep(2)
        str = '마을에 처음 오게 된 플레이어는 무기 없이 던전에 들어갈 순 없었습니다.' # 첫 장비 구매하기 퀘스트
        for run in range(1,2):
            for i in str:
                print(i, end = '')
                time.sleep(0.1)
        print()
        time.sleep(1)
        str = '따라서 모험가 길드의 자문을 구해보니, 마을에 장비 상점이 있다고 합니다.' # 첫 장비 구매하기 퀘스트
        for run in range(1,2):
            for i in str:
                print(i, end = '')
                time.sleep(0.1)
        print()
        time.sleep(1)
        str = '무기 상점에 가서 자기 직업에 맞는 무기를 한 개 사보아요!' # 첫 장비 구매하기 퀘스트
        for run in range(1,2):
            for i in str:
                print(i, end = '')
                time.sleep(0.1)
        print()
        time.sleep(1)
        print(BRIGHT_GREEN + "[수락하시겠습니까? (Y / N)]" + BRIGHT_END)
        mainAccept = logicInput()
        if mainAccept == 'Y':
            listPlayerQuest.append("메인 퀘스트 | 첫 장비를 구매하기 | 보상(골드 10 / 5 sp)") # 첫 장비 구매하기 퀘스트
            questAcceptPrint()



    else:
        if "메인 퀘스트 | 첫 장비를 구매하기 | 보상(골드 10 / 5 sp)" in listPlayerQuest: # 첫 장비 구매하기 퀘스트 달성 조건
            if playerEquipment != '':
                playerGold += 10
                playerSP += 5
                questClearPrint("첫 장비를 구매하기", 10, 5)
                print(BRIGHT_GREEN + "[sp는 hp를 증가시켜줍니다.]" + BRIGHT_END)
                spIntoHp(5)
                listPlayerQuest.remove("메인 퀘스트 | 첫 장비를 구매하기 | 보상(골드 10 / 5 sp)")


        if dungeonprogress >= 0:
            if '소' in dictionaryPlayerQuestMonster.keys():   # 첫번째 메인 퀘스트 달성 조건
                if dictionaryPlayerQuestMonster['소'] >= 1:
                    playerGold += 100
                    playerSP += 10
                    questClearPrint("소 1마리 잡기", 100, 10)
                    spIntoHp(10)
                    dictionaryPlayerQuestMonster['소'] = 0

                    # 스킬언락
                    if playerJob == '전사':
                        listPlayerSkill.append(listWarriorSkill[1])

                    elif playerJob == '마법사':
                        listPlayerSkill.append(listWizzardSkill[1])


                    time.sleep(1)
                    str = '새로운 스킬이 언락되었습니다!' 
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)
                    print()
                    time.sleep(1)

                    listPlayerQuest.remove("[메인 퀘스트 | 소 1마리 잡기 | 보상(골드 100 / 10 sp)]")

            else:
                print("===============================")
                print(BRIGHT_GREEN + "[메인 퀘스트 | 소 1마리 잡기 | 보상(골드 100 / 10 sp)]" + BRIGHT_END)   # 첫번째 메인 퀘스트
                time.sleep(1)
                str = '모험하기 전에, 우리는 너의 모험에 대한 재능을 확인해야 해!' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '너의 재능을 입증하기 위해, 소 1마리를 잡아줄 수 있을까?' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                mainAccept = logicInput()
                if mainAccept == 'Y':
                    questAcceptPrint()
                    dictionaryPlayerQuestMonster['소'] = 0
                    print()
                    time.sleep(1)

                    listPlayerQuest.append("메인 퀘스트 | 소 1마리 잡기 | 보상(골드 100 / 10 sp)")

            if ('양' in dictionaryPlayerQuestMonster.keys()) and ('닭' in dictionaryPlayerQuestMonster.keys()) and ('돼지' in dictionaryPlayerQuestMonster.keys()):
                if (dictionaryPlayerQuestMonster['양'] >= 1) and (dictionaryPlayerQuestMonster['닭'] >= 1) and (dictionaryPlayerQuestMonster['돼지']) >= 1:   # 첫번째 서브 퀘스트 달성 조건
                    playerGold += 100
                    if playerQuestCount1 == 0:
                        playerSP += 8
                        playerQuestCount1 += 1
                    questClearPrint("양 1마리, 닭 1마리, 돼지 1마리", 100, 8)
                    spIntoHp(8)
                    listPlayerQuest.remove("서브 퀘스트 | 양 1마리, 닭 1마리, 돼지 1마리 | 보상(골드 100 / 8sp)")
                    dictionaryPlayerQuestMonster['양'], dictionaryPlayerQuestMonster['닭'], dictionaryPlayerQuestMonster['돼지'] = 0, 0, 0

                    print("===============================")
                    print(BRIGHT_GREEN + "[서브 퀘스트 | 양 1마리, 닭 1마리, 돼지 1마리 | 보상(골드 100 / 8sp)]" + BRIGHT_END)   # 첫번째 서브 퀘스트
                    time.sleep(1)
                    str = '1층에 동물이 많아진 모양이야!!'
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)
                    print()
                    time.sleep(1)
                    str = '동물을 잡아줄 수 있을까?'
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)
                    print()
                    time.sleep(1)
                    print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                    subAccept = logicInput()
                    if subAccept == 'Y':
                        questAcceptPrint()
                        dictionaryPlayerQuestMonster['양'], dictionaryPlayerQuestMonster['닭'], dictionaryPlayerQuestMonster['돼지'] = 0, 0, 0
                        listPlayerQuest.append("서브 퀘스트 | 양 1마리, 닭 1마리, 돼지 1마리 | 보상(골드 100 / 8sp)")
                    elif (dictionaryPlayerQuestMonster['양'] >= 0) and (dictionaryPlayerQuestMonster['닭'] >= 0) and (dictionaryPlayerQuestMonster['돼지']) >= 0:
                        print("서브 퀘스트 | 양 1마리, 닭 1마리, 돼지 1마리 | 퀘스트가 진행중입니다.")

            else:
                print("===============================")
                print("[서브 퀘스트 | 양 1마리, 닭 1마리, 돼지 1마리 | 보상(골드 100 / 8sp)]")   # 첫번째 서브 퀘스트
                time.sleep(1)
                str = '1층에 동물이 많아진 모양이야!!'
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '동물을 잡아줄 수 있을까?'
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                print("수락하시겠습니까? (Y / N)")
                subAccept = logicInput()
                if subAccept == 'Y':
                    questAcceptPrint()
                    dictionaryPlayerQuestMonster['양'], dictionaryPlayerQuestMonster['닭'], dictionaryPlayerQuestMonster['돼지'] = 0, 0, 0
                    listPlayerQuest.append("서브 퀘스트 | 양 1마리, 닭 1마리, 돼지 1마리 | 보상(골드 100 / 8sp)")
                

        if dungeonprogress >= 1:
            if '자이언트 랫' in dictionaryPlayerQuestMonster.keys():   # 두번째 메인 퀘스트 달성 조건
                if dictionaryPlayerQuestMonster['자이언트 랫'] >= 1:
                    playerGold += 350
                    playerSP += 15
                    questClearPrint("자이언트 랫 1마리 잡기", 350, 15)
                    spIntoHp(15)
                    dictionaryPlayerQuestMonster['자이언트 랫'] = 0

                    # 스킬언락
                    if playerJob == '전사':
                        listPlayerSkill.append(listWarriorSkill[2])

                    elif playerJob == '마법사':
                        listPlayerSkill.append(listWizzardSkill[2])

                    time.sleep(1)
                    str = '새로운 스킬이 언락되었습니다!' 
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)

                    listPlayerQuest.remove("메인 퀘스트 | 자이언트 랫 1마리 잡기 | 보상(골드 350 / 15 sp)")

            else:
                print("===============================")
                print(BRIGHT_GREEN + "[메인 퀘스트 | 자이언트 랫 1마리 잡기 | 보상(골드 350 / 15 sp)]" + BRIGHT_END)   # 두번째 메인 퀘스트
                time.sleep(1)
                str = '우리 길드원이 2층 던전에서 랫을 사냥하던 중, 자이언트 랫을 발견했데.' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '혹시 자이언트 랫을 잡아줄 수 있을까?' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '보상은 충분히 줄게!' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                mainAccept = logicInput()
                if mainAccept == 'Y':
                    questAcceptPrint()
                    dictionaryPlayerQuestMonster['자이언트 랫'] = 0
                    listPlayerQuest.append("메인 퀘스트 | 자이언트 랫 1마리 잡기 | 보상(골드 350 / 15 sp)")

            if ('랫' in dictionaryPlayerQuestMonster.keys()) and ('빅 랫' in dictionaryPlayerQuestMonster.keys()):
                if (dictionaryPlayerQuestMonster['랫'] >= 2) and (dictionaryPlayerQuestMonster['빅 랫'] >= 1):   # 두번째 서브 퀘스트 달성 조건
                    playerGold += 350
                    if playerQuestCount2 == 0:
                        playerSP += 10
                        playerQuestCount2 += 1
                    questClearPrint("랫 2마리, 빅랫 1마리", 350, 10)
                    spIntoHp(10)

                    listPlayerQuest.remove("서브 퀘스트 | 랫 2마리, 빅랫 1마리 | 보상(골드 350 / 10sp)")
                    dictionaryPlayerQuestMonster['랫'], dictionaryPlayerQuestMonster['빅 랫'] = 0, 0

                    print("===============================")
                    print(BRIGHT_GREEN + "[서브 퀘스트 | 랫 2마리, 빅랫 1마리 | 보상(골드 350 / 10sp)]" + BRIGHT_END)   # 두번째 서브 퀘스트
                    time.sleep(1)
                    str = '2층에 랫이 많아진 모양이야!' 
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)
                    print()
                    time.sleep(1)
                    str = '랫을 잡아줄 수 있을까?' 
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)
                    print()
                    time.sleep(1)
                    print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                    subAccept = logicInput()
                    if subAccept == 'Y':
                        questAcceptPrint()
                        dictionaryPlayerQuestMonster['랫'], dictionaryPlayerQuestMonster['빅 랫'] = 0, 0
                        listPlayerQuest.append("서브 퀘스트 | 랫 2마리, 빅랫 1마리 | 보상(골드 350 / 10sp)")

                elif (dictionaryPlayerQuestMonster['랫'] >= 0) and (dictionaryPlayerQuestMonster['빅 랫'] >= 0):
                    print("서브 퀘스트 | 랫 2마리, 빅랫 1마리 | 퀘스트가 진행중입니다.")
            else:
                print("===============================")
                print(BRIGHT_GREEN + "[서브 퀘스트 | 랫 2마리, 빅랫 1마리 | 보상(골드 350 / 10sp)]" + BRIGHT_END)   # 두번째 서브 퀘스트
                time.sleep(1)
                str = '2층에 랫이 많아진 모양이야!' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '랫을 잡아줄 수 있을까?' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                subAccept = logicInput()
                if subAccept == 'Y':
                    questAcceptPrint()
                    dictionaryPlayerQuestMonster['랫'], dictionaryPlayerQuestMonster['빅 랫'] = 0, 0
                    listPlayerQuest.append("서브 퀘스트 | 랫 2마리, 빅랫 1마리 | 보상(골드 350 / 10sp)")



        if dungeonprogress >= 2:
            if '고블린 챔피언' in dictionaryPlayerQuestMonster.keys():   # 세번째 메인 퀘스트 달성 조건
                if dictionaryPlayerQuestMonster['고블린 챔피언'] >= 1:
                    playerGold += 900
                    playerSP += 15
                    questClearPrint("고블린챔피언 1마리 잡기", 900, 15)
                    spIntoHp(15)
                    dictionaryPlayerQuestMonster['고블린 챔피언'] = 0
                    listPlayerQuest.remove("메인 퀘스트 | 고블린챔피언 1마리 잡기 | 보상(골드 900 / 15 sp)")

            else:
                print("===============================")
                print(BRIGHT_GREEN + "메인 퀘스트 | 고블린챔피언 1마리 잡기 | 보상(골드 900 / 15 sp)" + BRIGHT_END)   # 세번째 메인 퀘스트
                time.sleep(1)
                str = '너 그 소식 들었어?? 최근 고블린의 개체 수가 증가하면서 고블린 챔피언이 나타났다고 해!!' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '3층에서 사냥하는 길드원이 다칠까 봐 그런데, 혹시 네가 고블린 챔피언을 잡아 줄 수 있을까?' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '보상은 충분히 줄게!' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                mainAccept = logicInput()
                if mainAccept == 'Y':
                    questAcceptPrint()
                    dictionaryPlayerQuestMonster['고블린 챔피언'] = 0
                    listPlayerQuest.append("메인 퀘스트 | 고블린챔피언 1마리 잡기 | 보상(골드 900 / 15 sp)")
    
            if ('고블린' in dictionaryPlayerQuestMonster.keys()) and ('창 고블린' in dictionaryPlayerQuestMonster.keys()) and ('마법사 고블린' in dictionaryPlayerQuestMonster.keys()) and ('전사 고블린' in dictionaryPlayerQuestMonster.keys()):
                if (dictionaryPlayerQuestMonster['고블린'] >= 2) and (dictionaryPlayerQuestMonster['창 고블린'] >= 1) and (dictionaryPlayerQuestMonster['마법사 고블린']) >= 1 and (dictionaryPlayerQuestMonster['전사 고블린']) >= 1:   # 세번째 서브 퀘스트 달성 조건
                    playerGold += 900
                    if playerQuestCount3 == 0:
                        playerSP += 30
                        playerQuestCount3 += 1
                    questClearPrint("고블린 2마리, 창 고블린 1마리, 마법 고블린 1마리, 전사 고블린 1마리", 900, 30)
                    spIntoHp(30)
                    listPlayerQuest.remove("서브 퀘스트 | 고블린 2마리, 창 고블린 1마리, 마법 고블린 1마리, 전사 고블린 1마리 | 보상(골드 900 / 30sp)")
                    dictionaryPlayerQuestMonster['고블린'], dictionaryPlayerQuestMonster['창 고블린'], dictionaryPlayerQuestMonster['마법사 고블린'], dictionaryPlayerQuestMonster['전사 고블린'] = 0, 0, 0, 0

                    print("===============================")
                    print(BRIGHT_GREEN + "서브 퀘스트 | 고블린 2마리, 창 고블린 1마리, 마법 고블린 1마리, 전사 고블린 1마리 | 보상(골드 900 / 30sp)" + BRIGHT_END)   # 세번째 서브 퀘스트
                    time.sleep(1)
                    str = '3층에 고블린이 많아진 모양이야!!' 
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)
                        print()
                    time.sleep(1)
                    str = '고블린을 잡아줄 수 있을까?' 
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)
                    print()
                    time.sleep(1)
                    print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                    subAccept = logicInput()
                    if subAccept == 'Y':
                        questAcceptPrint()
                        dictionaryPlayerQuestMonster['고블린'], dictionaryPlayerQuestMonster['창 고블린'], dictionaryPlayerQuestMonster['마법사 고블린'], dictionaryPlayerQuestMonster['전사 고블린'] = 0, 0, 0, 0
                        listPlayerQuest.append("서브 퀘스트 | 고블린 2마리, 창 고블린 1마리, 마법 고블린 1마리, 전사 고블린 1마리 | 보상(골드 900 / 30sp)")

                elif (dictionaryPlayerQuestMonster['고블린'] >= 0) and (dictionaryPlayerQuestMonster['창 고블린'] >= 0) and (dictionaryPlayerQuestMonster['마법사 고블린'] >= 0) and (dictionaryPlayerQuestMonster['전사 고블린'] >= 0):
                    print("서브 퀘스트 | 고블린 2마리, 창 고블린 1마리, 마법 고블린 1마리, 전사 고블린 1마리 | 퀘스트가 진행중입니다.")
            else:
                print("===============================")
                print(BRIGHT_GREEN + "서브 퀘스트 | 고블린 2마리, 창 고블린 1마리, 마법 고블린 1마리, 전사 고블린 1마리 | 보상(골드 900 / 30sp)" + BRIGHT_END)   # 세번째 서브 퀘스트
                time.sleep(1)
                str = '3층에 고블린이 많아진 모양이야!!' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                    print()
                time.sleep(1)
                str = '고블린을 잡아줄 수 있을까?' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                subAccept = logicInput()
                if subAccept == 'Y':
                    questAcceptPrint()
                    dictionaryPlayerQuestMonster['고블린'], dictionaryPlayerQuestMonster['창 고블린'], dictionaryPlayerQuestMonster['마법사 고블린'], dictionaryPlayerQuestMonster['전사 고블린'] = 0, 0, 0, 0
                    listPlayerQuest.append("서브 퀘스트 | 고블린 2마리, 창 고블린 1마리, 마법 고블린 1마리, 전사 고블린 1마리 | 보상(골드 900 / 30sp)")



        if dungeonprogress >= 3:
            if '리저드맨 킹' in dictionaryPlayerQuestMonster.keys():   # 네번째 메인 퀘스트 달성 조건
                if dictionaryPlayerQuestMonster['리저드맨 킹'] >= 1:
                    playerGold += 2300	
                    playerSP += 55
                    questClearPrint("리저드맨 킹 1마리 잡기", 2300, 55)
                    spIntoHp(55)
                    dictionaryPlayerQuestMonster['리저드맨 킹'] = 0
                    listPlayerQuest.remove("메인 퀘스트 | 리저드맨 킹 1마리 잡기 | 보상(골드 2300 / 55 sp)")

            else:
                print("===============================")
                print(BRIGHT_GREEN + "메인 퀘스트 | 리저드맨 킹 1마리 잡기 | 보상(골드 2300 / 55 sp)" + BRIGHT_END)   # 네번째 메인 퀘스트
                time.sleep(1)
                str = '길드장님이 5층에 있는 드래곤들을 약화하기 위해서, 리저드맨 킹을 잡아야 한데!' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '혹시 네가 잡아줄 수 있을까?' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '보상은 충분히 줄게!' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                mainAccept = logicInput()
                if mainAccept == 'Y':
                    questAcceptPrint()
                    dictionaryPlayerQuestMonster['리저드맨 킹'] = 0
                    listPlayerQuest.append("메인 퀘스트 | 리저드맨 킹 1마리 잡기 | 보상(골드 2300 / 55 sp)")

            if ('리저드맨' in dictionaryPlayerQuestMonster.keys()) and ('창 리저드맨' in dictionaryPlayerQuestMonster.keys()) and ('전사 리전드맨' in dictionaryPlayerQuestMonster.keys()):
                if (dictionaryPlayerQuestMonster['리저드맨'] >= 5) and (dictionaryPlayerQuestMonster['창 리저드맨'] >= 3) and (dictionaryPlayerQuestMonster['전사 리전드맨']) >= 4:   # 네번째 서브 퀘스트 달성 조건
                    playerGold += 2300
                    if playerQuestCount4 == 0:
                        playerSP += 30
                        playerQuestCount4 += 1
                    questClearPrint("리저드맨 5마리, 창 리저드맨 3마리, 전사 리저드맨 4마리", 2300, 30)
                    spIntoHp(30)
                    listPlayerQuest.remove("서브 퀘스트 | 리저드맨 5마리, 창 리저드맨 3마리, 전사 리저드맨 4마리 | 보상(골드 2300 / 30sp)")
                    dictionaryPlayerQuestMonster['리저드맨'], dictionaryPlayerQuestMonster['창 리저드맨'], dictionaryPlayerQuestMonster['전사 리전드맨'] = 0, 0, 0

                    print("===============================")
                    print(BRIGHT_GREEN + "서브 퀘스트 | 리저드맨 5마리, 창 리저드맨 3마리, 전사 리저드맨 4마리 | 보상(골드 2300 / 30sp)" + BRIGHT_END)   # 네번째 서브 퀘스트
                    time.sleep(1)
                    str = '4층에 리저드맨이 많아진 모양이야!!' 
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)
                    print()
                    time.sleep(1)
                    str = '리저드맨을 잡아줄 수 있을까?' 
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)
                    print()
                    time.sleep(1)
                    print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                    subAccept = logicInput()
                    if subAccept == 'Y':
                        questAcceptPrint()
                        dictionaryPlayerQuestMonster['리저드맨'], dictionaryPlayerQuestMonster['창 리저드맨'], dictionaryPlayerQuestMonster['전사 리전드맨'] = 0, 0, 0
                        listPlayerQuest.append("서브 퀘스트 | 리저드맨 5마리, 창 리저드맨 3마리, 전사 리저드맨 4마리 | 보상(골드 2300 / 30sp)")

                elif (dictionaryPlayerQuestMonster['리저드맨'] >= 0) and (dictionaryPlayerQuestMonster['창 리저드맨'] >= 0) and (dictionaryPlayerQuestMonster['전사 리전드맨']) >= 0:
                    print("서브 퀘스트 | 리저드맨 5마리, 창 리저드맨 3마리, 전사 리저드맨 4마리 | 퀘스트가 진행중입니다.")
            else:
                print("===============================")
                print(BRIGHT_GREEN + "서브 퀘스트 | 리저드맨 5마리, 창 리저드맨 3마리, 전사 리저드맨 4마리 | 보상(골드 2300 / 30sp)" + BRIGHT_END)   # 네번째 서브 퀘스트
                time.sleep(1)
                str = '4층에 리저드맨이 많아진 모양이야!!' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '리저드맨을 잡아줄 수 있을까?' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                subAccept = logicInput()
                if subAccept == 'Y':
                    questAcceptPrint()
                    dictionaryPlayerQuestMonster['리저드맨'], dictionaryPlayerQuestMonster['창 리저드맨'], dictionaryPlayerQuestMonster['전사 리전드맨'] = 0, 0, 0
                    listPlayerQuest.append("서브 퀘스트 | 리저드맨 5마리, 창 리저드맨 3마리, 전사 리저드맨 4마리 | 보상(골드 2300 / 30sp)")



        if dungeonprogress >= 4:
            if '골드 드래곤' in dictionaryPlayerQuestMonster.keys():   # 다섯번째 메인 퀘스트 달성 조건
                if dictionaryPlayerQuestMonster['골드 드래곤'] >= 1:
                    playerGold += 7500
                    playerSP += 80
                    questClearPrint("골드 드래곤 1마리 잡기", 7500, 80)
                    spIntoHp(80)
                    dictionaryPlayerQuestMonster['골드 드래곤'] = 0
                    listPlayerQuest.remove("메인 퀘스트 | 골드 드래곤 1마리 잡기 | 보상(골드 7500 / 80 sp)")

            else:
                print("===============================")
                print(BRIGHT_GREEN + "메인 퀘스트 | 골드 드래곤 1마리 잡기 | 보상(골드 7500 / 80 sp)" + BRIGHT_END)   # 다섯번째 메인 퀘스트
                time.sleep(1)
                str = '드래곤을 잡을 생각이구나!! 드래곤 중에 골드 드래곤이라고 있는 거 알아?' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '골드 드래곤을 잡으면, 무기상점에 있는 공허 관련 무기를 구매할 수 있을 정도의 골드를 보상으로 줄게?' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '잡아 줄 수 있을까?' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                mainAccept = logicInput()
                if mainAccept == 'Y':
                    questAcceptPrint()
                    dictionaryPlayerQuestMonster['골드 드래곤'] = 0
                    listPlayerQuest.append("메인 퀘스트 | 골드 드래곤 1마리 잡기 | 보상(골드 7500 / 80 sp)")

            if ('레드 드래곤' in dictionaryPlayerQuestMonster.keys()) and ('블루 드래곤' in dictionaryPlayerQuestMonster.keys()) and ('그린 드래곤' in dictionaryPlayerQuestMonster.keys()):
                if (dictionaryPlayerQuestMonster['레드 드래곤'] >= 30) and (dictionaryPlayerQuestMonster['블루 드래곤'] >= 30) and (dictionaryPlayerQuestMonster['그린 드래곤']) >= 30:   # 다섯번째 서브 퀘스트 달성 조건
                    playerGold += 7500
                    if playerQuestCount5 == 0:
                        playerSP += 50
                        playerQuestCount5 += 1
                    questClearPrint("레드 드래곤 30마리, 블루 드래곤 30마리, 그린 드래곤 30마리", 7500, 50)
                    spIntoHp(50)
                    listPlayerQuest.remove("서브 퀘스트 | 레드 드래곤 30마리, 블루 드래곤 30마리, 그린 드래곤 30마리 | 보상(골드 7500 / 50sp)")
                    dictionaryPlayerQuestMonster['레드 드래곤'], dictionaryPlayerQuestMonster['블루 드래곤'], dictionaryPlayerQuestMonster['그린 드래곤'] = 0, 0, 0

                    print("===============================")
                    print(BRIGHT_GREEN + "서브 퀘스트 | 레드 드래곤 30마리, 블루 드래곤 30마리, 그린 드래곤 30마리 | 보상(골드 7500 / 50sp)" + BRIGHT_END)   # 다섯번째 서브 퀘스트
                    time.sleep(1)
                    str = '5층에 드래곤가 많아진 모양이야!! ' 
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)
                    print()
                    time.sleep(1)
                    str = '드래곤을 잡아줄 수 있을까?' 
                    for run in range(1,2):
                        for i in str:
                            print(i, end = '')
                            time.sleep(0.1)
                    print()
                    time.sleep(1)
                    print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                    subAccept = logicInput()
                    if subAccept == 'Y':
                        questAcceptPrint()
                        dictionaryPlayerQuestMonster['레드 드래곤'], dictionaryPlayerQuestMonster['블루 드래곤'], dictionaryPlayerQuestMonster['그린 드래곤'] = 0, 0, 0
                        listPlayerQuest.append("서브 퀘스트 | 레드 드래곤 30마리, 블루 드래곤 30마리, 그린 드래곤 30마리 | 보상(골드 7500 / 50sp)")

                elif (dictionaryPlayerQuestMonster['레드 드래곤'] >= 0) and (dictionaryPlayerQuestMonster['블루 드래곤'] >= 0) and (dictionaryPlayerQuestMonster['그린 드래곤']) >= 0:
                    print("서브 퀘스트 | 레드 드래곤 30마리, 블루 드래곤 30마리, 그린 드래곤 30마리 | 퀘스트가 진행중입니다.")
            else:
                print("===============================")
                print(BRIGHT_GREEN + "서브 퀘스트 | 레드 드래곤 30마리, 블루 드래곤 30마리, 그린 드래곤 30마리 | 보상(골드 7500 / 50sp)" + BRIGHT_END)   # 다섯번째 서브 퀘스트
                time.sleep(1)
                str = '5층에 드래곤가 많아진 모양이야!! ' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                str = '드래곤을 잡아줄 수 있을까?' 
                for run in range(1,2):
                    for i in str:
                        print(i, end = '')
                        time.sleep(0.1)
                print()
                time.sleep(1)
                print(BRIGHT_GREEN + "수락하시겠습니까? (Y / N)" + BRIGHT_END)
                subAccept = logicInput()
                if subAccept == 'Y':
                    questAcceptPrint()
                    dictionaryPlayerQuestMonster['레드 드래곤'], dictionaryPlayerQuestMonster['블루 드래곤'], dictionaryPlayerQuestMonster['그린 드래곤'] = 0, 0, 0
                    listPlayerQuest.append("서브 퀘스트 | 레드 드래곤 30마리, 블루 드래곤 30마리, 그린 드래곤 30마리 | 보상(골드 7500 / 50sp)")


    prints()
    return 0

# SP -> HP 증가 함수
def spIntoHp(playerSP):
    if playerJob == '전사':
        dictionaryPlayerStat['hp'] += playerSP * 30
        dictionaryPlayerStat['mp'] += playerSP * 15

    elif playerJob == '마법사':
        dictionaryPlayerStat['hp'] += playerSP * 15
        dictionaryPlayerStat['mp'] += playerSP * 30

# 마을 이동 함수
def travel():
    global location

    print("[어느 지역으로 이동하시겠습니까?]")
    print("1. 고대시대에 존재했던 마을")
    print("2. secondTown")

    locationInput = logicInput()

    if locationInput > 0 and locationInput <= 2:

        if locationInput == '1':
            location = '고대시대에 존재했던 마을'

        elif locationInput == '2':
            location = 'secondTown'
    
    else:
        print("잘못 입력하셨습니다.")

# 전투 함수
def fight(monster):
    global playerGold # 전역변수 playerGold
    global dungeonprogress

    setTime = 2

    print("===============================")
    print((BRIGHT_RED + "[%s(이)가 나타났다!]" + BRIGHT_END) % (monster['이름']))

    playerHP = dungeonPlayerHP
    playerMaxHP = dictionaryPlayerStat['hp']

    playerMP = dungeonPlayerMP
    playerMaxMP = dictionaryPlayerStat['mp']

    monsterHP = monster['체력']

    if len(playerEquipment) == 0:
        playerPower = dictionaryPlayerStat['power']

    else:
        playerPower = dictionaryPlayerStat['power'] + playerEquipment['공격력']

    while 1:
        print("%s의 체력: %d, 마나: %d" % (playerName, playerHP, playerMP))
        print("%s의 체력: %d" % (monster['이름'], monsterHP))
        print("===============================")
        print("[A) 공격하기, S) 스킬사용, I) 아이템사용]")
        act = logicInput()

        if act == 'A' or act == 'S' or act == 'I':

            # 일반공격
            if act == "A":
                time.sleep(setTime)

                if playerJob == "전사":
                    print(BRIGHT_GREEN + "휘두르기!" + BRIGHT_END)
                    time.sleep(setTime)

                    monsterHP -= dictionaryPlayerStat['power']

                    print((BRIGHT_GREEN +"%s에게 %d의 데미지를 입혔습니다." + BRIGHT_END)% (monster['이름'], dictionaryPlayerStat['power']))
                        
                elif playerJob == "마법사":
                    print(BRIGHT_GREEN + "마법공격!" + BRIGHT_END)
                    time.sleep(setTime)

                    monsterHP -= dictionaryPlayerStat['power']

                    print((BRIGHT_GREEN + "%s에게 %d의 데미지를 입혔습니다." + BRIGHT_END) % (monster['이름'], dictionaryPlayerStat['power']))
                
            # 스킬사용
            elif act == "S":
                    time.sleep(setTime)

                    if len(listPlayerSkill) == 1:
                        Q = listPlayerSkill[0]

                        print("Q) %s" % Q['스킬이름'])
                        skill = logicInput()

                    elif len(listPlayerSkill) == 2:
                        Q = listPlayerSkill[0]
                        W = listPlayerSkill[1]

                        print("Q) %s, W) %s" % (Q['스킬이름'], W['스킬이름']))
                        skill = logicInput()
                    
                    elif len(listPlayerSkill) == 3:
                        Q = listPlayerSkill[0]
                        W = listPlayerSkill[1]
                        E = listPlayerSkill[2]

                        print("Q) %s, W) %s, E) %s" % (Q['스킬이름'], W['스킬이름'], E['스킬이름']))
                        skill = logicInput()

                    if skill == 'Q' or skill == 'W' or skill == 'E':
                        if skill == 'Q':
                            print((BRIGHT_GREEN + "%s의 %s!!!" + BRIGHT_END)% (playerName, Q['스킬이름']))

                            if playerJob == '전사':
                                Q['공격력'] = playerPower + playerPower / 2
                                Q['mp사용'] = 50


                            elif playerJob == '마법사':
                                Q['공격력'] = playerPower + playerPower / 4
                                Q['mp사용'] = 25

                            if playerMP < Q['mp사용']:
                                print(BRIGHT_RED + "마나가 부족합니다." + BRIGHT_END)
                            
                            else:
                                monsterHP -= Q['공격력']
                                playerMP -= Q['mp사용']

                                time.sleep(setTime)

                                print((BRIGHT_GREEN + "%s에게 %d의 데미지를 입혔습니다." + BRIGHT_END) % (monster['이름'], Q['공격력']))
                    
                        elif skill == 'W':
                            print((BRIGHT_GREEN + "%s의 %s!!!" + BRIGHT_END)% (playerName, W['스킬이름']))

                            if playerJob == '전사':
                                W['공격력'] = playerPower * 2
                                W['mp사용'] = 100


                            elif playerJob == '마법사':
                                W['공격력'] = playerPower + playerPower * 1.5
                                W['mp사용'] = 150

                            if playerMP < W['mp사용']:
                                print(BRIGHT_RED + "마나가 부족합니다." + BRIGHT_END)

                            else:
                                monsterHP -= W['공격력']
                                playerMP -= W['mp사용']

                                time.sleep(setTime)

                                print((BRIGHT_GREEN + "%s에게 %d의 데미지를 입혔습니다." + BRIGHT_END) % (monster['이름'], W['공격력']))

                        elif skill == 'E':
                            hp사용 = 0

                            print((BRIGHT_GREEN + "%s의 %s!!!" + BRIGHT_END )% (playerName, E['스킬이름']))

                            if playerJob == '전사':
                                playerPower = playerPower * 1.5
                                E['mp사용'] = 200
                                hp사용 = playerHP / 2


                            elif playerJob == '마법사':
                                E['공격력'] = monsterHP / 2
                                E['mp사용'] = 1000

                            if playerMP < W['mp사용']:
                                print(BRIGHT_RED + "마나가 부족합니다." + BRIGHT_END)

                            else:
                                monsterHP -= E['공격력']
                                playerMP -= E['mp사용']
                                playerHP -= hp사용

                                time.sleep(setTime)

                                print((BRIGHT_GREEN + "%s에게 %d의 데미지를 입혔습니다." + BRIGHT_END)% (monster['이름'], E['공격력']))
                            
                        else:
                            print("잘못 입력하셨습니다.")
                            continue

            # 아이템사용
            elif act == "I":
                i = 0

                type = ''

                print(BRIGHT_GREEN + "어떤 아이템을 사용하시겠습니까?" + BRIGHT_END)

                if len(listPlayerInventory) != 0:
                    for i in range(1, len(listPlayerInventory) + 1):

                        print("%d. %s" % (i, (listPlayerInventory[i - 1]['이름'])))
                    
                    while 1:
                        use = int(logicInput())

                        if use > 0:
                            type = listPlayerInventory[use - 1]['타입']

                            if type == 'hp':
                                playerHP += listPlayerInventory[use - 1]['회복']

                                if playerHP > playerMaxHP:
                                    playerHP = playerMaxHP
                                print(( BRIGHT_GREEN + "%s의 hp가 %d 회복되었습니다." + BRIGHT_END)% (playerName, listPlayerInventory[use - 1]['회복']))

                            elif type == 'mp':
                                playerMP += listPlayerInventory[use - 1]['회복']

                                if playerMP > playerMaxMP:
                                    playerMP = playerMaxMP
                                print((BRIGHT_GREEN + "%s의 mp가 %d 회복되었습니다." + BRIGHT_END)% (playerName, listPlayerInventory[use - 1]['회복']))
                            
                            elif type == 'all':
                                playerHP += listPlayerInventory[use - 1]['회복']
                                playerMP += listPlayerInventory[use - 1]['회복']

                                if playerHP > playerMaxHP or playerMP > playerMaxMP:
                                    print((BRIGHT_GREEN + "%s의 hp와 mp가 %d 회복되었습니다." + BRIGHT_END) % (playerName, listPlayerInventory[use - 1]['회복']))
                            
                            listPlayerInventory.pop(use - 1)
                            break
                    
                        else:
                            print("잘못 입력하셨습니다.")
                            continue
                
                else:
                    print(BRIGHT_RED + "사용할 아이템이 없습니다." + BRIGHT_END)
                    continue
        
        else:
            print("잘못 입력하셨습니다.")
            continue

        if monsterHP <= 0:
            if monster['이름'] in dictionaryPlayerQuestMonster.keys():
                dictionaryPlayerQuestMonster[monster['이름']] += 1
            if monster['타입'] == '보스':
                dungeonprogress += 1
                break

            else:
                if monster['이름'] == '좀비':
                    break
                else:
                    break


        time.sleep(setTime)

        if monster['타입'] == '보스':
            situation = rd.randint(1,101)
            if situation <= 80:
                print((BRIGHT_RED + "%s의 공격!!!" + BRIGHT_END) % monster['이름'])

                playerHP -= monster['공격력']

                time.sleep(setTime)

                print((BRIGHT_RED + "%s에게 %d데미지를 입혔습니다." + BRIGHT_END) % (playerName, monster['공격력']))

                time.sleep(setTime)

                print("===============================")
            
            elif situation <= 90:
                print((BRIGHT_RED + "%s의 체력회복!" + BRIGHT_END )% monster['이름'])
                time.sleep(setTime)
                heal = monster['체력'] / 10
                print((BRIGHT_RED + "%s가 %d만큼 체력을 회복하였습니다." + BRIGHT_END)% (monster['이름'], heal))
                print("===============================")

                monsterHP += heal

                if monsterHP >= monster['체력']:
                    monsterHP = monster['체력']

                time.sleep(setTime)
            
            else:
                print((BRIGHT_RED + "%s의 스킬사용!!!" + BRIGHT_END)% monster['이름'])

                playerHP -= monster['공격력'] * 2

                time.sleep(setTime)

                print((BRIGHT_RED + "%s에게 %d데미지를 입혔습니다." + BRIGHT_END) % (playerName, monster['공격력'] * 2))

                time.sleep(setTime)
                print("===============================")


        else:
            print((BRIGHT_RED + "%s의 공격!!!" + BRIGHT_END) % monster['이름'])

            playerHP -= monster['공격력']

            time.sleep(setTime)

            print((BRIGHT_RED + "%s에게 %d의 데미지를 입혔습니다." + BRIGHT_END) % (playerName, monster['공격력']))

            time.sleep(setTime)

            if playerHP <= 0:
                print(BRIGHT_RED + "눈 앞이 깜깜해졌다." + BRIGHT_END)
                break

            print("===============================")

    time.sleep(setTime)

    if playerHP <= 0:
        lostGold = playerGold / 10
        print((BRIGHT_RED + "%d원을 잃었다!" + BRIGHT_END) % lostGold )
        playerGold -= lostGold
        print("===============================")
        print("[현재 위치: %s]" % location)
        print("1. 소모품 상점으로 이동하기")
        print("2. 장비 상점으로 이동하기")
        print("3. 던전으로 이동하기")
        print("4. 모험가 길드로 이동하기")
        print("[I: 아이템창, E: 장비창, S: 스텟창, Q: 퀘스트창]")
        return 0

    print("===============================")
    print((BRIGHT_GREEN + "%s를 처치하였다!" + BRIGHT_END) % monster['이름'])
    print((BRIGHT_GREEN + "%d골드를 얻었습니다." + BRIGHT_END) % monster["골드"])

    playerGold += monster["골드"]

    time.sleep(setTime)

    return 0       

# 엔딩
def ending():
    str = ('%s 가 공허의 괴물들과 마녀를 처치한 후...' %(playerName))
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    print()
    time.sleep(1)
    str = '지구에 문명은 찾아볼 수 없을 정도로 황폐해졌고,' 
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    print()
    time.sleep(1)
    str = '많은 사람이 없어졌고, 소중한 공간 또한 사라졌다.' 
    for run in range(1,2):
        for i in str:
            print(i, end = '')
            time.sleep(0.1)
    print()
    return 0
    
# 로직 인풋
def logicInput():
    print("===============================")
    logic = input("입력: ")
    print("===============================")

    if logic.isdigit() == True:
        return logic
    else:
        return logic.upper()

# 로직 판단 함수
def systemJudgmentLogic(logic):
    # 게임 시작 화면 관련
    if page == 'start':
        if logic == '1':
            return 0

        elif logic == '2':
            explanationManu()

        elif logic == '3':
            exit()
    
    # 직업 생성 관련
    elif page == 'generateJob':
        if logic == '1':
            generateJob('전사')
            return 0
        
        elif logic == '2':
            generateJob('마법사')
            return 0
    
    # 닉네임 생성 관련
    elif page == 'generateName':
        if len(logic) >= 1 and len(logic) <= 10:
            generateName(logic)
            return 0

    # 스텟 생성 관련
    elif page == 'generateStat':
        global queue # 전역변수 queue

        if logic == 'R':
            generateStatRandom()
            queue += 1
            
        elif logic == "Y" and queue > 0:
            return 0

    # 스토리 출력 관련
    elif page == 'explanationStory':
        if logic == 'N':
            explanationStory()
            return 0
        elif logic == 'Y':
            return 0
    
    # 튜토리얼 출력 관련
    elif page == 'tutorial':
        if logic == 'Y':
            tutorial()
            return 0

        elif logic == 'N':
            return 0
    
    # 게임중 관련
    elif page == 'inGame':
        if logic == 'I':
            infoInventory()

        elif logic == 'E':
            infoEquipment()

        elif logic == 'Q':
            infoQuest()
        
        elif logic == 'S':
            infoStat()
        
        elif logic == 'K':
            infoSkill()

        # '고대시대에 존재했던 마을' 관련 로직
        if location == '고대시대에 존재했던 마을':
            if logic == '1':
                expendableStore()
            
            elif logic == '2':
                equipmentStore()
            
            elif logic == '3':
                dungeon()
            
            elif logic == '4':
                guild()
            
            elif logic == '5':
                travel()

        # secondTown 관련 로직
        elif location == 'secondTown':
            if logic == '1':
                expendableStore()
            
            elif logic == '2':
                equipmentStore()
            
            elif logic == '3':
                dungeon()
            
            elif logic == '4':
                guild()
            
            elif logic == '5':
                travel()

    # default 값
    else:
        print("다시 입력해주세요.")

# 프린트
def prints():
    print("[현재 위치: %s]" % location)
    print("1. 소모품 상점으로 이동하기")
    print("2. 장비 상점으로 이동하기")
    print("3. 던전으로 이동하기")
    print("4. 모험가 길드로 이동하기")
    print("[I: 아이템창, E: 장비창, S: 스텟창, Q: 퀘스트창]")

# < 프로그램 작동부 >
# 게임 스타트 화면
page = 'start'
while 1:
    print(bannerMain)
    print(bannerStart)
    print(bannerHelp)
    print(bannerExit)

    if systemJudgmentLogic(logicInput()) == 0:
        break

# 직업 선택
page = 'generateJob'
while 1:
    time.sleep(1)
    print(BRIGHT_GREEN + "[직업을 선택해주세요]" + BRIGHT_END)
    time.sleep(1)
    print("1. 전사")
    time.sleep(0.5)
    print("2. 마법사")
    time.sleep(1)

    if systemJudgmentLogic(logicInput()) == 0:
        time.sleep(1)
        print("[직업 선택이 완료되었습니다.]")
        break

# 닉네임 설정
page = 'generateName'
while 1:
    time.sleep(1)
    print("===============================")
    print(BRIGHT_GREEN + "[닉네임을 입력하세요(1 ~ 10자 사이 영문)]" + BRIGHT_END)
    time.sleep(1)

    if systemJudgmentLogic(logicInput()) == 0:
        time.sleep(1)
        print("[닉네임 설정이 완료되었습니다.]")
        break

# 스텟 설정
page = 'generateStat'
while 1:
    time.sleep(1)
    print("===============================")
    print(BRIGHT_GREEN + "[지금부터 캐릭터 스텟을 생성합니다.]" + BRIGHT_END)
    time.sleep(2)
    print("hp와 mp는 0~4% 사이, defense와 power는 0~4 사이의 랜덤한 값으로 증가합니다.")
    time.sleep(1)
    print("현재 증가한 스텟을 보고 마음에 들면 Y를 입력, 마음에 들지 않으면 R을 입력해주시길 바랍니다.")
    time.sleep(1)
    print("시작을 원하시면 R을 입력해주시길 바랍니다.")
    time.sleep(1)

    if systemJudgmentLogic(logicInput()) == 0:
        break

# 캐릭터 생성 완료
if playerJob == '전사':
    listPlayerSkill.append(listWarriorSkill[0])

elif playerJob == '마법사':
    listPlayerSkill.append(listWizzardSkill[0])

listPlayerInventory.append(listExpendableItem[0])
time.sleep(1.5)
print((BRIGHT_GREEN + "[플레이어의 직업은 '%s'입니다.]" + BRIGHT_END) % playerJob)
time.sleep(1.5)
print((BRIGHT_GREEN + "[플레이어의 닉네임은 '%s'입니다.]" + BRIGHT_END) % playerName)
time.sleep(1.5)
print((BRIGHT_GREEN + "[플레이어의 스텟은 'hp: %d, mp: %d, defense: %d, power: %d'입니다.]" + BRIGHT_END) % (dictionaryPlayerStat['hp'], dictionaryPlayerStat['mp'], dictionaryPlayerStat['defense'], dictionaryPlayerStat['power']))
time.sleep(1.5)
print("===============================")
time.sleep(2)
print("[캐릭터 생성이 완료되었습니다.]")
time.sleep(2)

# 스토리 설명
page = 'explanationStory'
while 1:
    print("===============================")
    print(BRIGHT_GREEN + "[스토리를 스킵하시겠습니까?(Y / N)]" + BRIGHT_END)

    if systemJudgmentLogic(logicInput()) == 0:
        break

# 튜토리얼
page = 'tutorial'
while 1:
    print(BRIGHT_GREEN + "[튜토리얼을 진행하시겠습니까?(Y / N)]" + BRIGHT_END)

    if systemJudgmentLogic(logicInput()) == 0:
        break

# inGame
page = 'inGame'
location = '고대시대에 존재했던 마을'

str = '<첫 의뢰를 받기 위해 모험가 길드로 이동해보세요!>'
for run in range(1,2):
    for i in str:
        print(BRIGHT_GREEN + i + BRIGHT_END, end = '')
        time.sleep(0.1)
print()
    
while 1:
    if page == 'inGame' and location == '고대시대에 존재했던 마을':
        print("===============================")
        print("[현재 위치: %s]" % location)
        print("1. 소모품 상점으로 이동하기")
        print("2. 장비 상점으로 이동하기")
        print("3. 던전으로 이동하기")
        print("4. 모험가 길드로 이동하기")
        print("[I: 아이템창, E: 장비창, S: 스텟창, Q: 퀘스트창]")
    
    systemJudgmentLogic(logicInput())

    if systemJudgmentLogic(logicInput()) == 1:
        break

# 프로그램 종료
os.system("pause")
