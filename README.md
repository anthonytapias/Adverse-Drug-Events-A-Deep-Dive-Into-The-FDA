# Beyond The FDA: Drug-Related Adverse Events in 2017


## Introduction
We have built an exploratory web application (via [Flask](http://flask.pocoo.org/) & [Dash](https://dash.plot.ly/)) that allows users to get information about FDA-regulated drugs (and their reactions) that were involved in "Adverse Events" reported to the FDA across different US holidays in 2017. Users are able to choose statistics and visualizations generated from a pre-defined set of SQLAlchemy queries.

The [FDA](https://fis.fda.gov/extensions/fpdwidgets/2e01da82-13fe-40e0-8c38-4da505737e36.html) defines Adverse Events (AE) as "...any symptom that occurs while taking a drug, which may or may not have been caused by the drug. This is different from an adverse drug reaction (ADR), where there is specific evidence that the AE is related to the drug. A side effect is the same as an ADR. As a result, ADR is always an AE, but an AE may or may not be an ADR."

Some questions that our app might help answer include:
- What were the most common drugs involved with adverse events during the holidays in 2017?
- What were the most common reactions reported during Adverse Events?
- On which holidays were the highest number of deaths, suicides, and attempted suicides reported?

## Gathering The Data
To collect the data, we queried the [FDA's API Drug Adverse Events endpoint](https://open.fda.gov/apis/drug/event/). This data was quite messy – in it were duplicate values in different fields, different structures for the same data, and clearly-impossible values for certain fields (e.g. 1000+ numbers for some ages). Cleaning the data and getting it into a workable format took the vast majority of our time. We attribute the state of the data to the fact that any medical professional can report AEs to the FDA, which introduces human error.

![alt text](https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/Screen%20Shot%202019-01-14%20at%207.45.40%20PM.png)

## Building The Database
After we got our data into a workable state, we then used [SQLAlchemy](https://www.sqlalchemy.org/) to store it in a relational database (you can view the code for that in the [models.py](https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/dash_package/models.py) file).  Because we wanted to focus on the narrative that users could create across drugs, drug brands, reported reactions, and holidays, we create six tables. Of these six, we had an association table as well as multiple tables modeling one:many and many:many relationships.

## Constructing The Queries
We then created queries (in the queries.py file) for the frontend of our app. Users could use drop-down menus to view the outputs of select queries. These queries included the number of adverse events for a given holiday or the top five reactions for a specific holiday that was choosen on the front end.

## Creating The Visualizations
In order to have a visual analysis of the data, we created several pie charts and graphs to display our data. This was written in HTML to be displayed in the Flask app. We found astonishing results and insights from our pie charts and graphs.
Here is what we found: We found that auto-immune disease medication came up frequently across all holidays as an adverse events.

### Top Five Reactions of one Holiday
We found that death had the most reactions on Christmas making up 28.4% of drug related events while drug ineffectiveness made up 25.1% of the drug related events. Interestingly off-label use made up the third most of drug related events at 19.4%.
<p align="center">
  <img width="500" height="475" src="https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/top_5_reactions_christmas.png">
</p>


### Top Five Brands of one Holiday
We found that Enbrel, which treats autoimmune diseases, came up the most at 57.8% of hospital visits. Cosentyx came up the second most at 11.8% which is used to treat moderate to severe plaque psoriasis.
<p align="center">
  <img src="https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/top_brands_christmas.png">
</p>

### Top Five Adverse Brands Across All Holidays
We used SQL-Alchemy to aggregate all the data of the number of drug related events a brand was associated with and compiled gthe results into a pie chart. We found that Enbrel again come up as the most in drug related adverse events with 35.5%, Makena,  is a progestin medication which is used to prevent preterm birth in pregnant women with a history of the condition and to treat gynecological disorders, making up 19% of the adverse events and Invokana, a medication used for the treatment of type 2 diabetes, which made 18.3% of the data.
<p align="center">
  <img src="https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/top_5_brands_all_holidays.png">
</p>

### Top Five Reactions Across All Holidays
Drug ineffectiveness was the most frequent reaction across all the observed holidays at 30.2%, death made up 20.7% of the data while nausea made up 17.2% of the dataV.
<p align="center">
  <img src="https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/top_5_reactions_all_holidays.png">
</p>

### Deaths Across All Holidays
Here are our obversations of the data we acquired containing the number of deaths per holiday. Cinco de Mayo had the most observed deaths, followed by Mardi Gras and Valentines Day. 
<p align="center">
  <img src="https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/deaths_and_suicides_with_bottomtab.png">
</p>

### Suicides Across All Holidays
Christmas made up the most suicides in drug related adverse events followed by Cannabis day and Thanksgiving. 
<p align="center">
  <img src="https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/suicides_per_holiday.png">
</p>

### Attempted Suicides Across All Holidays
Halloween had the most attempted suicides followed by Valentines day and Halloween. 
<p align="center">
  <img src="https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/attempted_suicides.png">
</p>


### Gender Analysis per Holiday
Below is an example of the gender analysis of Christmas. We found that in all the holidays, there were a larger percentage of women that were hospitilized because of a drug adverse event. This finding was particulary very interesting.
<p align="center">
  <img src="https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/gender_analysis.png">
</p>

## Deployment
We deployed our app (via the [run.py file](https://github.com/aulorbe/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA./blob/master/run.py)) through Flask and rendered our visualizations on the frontend with Dash. Rendering everything for the user was the last step in the construction of our ETL pipeline.

## Future Plans
In the future, we hope to build a website to host our app, so that users don't have to run the code themselves in order to view the final product.
