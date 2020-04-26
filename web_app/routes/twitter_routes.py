
from flask import Blueprint, jsonify # render_template, request, flash, redirect

#from web_app.models import db, Book, parse_records
from web_app.services.twitter_service import api as twitter_api

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_data(screen_name):
    print("FETCHING..", screen_name)
    
    # fetch user info
    user = twitter_api.get_user(screen_name)

    #fetch their tweets 
    statuses = twitter_api.user_timeline(screen_name, tweet_mode="extended", count=35, exclude_replies=True, include_rts=False)

    return jsonify({"user": user._json, "num_tweets": len(statuses)})