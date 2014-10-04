import cgi
import os
import jinja2
import webapp2

# import sentiment_analyser
from sentiment_analyser import analyse

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class SubmitPage(webapp2.RequestHandler):
    def post(self):
        input_url = cgi.escape(self.request.get('url'))
        response_code, response_content = analyse(input_url)

        if response_code is 0:
            template = JINJA_ENVIRONMENT.get_template('error.html')
            self.response.write(template.render(error_text=response_content, input_url=input_url))
        else:
            template = JINJA_ENVIRONMENT.get_template('results.html')
            self.response.write(template.render(percentage_pos=response_content[0], percentage_neg=response_content[1], terms_total=response_content[2], terms_pos=response_content[3], terms_neg=response_content[4], list_pos=response_content[5], list_neg=response_content[6], input_url=input_url))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/submit', SubmitPage)
], debug=False)