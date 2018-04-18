import bottle

@bottle.route("/")
def home_page():
    mythings = ['apple', 'orange', 'banana', 'peach']
    return bottle.template('hello_world', username='Andrew', things=mythings)

@bottle.route("/testpage")
def test_page():
    return "this is a test page"

bottle.debug(True)
bottle.run(host="10.197.9.97", port=8982)
