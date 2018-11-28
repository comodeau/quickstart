"""
This template is written by @Nocturnal-2

What does this quickstart script aim to do?
- I do some unfollow and like by tags mostly

NOTES:
- I am an one month old InstaPy user, with a small following. So my numbers in settings are bit conservative.
"""


from instapy import InstaPy
from instapy.util import smart_run



# get a session!
session = InstaPy(username='', password='' ,
                  headless_browser=True)


# let's go! :>
with smart_run(session):
    """ Start of parameter setting """
    # don't like if a post already has more than 200 likes
    session.set_delimit_liking(enabled=True, max=200, min=0)

    # don't comment if a post already has more than 6 comments
    session.set_delimit_commenting(enabled=True, max=6, min=0)

    """I used to have potency_ratio=-0.85 and max_followers=1200 for set_relationship_bounds()
        Having a stricter relationship bound to target only low profiles users was not very useful,
        as interactions/sever calls ratio was very low. I would reach the server call threshold for
        the day before even crossing half of the presumed safe limits for likes, follow and comments (yes,
        looks like quiet a lot of big(bot) managed accounts out there!!).
        So I relaxed it a bit to -0.50 and 2000 respectively.
    """
    session.set_relationship_bounds(enabled=True,
                                     potency_ratio=-0.50,
                                     delimit_by_numbers=True,
                                       max_followers=2000,
                                       max_following=3500,
                                       min_followers=25,
                                       min_following=25)
    session.set_do_comment(True, percentage=20)
    session.set_do_follow(enabled=True, percentage=20, times=2)
    session.set_comments([u'Amazing!', u' :heart_eyes: Awesome!!', u' :heart_eyes: Cool!', u' :heart_eyes: Good one!',
                           u' :heart_eyes: Really good one', u' :heart_eyes: Love this!', u' :heart_eyes: Like it!', u' :heart_eyes: Beautiful!', u'Great!',
						   u':heart: j\'aime, y\'a des bonnes choses a voir dans mon profile',
						  u':heart: j\'adore, visitez @{4s_style}',
						  u':heart: j\'aime',
						  u':heart: matnsach tchof le profile dyalna @{4s_style}',
						  u':heart: bonne visite @{4s_style}',
						  u':heart: @{4s_style} maroc style',
						  u':heart: fashion maroc @{4s_style}'])
    session.set_sleep_reduce(200)

    """ Get the list of non-followers
        I duplicated unfollow_users() to see a list of non-followers which I run once in a while when I time
        to review the list
    """
    # session.just_get_nonfollowers()

    # my account is small at the moment, so I keep smaller upper threshold
    session.set_quota_supervisor(enabled=True,
                                  sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                  sleepyhead=True, stochastic_flow=True, notify_me=True,
                                   peak_likes=(100, 700),
                                   peak_comments=(25, 200),
                                   peak_follows=(48, 125),
                                   peak_unfollows=(35, 400),
                                   peak_server_calls=(None, 3000))
    """ End of parameter setting """


    """ Actions start here """
    # Unfollow users
    """ Users who were followed by InstaPy, but not have followed back will be removed in
        3 days (72 * 60 * 60)
        Yes, I give a liberal one week time to follow [back] :)
    """
    session.unfollow_users(amount=25, InstapyFollowed=(True, "nonfollowers"), style="RANDOM",
                           unfollow_after=48 * 60 * 60,
                           sleep_delay=600)


    # Remove specific users immediately
    """ I use InstaPy only for my personal account, I sometimes use custom list to remove users who fill up my feed
        with annoying photos
    """
    # custom_list = ["sexy.girls.pagee", "browneyedbitch97"]
    #
    # session.unfollow_users(amount=20, customList=(True, custom_list, "all"), style="RANDOM",
    #                        unfollow_after=1 * 60 * 60, sleep_delay=200)

    # Like by tags
    """ I mostly use like by tags. I used to use a small list of targeted tags with a big 'amount' like 300
        But that resulted in lots of "insufficient links" messages. So I started using a huge list of tags with
        'amount' set to something small like 50. Probably this is not the best way to deal with "insufficient links"
        message. But I feel it is a quick work around.
    """

    session.like_by_tags(['caftanmarocain', 'caftans', 'caftandumaroc', 'caftanmaghribi', 'takchita',
						  'maroc', 'marocaine', 'casablanca', 'rabat', 'agadir', 'fes', 'tanger', 'tetouan', 'meknes','marrakech',
						  'moroccangirl', 'moroccangirls', 'marochijab', 'fashion', 'style', 'jumia',
						  'duniabatma', 'aminux', 'livraisongratuite'
						   ], amount=50)




