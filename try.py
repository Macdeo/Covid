from flask import Flask,url_for,render_template,request,redirect,url_for
import datetime
import tkinter as tk
from tkinter import ttk
import datetime
import tkinter.messagebox as messagebox
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from tkcalendar import Calendar


app = Flask(__name__)

DEPARTMENTS = {
    '01': 'Ain',
    '02': 'Aisne',
    '03': 'Allier',
    '04': 'Alpes-de-Haute-Provence',
    '05': 'Hautes-Alpes',
    '06': 'Alpes-Maritimes',
    '07': 'Ardèche',
    '08': 'Ardennes',
    '09': 'Ariège',
    '10': 'Aube',
    '11': 'Aude',
    '12': 'Aveyron',
    '13': 'Bouches-du-Rhône',
    '14': 'Calvados',
    '15': 'Cantal',
    '16': 'Charente',
    '17': 'Charente-Maritime',
    '18': 'Cher',
    '19': 'Corrèze',
    '2A': 'Corse-du-Sud',
    '2B': 'Haute-Corse',
    '21': 'Côte-d\'Or',
    '22': 'Côtes-d\'Armor',
    '23': 'Creuse',
    '24': 'Dordogne',
    '25': 'Doubs',
    '26': 'Drôme',
    '27': 'Eure',
    '28': 'Eure-et-Loir',
    '29': 'Finistère',
    '30': 'Gard',
    '31': 'Haute-Garonne',
    '32': 'Gers',
    '33': 'Gironde',
    '34': 'Hérault',
    '35': 'Ille-et-Vilaine',
    '36': 'Indre',
    '37': 'Indre-et-Loire',
    '38': 'Isère',
    '39': 'Jura',
    '40': 'Landes',
    '41': 'Loir-et-Cher',
    '42': 'Loire',
    '43': 'Haute-Loire',
    '44': 'Loire-Atlantique',
    '45': 'Loiret',
    '46': 'Lot',
    '47': 'Lot-et-Garonne',
    '48': 'Lozère',
    '49': 'Maine-et-Loire',
    '50': 'Manche',
    '51': 'Marne',
    '52': 'Haute-Marne',
    '53': 'Mayenne',
    '54': 'Meurthe-et-Moselle',
    '55': 'Meuse',
    '56': 'Morbihan',
    '57': 'Moselle',
    '58': 'Nièvre',
    '59': 'Nord',
    '60': 'Oise',
    '61': 'Orne',
    '62': 'Pas-de-Calais',
    '63': 'Puy-de-Dôme',
    '64': 'Pyrénées-Atlantiques',
    '65': 'Hautes-Pyrénées',
    '66': 'Pyrénées-Orientales',
    '67': 'Bas-Rhin',
    '68': 'Haut-Rhin',
    '69': 'Rhône',
    '70': 'Haute-Saône',
    '71': 'Saône-et-Loire',
    '72': 'Sarthe',
    '73': 'Savoie',
    '74': 'Haute-Savoie',
    '75': 'Paris',
    '76': 'Seine-Maritime',
    '77': 'Seine-et-Marne',
    '78': 'Yvelines',
    '79': 'Deux-Sèvres',
    '80': 'Somme',
    '81': 'Tarn',
    '82': 'Tarn-et-Garonne',
    '83': 'Var',
    '84': 'Vaucluse',
    '85': 'Vendée',
    '86': 'Vienne',
    '87': 'Haute-Vienne',
    '88': 'Vosges',
    '89': 'Yonne',
    '90': 'Territoire de Belfort',
    '91': 'Essonne',
    '92': 'Hauts-de-Seine',
    '93': 'Seine-Saint-Denis',
    '94': 'Val-de-Marne',
    '95': 'Val-d\'Oise',
    '971': 'Guadeloupe',
    '972': 'Martinique',
    '973': 'Guyane',
    '974': 'La Réunion',
    '976': 'Mayotte',
}

today = datetime.date.today()
date = today - datetime.timedelta(days=1)
date = str(date)
week=[]
week.append(date)

print(today, 'welcome to our application')

dpt = input("Entrer le nom ou le code votre département ")
url = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=donnees-hospitalieres-covid-19-dep-france%40public&rows=999&facet=date&facet=countrycode_iso_3166_1_alpha3&facet=region_min&facet=nom_dep_min&facet=sex&refine.sex=Tous&refine.nom_dep_min=" + dpt + "&refine.date=" + date
url1="https://data.opendatasoft.com/api/records/1.0/search/?dataset=donnees-hospitalieres-covid-19-dep-france%40public&rows=999&facet=date&facet=countrycode_iso_3166_1_alpha3&facet=region_min&facet=nom_dep_min&facet=sex&refine.sex=Tous&refine.nom_dep_min=" + dpt + "&refine.date=" + date


root = tk.Tk()
v = tk.StringVar()
v.set("day_death_new")  
def clicked():
    p= v.get()
   
Parameters = [('day_death_new','day_death_new'),
('day_hosp_new','day_hosp_new'),
('day_intcare','day_intcare'),
('tot_out','tot_out'),
('tot_death','tot_death'),
('day_hosp','day_hosp'),
('day_out_new','day_out_new'),
('day_intcare_new','day_intcare_new')]
tk.Label(root,
         text="""Please Choose a parameter""",
         justify = tk.LEFT,
         padx = 20).pack()
for parameter, val in Parameters :
    tk.Radiobutton(root,
                   text=parameter,
                   padx = 20,
                   variable=v,command=clicked,
                   value=val).pack(anchor=tk.W)
button = tk.Button(root,text="Submit",command=root.destroy).pack(anchor=tk.W)    

root.mainloop()
p = v.get()



def example1():
    def print_sel():
        print(cal.selection_get())
       
root = tk.Tk()
top = tk.Toplevel(root)
cal = Calendar(top,font="Arial 14", selectmode='day',cursor="hand1", year=2021, month=1, day=1)
cal.pack(fill="both", expand=True)
ttk.Button(top, text="ok", command=root.destroy).pack()
s = ttk.Style(root)
s.theme_use('clam')
ttk.Button(root, text='Calendar',command=example1).pack(padx=10, pady=10)
root.mainloop()
date=cal.selection_get()
print(date)
date=str(date)


datee = datetime.datetime.strptime(date, "%Y-%m-%d")
year=datee.year
month=datee.month
day=datee.day






for (k, v) in DEPARTMENTS.items():

        if (dpt == v):
            url = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=donnees-hospitalieres-covid-19-dep-france%40public&rows=999&facet=date&facet=countrycode_iso_3166_1_alpha3&facet=region_min&facet=nom_dep_min&facet=sex&refine.sex=Tous&refine.nom_dep_min=" + dpt + "&refine.date=" + date
            url1= "https://data.opendatasoft.com/api/records/1.0/search/?dataset=donnees-hospitalieres-covid-19-dep-france%40public&rows=999&facet=date&facet=countrycode_iso_3166_1_alpha3&facet=region_min&facet=nom_dep_min&facet=sex&refine.sex=Tous&refine.nom_dep_min="+v
            w=v
        elif (dpt == k):
            url = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=donnees-hospitalieres-covid-19-dep-france%40public&rows=999&facet=date&facet=countrycode_iso_3166_1_alpha3&facet=region_min&facet=nom_dep_min&facet=sex&refine.sex=Tous&refine.nom_dep_min="+v+ "&refine.date=" + date
            url1= "https://data.opendatasoft.com/api/records/1.0/search/?dataset=donnees-hospitalieres-covid-19-dep-france%40public&rows=999&facet=date&facet=countrycode_iso_3166_1_alpha3&facet=region_min&facet=nom_dep_min&facet=sex&refine.sex=Tous&refine.nom_dep_min="+v
            w=v
        
#print(url1)


#print (url)
r = requests.get(url)
r1 = requests.get(url1)

import json

jsondata = r.json()
jsondata1 = r1.json()

######################################
# conversion en texte pour l'enregistrement

jsondatastr = json.dumps(jsondata, indent=4)
jsondatastr1 = json.dumps(jsondata1, indent=4)

#print(len(jsondata1['records'])-1)

def missdata(m):
    for j in range(0,len(jsondata1['records'])):
        if m in jsondata1['records'][j]['fields']:
            print('exist',j)
            
        else: print('not exist',j)
#missdata('day_death_new')


# print (type(jsondatastr))

#####################################
# Create a subfolder and save JSOn data
# import os
# os.makedirs('data')
covid_data = open('data\covid.JSON', 'w')
covid_data.write(jsondatastr)
covid_data.close()

covid_data1= open('data\covid1.JSON', 'w')
covid_data1.write(jsondatastr1)
covid_data1.close()

#####################################

def result():
    print()
   
   
    print("Nombre de personnes actuellement hospitalisées à",
          dpt, " =", jsondata['records'][0]['fields']['day_hosp'])
    print("Nombre total de personnes actuellement en réanimation à",
          dpt, " =", jsondata['records'][0]['fields']['day_intcare'])

    print("Nombre quotidien de nouvelles admissions en réanimation à",
          dpt, " =", jsondata['records'][0]['fields']['day_intcare_new'])
    print("Nombre total de retour à domicile à", dpt, " =",
          jsondata['records'][0]['fields']['tot_out'])
    print("Nombre quotidien de retour à domicile à", dpt, " =",
          jsondata['records'][0]['fields']['day_out_new'])
    print("Les nouveaux décès d'aujourd'hui à ", dpt, " =",
          jsondata['records'][0]['fields']['day_death_new'])
    print("Nombre total de décès à", dpt, " =",
          jsondata['records'][0]['fields']['tot_death'])

res1=("Nombre de personnes actuellement hospitalisées à "+str(dpt)+"="
           + str(jsondata['records'][0]['fields']['day_hosp']))
res2=("Nombre quotidien de personnes nouvellement hospitalisées à "+str(dpt)+"="
           + str(jsondata['records'][0]['fields']['day_hosp_new']))
res3=("Nombre total de personnes actuellement en réanimation à "+str(dpt)+"="
           + str(jsondata['records'][0]['fields']['day_intcare']))
res4=("Nombre quotidien de nouvelles admissions en réanimation à "+str(dpt)+"="
           + str(jsondata['records'][0]['fields']['day_intcare_new']))
res5=("Nombre total de retour à domicile à "+str(dpt)+"="
           + str(jsondata['records'][0]['fields']['tot_out']))
res6=("Nombre quotidien de retour à domicile à "+str(dpt)+"="
           + str(jsondata['records'][0]['fields']['day_out_new']))
res7=("Les nouveaux décès d'aujourd'hui à "+str(dpt)+"="
           + str(jsondata['records'][0]['fields']['day_death_new']))
res8=("Nombre quotidien de personnes nouvellement hospitalisées à "+str(dpt)+"="
           + str(jsondata['records'][0]['fields']['day_hosp_new']))
res9=("Nombre total de décès à "+str(dpt)+"="
           + str(jsondata['records'][0]['fields']['tot_death']))


def checkCovid():
    try:
        for (k, v) in DEPARTMENTS.items():

            if (dpt == v):
                print(' Le département cherché est ', dpt)
                print(result())
            elif (dpt == k):
                print('le code utilisé est ', dpt, 'de département = ', v)
                print(result())
    except:
        #messagebox.showinfo("Erreur, verifier bien le nom ou le code de votre département ")
        checkCovid()

checkCovid()

import numpy as np
#print(len(jsondata1['records']))

def p_accumulation(f):
    x=[]
    y=[]
    for i in range(0,len(jsondata1['records'])):
        if f in jsondata1['records'][i]['fields']:
            y.append(jsondata1['records'][i]['fields'][f])
            
        else:y.append(0)
        
        x.append(i)
            
    y=np.cumsum(y)
    plt.plot(x,y)
    plt.title(f)
    plt.xlabel("Days")
    plt.ylabel(p)
    
    fig2=plt.gcf()
    plt.show()
    fig2.savefig("templates\p_accumulation.png")

def p_tendance(f):
    x=[]
    y=[]
    for i in range(0,len(jsondata1['records'])):
        if f in jsondata1['records'][i]['fields']:
            y.append(jsondata1['records'][i]['fields'][f])
            
        else:y.append(0)
        
        x.append(i)

    plt.plot(x,y)
    plt.xlabel("Days")
    plt.ylabel(p)
    plt.title(f)
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig("templates\p_tendance")
    


p_tendance(p)
p_accumulation(p)


#print(y)
#print(x)    
x=[]
y=[]  

def last_week(f): 
    x=[]
    y=[]    
    week=[]

    for i in range(1,8):
        
        today = datetime.date.today()
        date1 = today - datetime.timedelta(days=i)
        date2 = str(date1)
        week.append(date2)
    
    for i in range(0,7):
        for j in range(0,len(jsondata1['records'])):
            x.append(j)
            if week[i] == jsondata1['records'][j]['fields']['date']:
                  if f in jsondata1['records'][j]['fields']:
                      y.append(jsondata1['records'][j]['fields'][f])    
                  else:y.append(0)
    
    print(week)
    print('Nombre de décès par semaine =',sum(y))

op=sum(y)    
lweek=('Nombre de décès de cette semaine = '+ str(op))
last_week(p)

r=[]
t=[]
def by_week(f,year,month,day): 

    year=int(year)
    month=int(month)
    day=int(day)
        
    week=[]
    for i in range(1,8):
        
        nday = datetime.date(year,month,day)
        date1 = nday - datetime.timedelta(days=i)
        date2 = str(date1)
        week.append(date2)
    
    for i in range(0,7):
        for j in range(0,len(jsondata1['records'])):
            r.append(j)
            if week[i] == jsondata1['records'][j]['fields']['date']:
                  if f in jsondata1['records'][j]['fields']:
                      t.append(jsondata1['records'][j]['fields'][f])    
                  else:t.append(0)    

                
    print(week)
    print('Nombre de décès par semaine =',sum(y))
os=sum(t)
by_week(p,year,month,day)



from flatten_json import flatten

import csv

import json


json_flatten_data = flatten(jsondata)


f = open("data\Covid-19.csv", "w")
all_keys = []
for elt in json_flatten_data:
    all_keys.append(elt)
#print(all_keys)
writer = csv.DictWriter(f, all_keys)
writer.writeheader()
writer.writerow(json_flatten_data)
f.close()



type(jsondata)

from flatten_json import flatten

import csv

import json


json_flatten_data = flatten(jsondata)
f = open("Covid_19.csv", "w",newline="\n")
all_keys = []
for elt in json_flatten_data:
    all_keys.append(elt)
#print(all_keys)
writer = csv.DictWriter(f, all_keys, delimiter=";")
writer.writeheader()
writer.writerow(json_flatten_data)
f.close() 

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
 
wordcloud = WordCloud(max_words=5,
                                    stopwords= STOPWORDS,
                                    background_color='white',
                                    width=1200,
                                    height=1000).generate(jsondatastr)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


stop_words = ["facets", "count","name","path","state","date","countrycode_iso_3166_1_alpha3","region_min","nom_dep_min"] + list(STOPWORDS)
wc = WordCloud(stopwords = stop_words, background_color="white").generate(jsondatastr)

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
wc.to_file("templates/wordcloud.png")

today=str(today)

@app.route('/result')          
def result1():
   
    return (render_template("result.html",w=w,res1=res1,res2=res2,res3=res3,res4=res4,res5=res5,res6=res6,res7=res7,res8=res8,res9=res9,lweek=lweek,op=op))

@app.route('/home')
def index():
    return render_template("index.html",today=today,w=w)

@app.route('/covid')
def covid():

    return render_template("covid.html",department=DEPARTMENTS )

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form['nm']
        return redirect(url_for("user",usr=user))
    else: 
        return  render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__=="__main__":
    app.run(debug=True)




