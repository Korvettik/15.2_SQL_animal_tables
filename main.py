from flask import Flask, render_template, request, jsonify
import json
import sqlite3

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False






# Главная страница домашки
@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('index.html')



# 1 Поиск по id
@app.route('/search/', methods=['GET', 'POST'])
def search_page(json_str=False):
    s = request.args.get('id')
    with sqlite3.connect("new_animal") as con:
        cur = con.cursor()

        sqlite_query = f"""
            SELECT 
            "animal"("id"), "animal"("age_upon_outcome"), 
            "animal"("animal_id"), "animal"("name"), "animal"("date_of_birth"),
            "animal"("outcome_month"), "animal"("outcome_year"), 
            
            "types"("animal_type"),
            "breeds"("breed"),
            "outcome_types"("outcome_types"),
            "colors"("color1"),
            "outcome_subtype"("outcome_subtype")
            

            FROM 
            "animal" FULL JOIN "types", "breeds", "
            outcome_types", "colors", "outcome_subtype"
            
            ON 
            "animal"("id_type") = "types"("id_type"),
            "animal"("id_breed") = "breeds"("id_breed"),
            "animal"("id_color") = "colors"("id_color"),
            "animal"("id_outcome_subtype") = "outcome_subtype"("id_outcome_subtype"),
            "animal"("id_outcome_type") = "outcome_type"("id_outcome_type")
            
            WHERE animal(id) = {int(s)}
            """



        rows = cur.execute(sqlite_query).fetchall()  # вернет список кортежей

#     # создаем JSON объект
#     data = list()
#     for row in rows:
#         new_row = {"title": row[0],
#                    "country": row[1],
#                    "release_year": row[2],
#                    "rating": row[3],
#                    "description": row[4]}
#         data.append(new_row)
#
#     return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)