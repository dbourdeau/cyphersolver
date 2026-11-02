"""Russian corpus for language scoring: ru.wikipedia plain extracts on early Soviet diplomacy and politics."""
import json,os,time,urllib.parse,urllib.request
HERE=os.path.dirname(os.path.abspath(__file__))
T="""Рапалльский договор (1922)|Генуэзская конференция|Народный комиссариат иностранных дел РСФСР|Чичерин, Георгий Васильевич|Копп, Виктор Леонтьевич|Карахан, Лев Михайлович|Красин, Леонид Борисович|Литвинов, Максим Максимович|Иоффе, Адольф Абрамович|Крестинский, Николай Николаевич|Советско-польская война|Рижский мирный договор|Кронштадтское восстание|Новая экономическая политика|Голод в Поволжье (1921—1922)|Гражданская война в России|Брестский мир|Советско-германские отношения|Англо-советское торговое соглашение|Третий Интернационал|Советско-турецкие отношения|Московский договор (1921)|Советско-персидский договор (1921)|Советско-афганский договор (1921)|Врангель, Пётр Николаевич|Ленин, Владимир Ильич|Троцкий, Лев Давидович|Радек, Карл Бернгардович|Антоновское восстание|Мартовское восстание в Германии|Бриан, Аристид|Ллойд Джордж, Дэвид|Версальский договор|Репарации|Веймарская республика|Русская армия Врангеля|Высший совет народного хозяйства|Внешняя торговля|Концессия|Дипломатия|Посольство|Правительство""".split('|')
done=open(os.path.join(HERE,"ru_corpus.txt"),encoding="utf-8").read() if os.path.exists(os.path.join(HERE,"ru_corpus.txt")) else ""
out=open(os.path.join(HERE,"ru_corpus.txt"),"a",encoding="utf-8");n=0
for t in T[10:]:
    u='https://ru.wikipedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','format':'json','prop':'extracts','explaintext':1,'redirects':1,'titles':t})
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'cyphersolver-corpus/1.0 (research)'}),timeout=60))
        for p in d['query']['pages'].values():
            x=p.get('extract','');out.write(x+'\n');n+=len(x)
    except Exception as e: print(t,e)
    time.sleep(8);out.flush()
print(n)
