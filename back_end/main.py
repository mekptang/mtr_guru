from flask import Flask, request, json
from IPython.display import display
import time

import history_search.hr_plot_data as hr_plot
import history_search.lr_plot_data as lr_plot
import history_search.hr_data as hr

import route_search.route_suggestion as rs


# Set routes
app = Flask(__name__)

### FOR TESTING ###
@app.route("/")
def test():

    query = {
        'graph': 'p_lr_1a',
        'start_station_id': 'TML-TKW',
        'direction': 'up',
        'start_time': '2022-04-22 18:45',
        'end_time': '2022-04-22 19:05'  
    }

    start = time.time()
    result = hr.raw_hr_1_extract(query).to_string()
    end = time.time()

    print(end - start)

    return '<p>朋友</p>'


### HEAVY-RAIL ###
@app.route('/hr', methods=['POST'])
def p_hr():

    # Read the input json body
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = json.loads(request.data)
    else:
        return 'Content-Type not supported!'


    # Return the data for each graph request
    ### TYPE 1 - PLOTS RELATED TO STATION ###
    # p_hr_1a - Display real waiting time patterns (LineChart)
    if data['graph'] == 'p_hr_1a':
        return hr_plot.json_p_hr_1a_create(data)

    # p_hr_1b - Count number of train arrivals (BarChart)
    elif data['graph'] == 'p_hr_1b':
        return hr_plot.json_p_hr_1b_create(data)

    # p_lr_1c - Display eta delay time patterns (LineChart)
    elif data['graph'] == 'p_hr_1c':
        return hr_plot.json_p_hr_1c_create(data)

    # p_hr_1d - Display real delay time patterns (ScatterChart)
    elif data['graph'] == 'p_hr_1d':
        return hr_plot.json_p_hr_1d_create(data)


### LIGHT-RAIL ###
@app.route('/lr', methods=['POST'])
def p_lr():

    # Read the input json body
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = json.loads(request.data)
    else:
        return 'Content-Type not supported!'


    # Return the data for each graph request 
    ### TYPE 1 - PLOTS RELATED TO STATION ###
    # p_lr_1a - Display real waiting time patterns (Multiple Line Chart)
    if data['graph'] == 'p_lr_1a':
       return lr_plot.json_p_lr_1a_create(data)

    # p_lr_1b - Display eta delay time patterns (Multiple Line Chart)
    elif data['graph'] == 'p_lr_1b':
        return lr_plot.json_p_lr_1b_create(data)

    # p_lr_1c - Display real delay time patterns (Box Plot / Dot Plot)
    elif data['graph'] == 'p_lr_1c':
        return lr_plot.json_p_lr_1c_create(data)

    # p_lr_1d - Count number of train arrivals (Multiple Bar Chart)
    elif data['graph'] == 'p_lr_1d':
        return lr_plot.json_p_lr_1d_create(data)


    ### TYPE 2 - PLOTS RELATED TO TRIPS BETWEEN TWO STATIONS ###
    # p_lr_2a - Display combined waiting time of ALL available routes to a station (Line Chart)
    if data['graph'] == 'p_lr_2a':
        return lr_plot.json_p_lr_2a_create(data)


### Route Suggestion ###
@app.route('/route', methods=['POST'])
def p_route():

    # Read the input json body
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = json.loads(request.data)
    else:
        return 'Content-Type not supported!'

    return rs.suggest_route(data)


# if __name__ == "__main__":
#     app.run(host='0.0.0.0')

# start = time.time()
# end = time.time()

#h = end - start