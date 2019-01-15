# Beyond The FDA: Drug-Related Adverse Events in 2017


## Introduction
We have built an exploratory web application (rendered via Dash) that allow users to get information about FDA-regulated drugs (and their reactions) that were involved in "Adverse Events" reported to the FDA across different US holidays in 2017. Users are able to choose statistics generated from a pre-defined set of SQLAlchemy queries and their accompanying visualizations.

The [FDA](https://fis.fda.gov/extensions/fpdwidgets/2e01da82-13fe-40e0-8c38-4da505737e36.html) defines Adverse Events (AE) as "...any symptom that occurs while taking a drug, which may or may not have been caused by the drug. This is different from an adverse drug reaction (ADR), where there is specific evidence that the AE is related to the drug. A side effect is the same as an ADR. As a result, ADR is always an AE, but an AE may or may not be an ADR."

Some questions that our app might help answers include:
- What were the most common drugs involved with adverse events during the holidays in 2017?
- What were the most common reactions reported during Adverse Events?
- On which holidays were the most deaths, suicides, and attempted suicides reported?

## Gathering The Data
To collect the data that populated our database, we queried the [FDA's API Drug Adverse Events endpoint](https://open.fda.gov/apis/drug/event/). This data was quite messy and included duplicate values in different fields, different structures for the same data, and clearly-impossible values for certain fields (e.g. 1000+ numbers for some ages). Cleaning the data and getting it into a workable format took the vast majority of our time. We attribute the state of the data to the fact that any medical professional can report AEs to the FDA, which introduces human error into the data.

## Building The Database
After we got our data into a workable state, we then used [SQLAlchemy](https://www.sqlalchemy.org/) to store it in a proper database (you can view the code for that in the [models.py](https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/dash_package/models.py) file).  Because we wanted to focus on the narrative that users could create among drugs, drug brands, reported reactions, and holidays, we create six tables. Of these six, we had an association table as well as multiple tables modeling one:many and many:many relationships.

## Constructing The Queries


## Creating The Visualizations
![alt text](https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/top_five_reactions_christmas.png)
## Deployment

## Future Plans

