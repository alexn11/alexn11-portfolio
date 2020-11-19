import flask
from lib.portfolio import load_portfolio

app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def main():
  
  portfolio_columns, portfolio, tag_list, other_projects = load_portfolio()
  
  return flask.render_template('main.html',
                                portfolio_columns = portfolio_columns,
                                tag_list = tag_list,
                                portfolio = portfolio,
                                other_projects = other_projects)

  
if __name__ == '__main__':
    app.run()
    



















