# Note that as our custom news module is loaded, it also displays a message about that.
# This is because the commands executed in the module are also loaded into this workspace.
# To prevent needless executions, use the if __name__ == "__main__" condition which ensures that the commands are
# only executed when the module is invoked directly. This is why the get_news_from_cnn function
# does not get invoked automatically.
import news

# Printing the fist 5 news articles loaded from CNN
for article in news.get_news_from_cnn()[:5]:
    print(article)
