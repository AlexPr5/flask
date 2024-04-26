
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app )                   #Сам сайт


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable =False)
    subtitle = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)  #Модули     

    def __repr__(self):
                return f'<Card {self.id}>'

#Запуск страницы с контентом
@app.route('/')
def index():
    #Отображение объектов из БД
    #Задание №2. Отоброзить объекты из БД в index.html
    cards = Card.query.order_by(Card.id).all()
    
    return render_template('index.html', cards = cards)

#Запуск страницы c картой
@app.route('/card/<int:id>')
def card(id):
    #Задание №2. Отоброзить нужную карточку по id
    card = Card.query.get(id)

    return render_template('card.html', card=card)

#Запуск страницы c созданием карты
@app.route('/create')
def create():
    return render_template('create_card.html')

#Форма карты
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']            #Если все данные из этой таблицы равны тому что происходит сейчас

        #запись данных в БД
        card = Card(title=title, subtitle=subtitle, text=text)
        db.session.add(card)
        db.session.commit()     

        return redirect('/')                    #То выводит вот это
    else:
        return render_template('create_card.html')      #В сотальных случаях выводит вот это


if __name__ == "__main__":          #Если имя "main"
    app.run(host='0.0.0.0', port=80)
   # app.run(debug=True)