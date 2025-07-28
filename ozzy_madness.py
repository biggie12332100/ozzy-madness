import random
import time
import webbrowser
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

def crazy_text_effect(text, font_size=30): 
    colors = ["red", "green", "blue", "purple", 
    "orange"] img = Image.new("RGB", (800, 200), 
    "black") draw = ImageDraw.Draw(img)
    
    try: font = ImageFont.truetype("arial.ttf", 
        font_size)
    except: font = ImageFont.load_default()
    
    x = 10 for char in text: color = 
        random.choice(colors) draw.text((x, 50), 
        char, fill=color, font=font) x += 
        font_size + random.randint(-5, 5)
    
    img.show() def play_ozzy_song(): songs = [ 
        "https://www.youtube.com/watch?v=ukgnU5fA9W4", 
        # Crazy Train
        "https://www.youtube.com/watch?v=5s7_WbiR79E", 
        # Mr. Crowley
        "https://www.youtube.com/watch?v=gi3g9z8q__8" 
        # Paranoid
    ] webbrowser.open(random.choice(songs)) def 
ozzy_facts():
    facts = [ "Ozzy однажды откусил голову 
        летучей мыши на сцене! 🦇", "Ozzy выпил 
        целую бутылку виски за 30 секунд. И 
        выжил. 🥃", "Ozzy пережил передозировку, 
        падение с высоты и укус летучей мыши. 
        Бессмертен? 💀", "Ozzy как-то сказал: 'Я 
        не знаю, как я ещё жив.' 🤘"
    ] print(random.choice(facts)) def main(): 
    print("🔥 Добро пожаловать в ОЗЗИ-ГЕНЕРАТОР 
    БЕЗУМИЯ! 🔥") time.sleep(1)
    
    # Показываем Ozzy в ASCII (грубое 
    # приближение)
    print(''' ,-~~-.___. / ()=(() \\ ( ( 0 \._\, 
           ,----'
      ##XXXxxxxxxx
             / ---'~; / /~|- _( / / / \_/ / / / 
        \ /
         |      /
         |     |
    ''') ozzy_urls = [ 
        "https://i.imgur.com/Jz6Q2bU.jpg", # 
        Ozzy с пауками 
        "https://i.imgur.com/5JZ3Q6h.jpg", # 
        Ozzy в молодости 
        "https://i.imgur.com/jkZvW9x.jpg" # Ozzy 
        кусает голубя
    ]
    
    try: img = 
        download_image(random.choice(ozzy_urls)) 
        img.show()
    except: print("Не удалось загрузить Ozzy, но 
        он всё равно наблюдает за тобой! 👀")
    
    crazy_text_effect("SHARON!!! I'M COMIN' 
    HOME!") time.sleep(2)
    
    ozzy_facts() time.sleep(1)
    
    print("\nЗапускаю Crazy Train... 🚂") 
    play_ozzy_song()
    
    print("\nГотово! Теперь ты настоящий Prince 
    of Darkness! 👑")
if __name__ == "__main__":
    main()
