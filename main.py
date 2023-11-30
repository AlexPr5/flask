from flask import Flask
import random


app = Flask(__name__)

#ГЛАВНОЕ - МЕНЮ ПРИЛОЖЕНИЙ
@app.route("/")
def hello_world():
    return '<h1>My apps:</h1>\
        <p>\
            <img width="25" src="data:image/png;base64,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">\
            <a href="/facts">Интересные факты о технологических зависимостях</a></p>\
        <p>\
            <img width="25" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMwAAADACAMAAAB/Pny7AAAAbFBMVEUAAAD////u7u7t7e3s7Oz8/Pz29vbx8fH5+fmKiopiYmJra2vm5ubp6enf399lZWWampqrq6vS0tIpKSlzc3NISEi2trbExMTY2NgWFhZZWVmSkpI0NDQ9PT2+vr4QEBAdHR1PT099fX2ioqLSKH8hAAASuklEQVR4nO1d6ZqrqhINKkMStR0SNZMx8f3f8YKAIyAas7vv9536c862tawVoFgFVbgDQpAjBA4vuFheIC6/gttHPH7B+yM6nN1IidspccdKPHFhzpDf0uHsoBCEhUwuEHGBOOM7xAXnj+jAO3krkn+aPDu+Y3IB/hUdO9FCHpKN5vBm9Yj4N8SineUd0BldAN4f0TEFg0WnNSgRojfkl3T8B+Y/MP+BWQfGXaJE44lMOpwNdMx7MySFCNn4AqQTN6ETn7j4pbdw6eiMx6WjEeJCj0aIO8aPeHodGHtFkkW3KM6TkKzTYW/HmJttSxIhzm+PnZBrlLRd498QTcdA8BaDgckt3fXkUReEq10CxtqOr4Lxo/NuJNc6aAby/x2Y7PocY9ntqp8cEm8+BPhbYJJXOoXCJD0W1O3+34ChvzvaK1qlbZ0bHU7fBeNy6Snh0nOJowvyDm+owyEk1iPhUo5f640vrLDD3Ull3cw7ugCxeLg38w4vAG/wCMon434q1wQhx9PqWGfHB9xMHVihwtTDOrncQoxMwdkKO7YmmkWkGfdTedQ+wn+VNdNxH8RXWyhMDlk7VP4WGDruney4BAqV6p3Dno6/Aob+tXhb97BOHvvwN8A4BjC0h/n7x7zpCnmeI7wIjMGOnaTP3RKPuNApGd0BnfEjHiHZaxWUBs41YTo2sGMSnKGlFxCClLushtLIMQQf27FFcOZi5J0+g8LkPX7tbwRnGDv15XMsu905x5/Y0chnRJO2SmnBXezkkKO1dmwAhiCcvLeCQqXaF1C+9p+DAcXtPmfg/XXcR0ze19l7aV+L/NYD/1swqJ7zYYcoywsfU3dDPW2RxBYU9BAj6H4OZmHzwuzHbNoxTnyHAqEuwuE6IE7maWh6zPmrvxGcdS4RyaCI/SM8mc26Jew55Dbeu+dWk8Ns49z3AcCepR39C66kMx1JEDTCGS+t9u6gUbEZyj6ArEFUOpCFy3jExMqO0QU9N9PvWAESVyZT0hqL9yh1QJsp9pHL7mXaObMGo2WrpDDGLOk7aLfw1DoCC7e2251Cgo12bAAGhnuTCZdTMd+6luyHBaJfBePHxsHyqmFPB26H6NCQ2bUbIY+MwvlaN/Myoy+6nMJWB+WfyAmTPC/QxJDMEgzta6WD4NSOj8G4iORvI6VM65bH0g4Gi/j980jT1z5Do8CqtgazS/fJGIwpOJusmznca/eDIvZnmOzNlPJVtlMDwKDYvyTy9Ibkmpe3ZMwItZHfs2OwkOaMLoCd3b4UQNFMVPxTQCifgKDuA08z0AuoCFgWXz9fdNbBKsMmUdqYzrjjOIJTkfIxE7ScglaHB8Pj8O436qiIS/JqERjKps8JCzcmdGZEeKyIJmXHhzmGeIJSh+uAyfLsu2eIB25WK54DedLJC23Amh2Eo9m3n3o6YD723s8b6RkCV4VAl7oLo1aDwSibXw179XSQctIh7xno/6rzVFMp5+RTMBjXlcWLrjyApzpQMvV556LXMhivBLO7i9XP9WASuxc93wwOcrGvIG4H0u/vZME0M5Szbw1m4s0aMDfbN9HpDUCXqAbECfQ3inAQWTFNheRCR+uZxmC02YP8gpFWDuV1K0CuuH6pwSCdj4B4uT9rpBxmAE5Mn0lrVFqnlXOsIgn3BPQzEAGKZwJunTwLNJPWSANlFiyPt98kfceLuEelungvGl7VvIe+pTwo77KQyHHG24CDC/NE01vQ0dRS1R1ZBcVRQLkmSx1BjbFQIsEIWcKa83V7FZ38SDAA7y8SIPUJ/pJWv4YiFv8MDOXsa90Pl2fEHD8mWEZl6Y1F1h4Gie3oOWes/28AhgaMwZpNsU6qm09DNdnC6Y8vspvouCxf1fzz9z3ZLjijfyyPH8F5lbnoU+mp7AxxXYDr1wwhv78TYcfQdqvgzJ0GZ55D+8iijWSNPH8yvi7SS0gIjZPo81h2doyCs0lSAzIIm7e7/w9n15bn5HKMQ0SG7yAgqA0e5hCHvTCRTi4mew3Lsx70sziBLUlkyRef7Svdc5n40q4WACeWzlr1QByyeI4vz9I2zLKgy53p7ZzJ5dn2yphoYlhe0/T8lswbEIcO4qU7/QO5XKOAO6WWVxnH4p6ldaJ2itq/0vRarmLNMOTc5H4LBBiPlXbkH7np5zVDpDPENy2/XxPEu0wTvgZiL+gcwhVgQBvJ3PkQ5L8IWcI9VXAOIcAeN6Q2ecgayf7fuHA5riifWAGG9ObnewK6OAI4H+4uH3xADYGm5ffLvjOV9rCk1x2O0tBFwdlgeLx92Pp1APLrZ54gwiT50f+5OlBP0f6oyB8ESQcbMBNvNnzbMw4QduQmD511VsYkXB4n/ePNuOrsCEbRz8HB2s0mfXA2dlyvzCNtUAT826f8UyOvyGOZ6o0d9Fcrx3P1QRq6JDjDEy98eVP/IoMiQvLTZ/xTKfd9QYeTsAPifEoKDwjY15xJCuQoppRH86qGJNJ+gEtDv18lz2MuWRSgNLtQZUodDFUaUzCOHgzbgXFbLk6Ar4yTV8u19FELBgSRkj4dVrBmDRg6i7Ph6QolMFyx2KqRNAoR7gh+qXExW4JhGfAF94bNIzNbnPbCNzGlHb42gtoWDJV3wDbH5COWC4VGeYT8xdwOx5DLsTmYXRrT0LF9xJgsbyNsB8dt7UClyU1agOn6qgQzdc0DeeXtmislJ3MJG0a5M+4iZ3GIZpI4TN5Muw01A4Z1ckS5Bn+GMpzjSoZTnRIA5XsJCucWhA/YouZMxEA6OqOQR1Rg7HqiKGFdXP38iTHBbWFDOO/rD3wp0PWWBGfzYNh6bEBdkEwbD5cvSZ1jn09bjQ7H5veg3EyMgw6MMP0zMLvqWCLS5sDDhYmB6a2AiPd8j602viuLh9aBsYuQ76ekWyQgbm7f154nSvXk/oQDwrddu36vZRo4727cYRTEln3tUeLWEBcAaxL+zZZp4GSdDgrHJq6+iKgY8TqC0j6e+G7LMGky4IUODOcZzinoDKGz1JJXSTCGnbN+DoO4sGxVaR92OiAo7wZOcDmz/TwZWBGrlpyCcXoHgkgwk+VZEZQqGUBlmOer2m+9mgOJNkv4ea7bpVUPQ9d2jLVgDMuzApQdN7vW79NZC+haypZna0mJOhA930IgeBV1FytWFSfcbC2YI6ZzSfbWrjnvEyJ1uASVp2l+wz6RhrgOQsmKNbjNWPMPn6iT+FSp33S/tWmNLib+ONmOTrFtF0GkWLUmsi0YiBEKcl0y8Kum98i3QL+/JHXN/C4TjviGTYXq9a7rtxrqxmBoD8EI67rI5SeXi58eAdAv6/318bju6zzoVTLC/EfLstM68R2CPDWB3hpM4xgxKTSBR3pKuO/nu2+ERvaszgb3gtNCH/9cS56XzdaQVBvSJjC6Wi/XAEbWHqFIZ9GeQLdXL9Z4hN5b9ElfaQY7O3CgysQx1Jzp0xqVYEj/DgJC7VyfdRHXMPSjM6ruGTpXQdB/AioSbWlwNrZ0unM2qfVScIwf3xnUernE04b/V+qmp/ViGCVa/E+WSjy0Q7FWQoOzFTVnqnnGpWO4W8fw6CBA2iqSyy1EkkZ1O1g37bh/NMl+QzuS6d3riKZieF9zKknhdkoo3cu0s8U552haMNBQXX9MFHYUUxaxGWu+3KsqfdBJIPdbJZgkWs/0KNEAjAHLzVfZ8U0wrdyPddAqAfp9znvSbEkKMKG2DatIbcdmYMwU8HltF+5cQ3b/tam04GCIVmNadgNxUC6mdAAWYCY1Z3MRU/p2iFiMgPrCixvwJBhtTtY56Y47gdIQgzezADPeBpzPcj05zZIVI2P6ZRmEpWvWOfFXgbrTTbAPmrySxg7lPCPWzVTbgNrgzLjWLEQsZXguTrTDoQa8YlzbMIeQ62DbV1HVZnxTO7BqX3uz4GwsVczB0E6h7Wgp4BlJunqGoyN0IJEP/sylHbiojGCEbASGUgJuiIu0ixhPpwGDHXUvq2rRusgXNPxSSjuU59d8D8wuEy3joFo3JOIGjK7pnsIpd79GCwZj1bT0RTC1BEMUefNc9g0YoFndvwgw3XxaJWLMECUj/SKYGxJgsLaatAHjAV0sx8HkHQl7iCI8TJQ/zzfBEAHGhboSCDMY3s36GbpiEDmaqXiz4GwqjTvjCnQpwxYt01+drcT8gRw1SbIMzjDL25AhzzTdRCVHn0YofCsLhJpBswdMqb5lIBgMtxvgdugeOODGUIS74Ez8GxuqNCwWgPeYPSZmb6ihDHvQMAAdmNvobBQoqoB9DRe3ojPyHutdAJYiyLe7xROaNLQZMJE/+BFyvmODta//wi5A9cix1PIRmOo28NlvIqzQVlRtD+Yc95R8BOYy6E33oAHjar3JF+IZXsw2BqN5wAxmKDFp7MAGFr41mDQDCjC+Zrl1AZiTx+3AhhLEBcGZawOG08sxGF3wbA+GNTi1g7JWQ2679Gbu5PhKfc2ZaczsR48090Odtc08A23ARFKpqU7IIq3R6dIa5Sn7+pbZk8EjgDY8hpluVWMPIKFh8TyYa8EKPak+3fTLwci0RmmpszKtUZqHZPIcF8YoSm0vN9OZTqoY8to3w4rCTpEI9CHRjDji7hHgG1IzRAgwC+aARPKcZ8yf2Zo1P7LGg8pHSPg25ZtZtkxasiR/ZodvvG/7EOAnwTJ5Ds8lJFiCOUBpx78GQ/lhwdePgtnCAEswWVOw8CtgmgNK2e3zxc92YB5NFabrQlBot7BmwUxrzmTh0Gw8c8wQ8OajHjswb7ZyRmfXIJ4pBjOtm2mP2TDMM8d91fw3fee+DRiWrjgHJmaHhkBUGioeBBg82eOzqDnTM4AIleLnu7/nU87t6ExDXQuLnLOD6yyvOTNwsxuArpjYnvNJwHZg6ABE86fy7VYWA4FIu2F3s3Nji8BAkD3ED2OsEb5EZA0YPQ2/8Rssa+nswLQ5Z+fQM92XZmtqzqBycbQPhuI9W6SaLwnOnq8SwNB0xxmtOhBEf6aSAIMw9IVf2wbM8xw5wEVGMKd1BxyiQtfPJBjPJYGNa7YE87g1eQBGMGnYnT4/9Wb6mjMMdFPxDchHkEV6pW1wdsoJYEqNYOirNUeXqIOz9lZAdMt6RNZ6Ad8GjE1wds18wu0wcbMX47djS+eDsyaJR7PXvee7++wRKzA2dCZh+35zRDMtyOBAEKe1o5GZww3Umy43rmdTML44T8wE5p4Q95OTGpS7e8ewab9NwYTImQNzLki/IVYcO4FVXiCNKaFZ1M1mw+Z5MDen690rwVDeoiqeqEqIN20Z1wymeouTBD48EISA/KqA81PAbbuZK/wOmh6pVF3zJUe1TGrO+t8oAyg7K1hn5Fu65gVgMJkeofo8x7BXDDexVFFzZhICQtVpjefMtYo0mYo5MAE765FAP54mdkd01rcy03QgiEzX5/9O9lOS/DxZFFbZ0ZmGnDjTaun7PkfI65/XLOjMspqz8QnWNKSd2lBV24FR1WmxMjBeGL7tGecQ+as+MmELRlFj/oiDrx3YjlGw4kA/OzCOYlDWPlHasQmYpmpp8RkAdmAekzCP+/6NwDhKJRjoE5M/ATOW9tjMb36Emq05xotKRdaAuUfjpM11H6GehDyTDydD4CnctAGMg+12zloobx8gCzsmwZkurbH3fbHRKigr5IGJrhxIBcZus0kKq9y2tMM2rdF4UDpLp8zs180WgTlmyNqO4YXVH6CiXdizPO9sEZhzFCyyg8nHYNi/kd0X2haAqWQF3r8Gwy4gmzJzezDHxEG/BKZRYj7vYhGYNHMR/uWPtsE5hmMJ5gb7R7WsA6N1zT0lMy4RmimBFZhDwF/8iR22R+kbLxCQHAyngTQ7Z9q0RiaXF42KP7djEpx52uBMHxR57Csu+vPOZunMuUZw/KXTNXaYgjPRZy2/QRtOv2tsB+ZB3TF2Dd+gtbZjyw/qJpoKYSOY6p032R5/7uvASF0PbwJzLD3SHdXyl8AA4KsqA/VgHpnfrtP/OTBsb2VqsxYM+y4o+dJ3mzcA4zkYFWM2rQFzLIhSx3o7TNuAsrRr5COn228Dt0rZ1SjNSQnmnhG9jpV2uJt86TQY3zE45KNhAMEATFojgM06Vn3pVLTQZ9+gHesAXu8UvJpvaXS5iuzrYbJr6HWs+QatNRi7j1CLX5XA8iDgXPxGB/IF40kPpZWO3/0IdV8HO/lALEPvuQ6x2/S8xtBSx58B0xxuUtTvn5+mjovpQDj6uZ7qcIGOPwOG/R0FIT/PpPn8BJ2ECnm8yW+DWeIAxJkGQx3sVBCyVMcvfIT6j+iYrGhOVhLRZCVxstb4V3TMfBnIao13TEV+S8fGRPN3dfwH5j8wvwzG2cCQf6pj7jtnKi8yqfVa4Ym+osNi52zFHPFbOlZ9hHp0AfwVHea0Rv7MCqL5Ozr+B4hginD8Q8TgAAAAAElFTkSuQmCC">\
            <a href="/random">Показать рандомное число</a></p>\
        <p>\
            <img width="25" src="https://i.gifer.com/origin/5b/5b28fde489ffaea3bda9926fb90a77d1_w200.gif">\
            <a href="/moneta">Играть в "Орёл - Решка"</a></p>\
        <p>\
            <img width="25" src="https://pictures.pibig.info/uploads/posts/2023-04/1682146554_pictures-pibig-info-p-chernii-kot-risunok-siluet-instagram-44.jpg">\
            <a href="/cats">Случайная картинка с котиком</a></p>\
        '
###конец

#ПРИЛОЖЕНИЕ РАНДОМНОГО ЧИСЛА
@app.route("/random")
def rendom():
    return f'<h1>Показать рандомное число</h1>{random.randint(1, 100)}</p><br>\
        <a href="/random">Еще раз</a> | \
        <a href="/">Назад</a>'
###конец

#ПРИЛОЖЕНИЕРАНДОМНЫХ ФАКТОВ ИЗ СПИСКА
@app.route("/facts")
def facts():
    sp=["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
        "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.", 
        "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.", 
        "Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.",
        "Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.", 
        "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента."
    ]
    return f'<h1>Интересный факт</h1><p>{random.choice(sp)}</p>\
        <a href="/facts">Еще факт</a> | \
        <a href="/">Назад</a>'
###конец

# ПРИЛОЖЕНИЕ ОРЕЛ И РЕШКА
@app.route("/moneta")
def moneta():
    t = random.randint(1, 2)
    if t == 1:
        return '<p>Орёл</p>\
        <a href="/moneta">Подкинуть еще раз</a> | \
        <a href="/">Назад</a>'
    else:
        return '<p>Решка</p>\
        <a href="/moneta">Подкинуть еще раз</a> | \
        <a href="/">Назад</a>'
###конец

#СЛУЧАЙНАЯ КАРТИНКА КОТИКА
@app.route("/cats")
def cats():
    catimg=[\
        "https://funik.ru/wp-content/uploads/2018/10/17478da42271207e1d86.jpg",\
        "https://w.forfun.com/fetch/96/96e20d242c141a43cfb6295be5aa3e3e.jpeg",\
        "https://gas-kvas.com/grafic/uploads/posts/2023-10/1696422772_gas-kvas-com-p-kartinki-milie-kotyat-1.jpg",\
        "https://w.forfun.com/fetch/b7/b78fea5ac7f4eca30bb04afe26a90d52.jpeg",\
    ]
    return f'<h1>Котики</h1>\
        <img width="300" src="{random.choice(catimg)}"><br><br>\
        <a href="/cats">Еще картинка</a> | \
        <a href="/">Назад</a>'
###конец


app.run(debug=True)
