from webapp import webapp
from irisflower import data_reader as dr
from irisflower import correlation_analysis as corr

@webapp.route('/')
@webapp.route('/index')
def index():
    data = dr.read_data()
    correlations = corr.pairwise_correlations(data, graphical=False)
    return correlations
