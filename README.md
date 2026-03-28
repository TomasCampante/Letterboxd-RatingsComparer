# Letterboxd-RatingsComparer
Have you ever wondered how your movie ratings differ systematically from the average? Well, now you can!

## Step 1
Log in to you Letterboxd account; go into your profile; edit profile (account settings); data; and click in "EXPORT YOUR DATA".

## Step 2
This will start the download of a .zip folder containing different files. The file you are interested in is "ratings.csv". Copy/move it into the same directory as the python file ("plot_ratings.py") you can find in this GitHub repository.

## Step 3
Run the python file. You can do this in several different ways. It is assumed you know how to run a python file. If not, ask a search engine, artificial intelligence, or your nerd friend. Make sure to have all the necessary dependencies! 

The first time you run the program, it will take some time. This is because it is retrieve the average ratings for the movies you have rated from the Letterboxd servers.

After the script has ran, a plot will appear and a new file can be found in the directory where the "ratings.csv" and "plot_ratings.py" also are. In "all_data.csv" you can find a table with the movies you have rated, your rating, the avrage ratings on Letterboxd, and other less-important information.

## Step 4
You cna now make some plots with that data and get insights on how your ratings differ from the average. Are you nicer? Are you more demanding? What movies do you like that most people don't? What movies do most people like that you don't?

### Have fun

If you have any questions, please open an issue. I appreciate it. Enjoy!
