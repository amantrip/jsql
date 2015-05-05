## JSQL: JSON Query Language ##

JSQL or JSON Query Language is a simple language with two overarching goals:
	- Query JSON Objects: This includes being able to SELECT, SUM, COUNT, DELETE, ORDER BY, LIMIT etc. 
	- Manipulate JSON Objects: Add, Subtract, Find Union, and Intersection etc. 

Additionally, JSQL provides some basic functions, which can be used as a bootstrap to build more complex functions. Within the above-mentioned goals, JSQL provides additional features including regex queries, and distributed processing of queries.   One of the immediate applications of such a language can be dynamically building queries for JSON objects based on user-input or merging multiple JSON objects from different sources.

### Folder Structure ###
- main.py
- JSQL
	- org: consists of JSON Simple
	- scripts: lex, yacc and parse tables
	- utils: Java Worker
- testing
	- tests: consists of all tests
		- test1.jsql
		- test2.jsql
	- runall.sh: This script runs, compiles and tests all tests in the tests folder.
	


