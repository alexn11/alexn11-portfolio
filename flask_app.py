import flask
from lib.portfolio import load_portfolio

app = flask.Flask(__name__, template_folder='templates')


initial_state = {}


  


@app.route('/', methods=['GET', 'POST'])
def main():

  state = initial_state
  portfolio_columns, portfolio, tag_list = load_portfolio()

  if(flask.request.method == 'GET'):
    return flask.render_template('main.html',
                                  state = state,
                                  portfolio_columns = portfolio_columns,
                                  tag_list = tag_list,
                                  portfolio = portfolio)
    
  if(flask.request.method == 'POST'):
  
    form_values = flask.request.form
    #state = {}
    
    return flask.render_template('main.html',
                                 state = state,
                                 portfolio_columns = portfolio_columns,
                                  tag_list = tag_list,
                                 portfolio = portfolio)



if __name__ == '__main__':
    app.run()
    



















