# Live Pair Programming

Offered as an alternative 90 minute session for those who aren’t able to or would prefer not to make the 3.5 hour commitment for the take home task + pair programming session.

# Front-end

[FE Live task](https://www.notion.so/FE-Live-task-d5576d6bf9d349a398f68210aa059c89)

Interview guidance: 

# Back-end

## Brief

Can be directly linked to candidates from here: [https://gist.github.com/holmesmr/18a95628cdccef7790139f4a6fd66a59](https://gist.github.com/holmesmr/18a95628cdccef7790139f4a6fd66a59)

We’d like you to create an API which provides ordered information on various entities from the Star Wars films by their statistics.

For the purpose of this task, you will use [SWAPI](https://swapi.dev/), a public Star Wars REST API. 

Your service should present an API which:

- Surfaces a list of starships sorted by name
- Allow the sort order to be ascending or descending
- Allow the sort key to be changed (e.g. sort by length or cost rather than name)

You may use a web application starter kit of your choice or provide your own pre-built “Hello, World!” application.

## Evaluation criteria

- The candidate should be able to structure a basic REST API using JSON and make appropriate choices about naming and data structure.
- The candidate should be able to identify several details about the SWAPI service that will pose challenges for their implementation.
    - The need to “unpaginate” the Ship listing
    - Fields are “stringly typed”, i.e.