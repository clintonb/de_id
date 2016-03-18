How this should work.

Data Ingestion
--------------
1. Ingest the data from a CSV/TSV into a SQLite database.
2. Filter out instructors/staff.
3. Copy the data a separate "read-only" table for comparison later.
4. Index the course_id and user_id columns.
5. Clean level of education (loe) data, mapping to a single set of levels.
6. Clean gender, treating N/A values as NULL.

De-identification #1
--------------------
1. Generate unique, anonymous user IDs to replace existing user ID values.

Analysis #1
-----------
1. Create a new column to store the entropy for each row.
2. Generate a utility matrix for both tables, and compare.

De-identification #2
--------------------
1. Establish k-anonymity by dropping rows to decrease the number of students that can be identified based on enrollment
   in a given combination of courses. See http://dataprivacylab.org/people/sweeney/kanonymity.html.
2. Remove students in unique combinations of courses (e.g. Alice is the only student in both courses Foo and Bar).

Analysis #2
-----------
1. Repeat the process from the first analysis to determine entropy for the remaining rows.
2. Determine the change in entropy

De-identification #3
--------------------
1. Map country country codes to continents.

Analysis #3
-----------
(Same as above.)

De-identification #4
--------------------
1. Group/bin rows based on the number of forum posts. (??? Tail finder ???)
   https://github.com/jdaries/de_id/blob/master/De-identification.py#L634-L658
2. Group/bin rows based on birth year.  (??? Tail finder ???)

Analysis #4
-----------
(Same as above.)

De-identification #5
--------------------
1. Apply L-diversity to the grade column.
2. ??? Flag users who did not complete the course: nevents is NULL and nchapters is NULL, ndays_act is NULL, or nforum_posts is 0.
   https://github.com/jdaries/de_id/blob/master/De-identification.py#L678-L710


Analysis #5
-----------
1. ??? Using new selection of columns to update the k-anonymity key. (Unsure which columns.)
   https://github.com/jdaries/de_id/blob/master/De-identification.py#L728-L735
2. Delete rows that do NOT meet our desired level of k-anonymity.
3. Provide stats: total rows remaining, students who viewed a course, explored a course, received a certificate.
4. Histogram/data for gender and birth year.
5. Repeat 4 and 5 for original data.
6. Generate a utility matrix for both tables, and compare.
