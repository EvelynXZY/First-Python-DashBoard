# Homework 1

Due: 2/4/2022

Review the instructions at [`docs/git.md`](../git.md) to get your repository started, setting up this assignment and future assignments. Make sure you are on the `hw1` branch before proceeding. Fetch/pull changes each time you sit down to work.
***

> A note on this assignment's verbosity: Many of the steps in this assignment are outlined here on a deeper level to help guide your understanding of the motivations behind the code design. Don't be intimidated by all of the different techniques and approaches, and you are not required to use them all -- take what's useful and use it to help you complete the assignment efficiently and get the autograder passing. The level of detail provided is meant to help, not slow you down.

## US Census API
Let's write some code to pull data from the US Census API. Visit the [Census API User Guide](https://www.census.gov/data/developers/guidance/api-user-guide.Example_API_Queries.html). Skim the contents of the entire guide, then visit the **Example API Queries** tab/section and start at the **Population Estimates Example**.

Read steps 1-7 to get a basic idea of how this endpoint works.

### Examine the tests provided in the starter code.
***
- Open `tests/test_census_api.py` to view example invocations of your application function in the form of automated tests. Do not commit changes to these tests. These tests will be run by the autograder for step 1 of this assignment. Observe the following:
    - The test is refining the syntax you are allowed to use. Some basic things need to be true of each student's submission (in addition to providing the correct output) in order for the test to pass :
        1. The function needs to be named `endpoint` in the module `assignments.hw1.census`. Remember that modules can simply be Python files.
        2. It must accept the arguments defined in the test. 
        3. It must handle the argument values in a way consistent with the arguments' structures and data types.

    - Observe how the tests work: For example, the test for `endpoint` establishes the "right answer" as `expected_url` and tests your function by making sure its output (`actual_url`) is what we expect.
    - This test is simply a very straightforward translation of the example provided in the Census's documentation. This simplicity and its guarantee of correctness (since it was in the documentation) shows why tests are often a good place to start coding, whether you're trying to answer a specific question (such as the Hispanic population by state in this example) or attempting general data exploration (starting here can kick off a bottom-up approach to building out your API client's functionality.)  
    - Notice that your API call `census.get` should perform the request and return a Pandas DataFrame of the data.
        - In practice, you could easily save your data after retrieving it by calling `.to_csv`, `to_hdf` or similar, but we aren't testing that here. If you'd like to save data while you work, save the files in the `data/` folder where they won't be tracked by git.
        - Normally we would take this response and clean up the output a bit to convert things back to appropriate data types and human-readable values-- however, this type of data cleaning will be reserved for a future module with a bit more Pandas under your belt.
    
    You should immediately see how writing code according to test specifications can focus your efforts and establish code standards for collaboration.
- Run `pytest` to observe why the test is failing and observe what a failing test looks like in general.

### Coding your API client - 60 points
***
> Note: while these steps follow a natural progression, the intent is that each step is able to be worked on without a complete solution from a previous step. For example, you might be able to get tests from section 2 to pass by generalizing your `variable_predicates` function even if you are stuck on your implementation of `geographies`. 
1. **Single example query -- 10 points per test, 40 points total**. 

    Write some functions to retrieve the example data and pass the tests provided. Here are some tips and observations:
    - Think carefully about efficient use of data types to keep your functions concise but generalizable -- the more you can think ahead, the more you can save yourself headaches in step 2 (Generalizing Your Client). Try to avoid complicated intermediate steps, and if you decide you do need them, put them in a separate function or module. For example, you might want to create a module named `categorical_variables` where you can define some [enumerables](https://docs.python.org/3/library/enum.html) based on the [Census variables documentation](https://www.census.gov/data/developers/data-sets/popest-popproj/popest/popest-vars.Vintage_2019.html). Notice that the `variable_predicates` argument in the test uses the "human-readable" value when passing the argument, while the query string encodes it using its ID. Think about why the test imposes this. Then take care to choose appropriate data types to perform conversions.
    - Similarly with the `geographies` argument, think carefully about the decision to use the `us` package and how it can help you perform conversions.
    - Use [requests](https://docs.python-requests.org/en/latest/) to make your API call. `requests.get` allows you to pass in query parameters using a Python dictionary, so take advantage of this -- notice that we didn't compose the querystring URL manually and instead focused on encoding each individual parameter as parameter values (as with `variables`) or key-value pairs (as with `variable_predicates`). Python's new [dictionary union operator](https://www.python.org/dev/peps/pep-0584/#specification) might be helpful.
    - You must obtain an API key from the Census to authenticate your API client. Do some digging to find the link to the API key request form. Examine the test to figure out the syntax for authenticating if you have not already.
        - You must store this API key in an environment variable and load it into your code using `os.environ` and `python-dotenv`: see your `.env` file for examples.
    - If you're stuck on what to do next or feel overwhelmed, try to add code that fixes whatever is causing your test to fail until you get a new error, repeating this process until your test passes.

2. **Generalizing your client - 5 points per test, 20 points total**

    Once your simple example test is passing, you will likely need to make some modifications to your code for it to handle all possible query options. The autograder will be testing a meaningful selection of queries. These tests will be hidden from you by the autograder, but you will be able to view the test output, including errors,s when you submit the assignment. Think about the following as you proceed:
    - You must figure out how your function will process the various inputs by thinking carefully about the specifications provided by the Census API, most of which are outlined in the Core Concepts section of the documentation.
    - When developing and testing your API, DO NOT include repeated external API requests inside of loops that iterate through all possible values -- Not only is this poor code design, but it puts an unnecessary strain on the Census's servers and network traffic. Many APIs will limit the rate at which you can make requests and may cut off your access if they find excessive activity coming from your IP address or API key.

## Scraping Wikipedia - Listception - 40 points

Keeping in mind web scraping etiquette, Wikipedia is a great source of scrapable information that we, as a class, can experiment on with eased concerns. Maybe we can fish for some project ideas...

Using any combination of [Wikipedia's Python client](https://wikipedia.readthedocs.io/en/latest/), [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Scrapy](https://docs.scrapy.org/en/latest/), or `pandas.read_html`, create a scraper that obtains the data for a meta-database of Wikipedia's featured lists.

Write a module `assignments.hw1.listception` containing the following functions:

1. **`featured_lists` - 20 points**
    - returns a DataFrame containing a row for each list provided on [Wikipedia's Featured Lists](https://en.wikipedia.org/wiki/Wikipedia:Featured_lists)
    - Each subcategory level should get its own column, going left-to-right down the hierarchy. For example, your first column should contain values from `["Arts", "Engineering and technology", "Everyday Life", ...]` and so on while the second column contains ["Art and architecture", "Media", ... , "Computing", "Engineering and technology", ...] and so on, until you have a column for each subsection level (values can be `NaN` for sections with fewer sublevels). Each row should contain the title of the list page and the URL for the page.

2. **`lists_content(pages)` - 20 points**
    - Takes a list of page titles and returns a DataFrame, indexed by `Page Title` and `Table Index` where each row represents a row from the table on a page. See [`pandas.DataFrame.set_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) for basic examples of setting indexes.

Happy scraping!