from variables import *

@app.route("/", methods=["GET", "POST"])
def welcome():
    return render_template("welcome.html")

@app.route("/standings", methods=["GET", "POST"])
def standings():

    generate_standings_list()

    return render_template("standings.html", standings_list = standings_list)

@app.route("/predictions", methods=["GET", "POST"])
def predictions():

    generate_concise_race_list()

    check_remaining_races(race_list)

    race_count = len(rem_races_list)

    generate_standings_list()

    return render_template("predictions.html", standings_list = standings_list, race_count = race_count, rem_races_list = rem_races_list)

@app.route("/results", methods=["GET", "POST"])
def results():

    predictions_list.clear()

    for round in rem_races_list:
        check_pred = []
        if round["race_type"] == "sprint":
            round = round["round"]
            print(round)
        else:
            round = int(round["round"])

        for driver in standings_list:
            position = int(driver["position"])

            pred_1 = request.form.get(f"prediction{position}{round}")
            
            for pred in check_pred:
                if pred_1 == pred and (pred_1 not in ('0', '')):
                    return render_template("/apology.html")
            
            check_pred.append(pred_1)
            print(check_pred)


    for driver in standings_list:
        race_predictions = []
        position = driver["position"]
        name = driver["name"]
        
        for race in rem_races_list:
            if race["race_type"] == "sprint":
                round = race["round"]
                prediction = request.form.get(f"prediction{position}{round}")
                prediction_dict = {
                    "race_type": "sprint",
                    "prediction": prediction
                }
            elif race["race_type"] == "normal":
                round = int(race["round"])
                prediction = request.form.get(f"prediction{position}{round}")
                prediction_dict = {
                    "race_type": "normal",
                    "prediction": prediction
                }
            
            race_predictions.append(prediction_dict)
            
        predictions_list.append(race_predictions)

    for index, pred_list in enumerate(predictions_list):
        score_predict = 0
        for prediction in pred_list:
            if prediction["race_type"] == "normal":
                if prediction["prediction"] == '1':
                    points = 25
                elif prediction["prediction"] == '2':
                    points = 18
                elif prediction["prediction"] == '3':
                    points = 15
                elif prediction["prediction"] == '4':
                    points = 12
                elif prediction["prediction"] == '5':
                    points = 10
                elif prediction["prediction"] == '6':
                    points = 8
                elif prediction["prediction"] == '7':
                    points = 6
                elif prediction["prediction"] == '8':
                    points = 4
                elif prediction["prediction"] == '9':
                    points = 2
                elif prediction["prediction"] == '10':
                    points = 1
                else:
                    points = 0
                
                score_predict = score_predict + points
            elif prediction["race_type"] == "sprint":
                if prediction["prediction"] == '1':
                    points = 8
                elif prediction["prediction"] == '2':
                    points = 7
                elif prediction["prediction"] == '3':
                    points = 6
                elif prediction["prediction"] == '4':
                    points = 5
                elif prediction["prediction"] == '5':
                    points = 4
                elif prediction["prediction"] == '6':
                    points = 3
                elif prediction["prediction"] == '7':
                    points = 2
                elif prediction["prediction"] == '8':
                    points = 1
                else:
                    points = 0

                score_predict = score_predict + points

        current = int(standings_list[index]["points"])
        new_standings = current + int(score_predict)
        standings_list[index].update(predicted_standings = new_standings)
        
    print(standings_list)

    return render_template("results.html", standings_list = standings_list)
