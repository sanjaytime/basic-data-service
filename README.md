Acceptance Criteria:

write code to do the following (keep in mind, we should be able to
reproduce your setup with your submitted code):
- Spin up a relational database (Postgres, MySQL, etc.). Docker containers are
preferred for ease of reproducibility.
- Define a table schema for each table in a relational database using SQL or a
language of your choice
- Parse the files linked at the end and bulk insert the data into your database
tables.

Next, we want you to simulate having an “analytics database” for hypothetical
Business Intelligence queries. Please write code to do the following:
- Spin up another database (eg. Postgres, MySQL, etc) separate from the first
one.
- Write code to replicate the tables in the first database into this one.
- Design a dimensional model/star schema using the above tables as the
source, keeping in mind the entity relationships described above. You can
design facts and dimensions as you deem appropriate.

Finally, we’d like to generate some insights from the analytical models you’ve just
built.
- Create a report (Jupyter notebook, PDF, etc) that has “insights” in the form of
charts, graphs, and summarizing statistics, as you deem appropriate
- Include the code that generates these insights and analytics (including code
that connects to and reads from the second database)
