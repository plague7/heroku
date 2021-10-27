from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

data=pd.read_csv("C:/Users/Simplon/Desktop/Travaux python/OpenFoodFacts - Cholesterole/dataNET_copie/data_cleaned.csv")

@app.route('/')
def index():
    return render_template('index.html')

#def notdash():
#
#    fig=px.histogram(data, x="pnns_groups_2", 
#                 color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
#    
#    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#
#    return render_template('notdash.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run()