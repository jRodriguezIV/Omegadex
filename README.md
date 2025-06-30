# 📔 Omegadex Ω 
### The Final Codex — The Last Guide You Will Ever Need
***Master** the Essentials. Rule the **Knowledge**.*  

## 🚀 Usage  
1. Browse through the **Topics** section to find the topic you're interested in.  
2. Click on the topic's link to be taken directly to its respective cheat sheet in this repository.


## 📌 Topics

<details>
<summary>📈 <strong>FinTech</strong></summary>

<details>
<summary>📃 <strong>Theory</strong></summary>    

- **Vectorized VS Event Driven BackTesting**: Compares vectorized and event-driven backtesting approaches, highlighting their differences in speed, realism, complexity, and use cases for trading strategy evaluation         
→ [vectorized_vs_eventdriven_backtesting.md](FinTech/Theory/Vectorized_vs_EventDriven_BackTesting/vectorized_vs_eventdriven_backtesting.md)  

  --- 

</details> <!-- Close Theory -->

<details>
<summary>💹 <strong>Algorithmic Trading Strategies</strong></summary>    

- **Buy and Hold Strategy**: Demonstrates how to implement and visualize a buy and hold investment strategy by calculating and plotting cumulative portfolio returns from historical stock data       
→ [buy_and_hold_strategy.ipynb](FinTech/Aglorithmic_Trading_Strategies/Buy_and_Hold_Strategy/buy_and_hold_strategy.ipynb)  

  --- 

</details> <!-- Close Algorithmic Trading Strategies -->


<details>
<summary>👓 <strong>Data Visualization</strong></summary>    

- **Data_Visualization**: Time series visualization using Matplotlib, covering line plots, custom styling, multi-series charts, scatter plots, and histograms with full annotations      
→ [data_visualization.py](FinTech/Data_Visualization/data_visualization.py)  
    - Python notebook format for interactive data visualization  
    → [data_visualization.ipynb](FinTech/Data_Visualization/data_visualization.ipynb)  
- **3D Visualization**: Visualize implied volatility surfaces with 3D plotting in Python to explore the power of multi-dimensional financial data representation  
→ [3d_visualization.ipynb](FinTech/Data_Visualization/3D_Visualization/3d_visualization.ipynb)
- **Plotting Candlesticks**: Download, process, and visualize S&P 500 (SPY) historical price data as an interactive candlestick chart using Bokeh in Python    
→ [plotting_candlesticks.ipynb](FinTech/Data_Visualization/Plotting_Candlesticks/plotting_candlesticks.ipynb)
- **Bollinger Bands**: Calculate and plot Bollinger Bands for historical price data using Python and matplotlib.    
→ [bollinger_bands.ipynb](FinTech/Data_Visualization/Bollinger_Bands/bollinger_bands.ipynb)
 
  --- 

</details> <!-- Close Data Visualization -->



- **Time Value of Money (TVM)**  
Core formulas for calculating PV, FV, annuities, and interest in LATEX-style math notation format   
→ [time_value_money.md](FinTech/TVM/time_value_money.md)

  - Core formulas for calculating PV, FV, annuities, and interest in python coding format   
  → [time_value_money.py](FinTech/TVM/time_value_money.py)

- **Times Series Data**  
Key concepts and structures in time series data, including OHLCV, LTP, data granularities, and distinctions between time-related data types like cross-sectional, longitudinal, and panel data    
→ [time_series_data.md](FinTech/Time_Series_Data/time_series_data.md)

- **Libraries and SDKs for FinTech/Quant**  
  Overview of essential Python libraries, SDKs, and APIs for financial analysis, trading, and ML  
  → [libs_and_sdks.md](FinTech/libs_and_sdks/libs_and_sdks.md)

- **Quant Project Setup**  
 Provides a general template fo a clean, reproducible quant project  
→ [quant_project_setup.md](FinTech/Quant_Project_Setup/quant_project_setup.md)



</details> <!-- Close FinTech -->

<details>
<summary>💻 <strong>Computer Science</strong></summary>

<details>
<summary>🤖 <strong>Machine Learning</strong></summary>

- **Linear Regression**  
    Explains and demonstrates linear regression using scikit-learn, covering data preparation, model training, evaluation, and visualization of results      
    → [linear_regression.ipynb](Computer_Science/Machine_Learning/Linear_Regression/linear_regression.ipynb)

  - **Logistic Regression**  
    Demonstrates logistic regression using scikit-learn, including data preparation, model training, prediction, and visualization on the Iris dataset    
    → [logistic_regression.ipynb](Computer_Science/Machine_Learning/Logistic_Regression/logistic_regression.ipynb)



</details> <!--Close Machine Learning -->

- **Logarithmic Math**  
    A clear, math-focused cheat sheet explaining how to compute and interpret logarithms (base 2 and 10) by hand, with emphasis on their role in data allocation and algorithmic complexity  
    → [logarithmic_math.md](Computer_Science/logarithmic_math/logarithmic_math.md)



</details> <!-- Close Computer Science -->

<details>
<summary>🐍 <strong>Python</strong></summary>

<details>
<summary> &nbsp;&nbsp;&nbsp;&nbsp;🔢 <strong>Numpy</strong></summary>

- **Numpy**  
Introduces NumPy, demonstrating array creation, dimensionality, and shape manipulation for efficient numerical computing in Python           
→ [numpy.ipynb](Python/Numpy/numpy.ipynb)
  - **Indexing and Slicing Arrays**  
  Demonstrates how to index, slice, and initialize NumPy arrays, including creating arrays of ones, zeros, and identity matrices             
  → [indexing_and_slicing_arrays.ipynb](Python/Numpy/Indexing_and_Slicing_Arrays/indexing_and_slicing_arrays.ipynb)
  - **Vectorization and Broadcasting Arrays**  
  NumPy's vectorization and broadcasting features for efficient array operations, including arithmetic, comparison, and logical operations across arrays of different shapes               
  → [vectorization_and_broadcasting_arrays.ipynb](Python/Numpy/Vectorization_and_Broadcasting_Arrays/vectorization_and_broadcasting_arrays.ipynb)

</details> <!-- Close Numpy -->

<details>
<summary> &nbsp;&nbsp;&nbsp;&nbsp;🐼 <strong>Pandas</strong></summary>

- **Series**  
Introduces the pandas Series data structure, demonstrates its creation, manipulation, handling of missing data, and the use of methods like apply() for element-wise operations             
→ [series.ipynb](Python/Pandas/Series/series.ipynb)

<details><summary>&nbsp;&nbsp;&nbsp;&nbsp; 🪟<strong> DataFrames </strong></summary>

- **DataFrames**: Demonstrates how to create, manipulate, and analyze pandas DataFrames, including indexing, column operations, loading data, and sorting               
→ [dataframes.ipynb](Python/Pandas/DataFrames/dataframes.ipynb)
- **Descriptive Statistical Functions**: Demonstrates how to create, manipulate, and analyze pandas DataFrames, including indexing, column operations, loading data, and sorting               
→ [descriptive_statistical_functions.ipynb](Python/Pandas/DataFrames/Descriptive_Statistical_Functions/descriptive_statistical_functions.ipynb)
- **Indexing and Missing Values**: Demonstrates how to index, select, and manipulate pandas DataFrames, including handling missing values, replacing data, and reindexing                
→ [indexing_and_missing_values.ipynb](Python/Pandas/DataFrames/Indexing_and_Missing_Values/indexing_and_missing_values.ipynb)
- **Groupby**: Demonstrates how to use pandas groupby, aggregation, transformation, filtering, merging, and concatenation to analyze and combine data in DataFrames               
→ [groupby.ipynb](Python/Pandas/DataFrames/Groupby/groupby.ipynb)

</details> <!-- Close DataFrames -->
</details> <!-- Close Pandas -->
  


<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;📊 <strong>Data Structures</strong></summary>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;📖 <strong>Dictionaries</strong></summary>

- **Dictionaries**    
  A quick-reference Python cheatsheet for core dictionary operations including length, key/value access, deletion, popping, sorting, and clearing        
  → [dictionaries.py](Python/Data_Structures/Dictionaries/dictionaries.py)

  - **Dictionary Indexing and Access**  
  Covers concise, practical techniques for accessing, indexing, and navigating Python dictionaries, including nested data and safe retrieval methods    
    → [dictionary_indexing_and_access.py](Python/Data_Structures/Dictionaries/Dictionary_Indexing_And_Access/dictionary_indexing_and_access.py)

</details> <!-- Close Dictionaries -->

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;📋 <strong>Lists</strong></summary>

- **List Indexing and Access**  
  Techniques for accessing list elements, slicing, reverse indexing, and dictionary comparison  
  → [list_indexing_and_access.py](Python/Data_Structures/Lists/list_indexing_and_access/list_indexing_and_access.py)

- **List Manipulation**  
  Built-in list methods for adding, removing, updating, and sorting elements    
  → [list_manipulation.py](Python/Data_Structures/Lists/list_manipulation/list_manipulation.py)

</details> <!-- Close Lists -->


- **Data Structures Overview**  
  Concise reference for core Python data structures, their usage, and common operations. Stacks, Queues, and Trees         
  → [data_structures_overview.py](Python/Data_Structures/data_structures_overview.py)

- **Tuples and Sets**  
  A compact reference covering the fundamentals of Python tuples and sets, their creation, properties, and key operations like union, intersection, and immutability rules      
  → [tuples_and_sets.py](Python/Data_Structures/Tuples_and_Sets/tuples_and_sets.py)


</details> <!-- Close Data Structures -->

- **Lambda**  
  Explains Python's lambda (anonymous) functions and demonstrates their use with map() and filter() for concise data processing         
  → [lambda.ipynb](Python/Lambda/lambda.ipynb)
- **Conditional Statements**  
Explains Python conditional statements, demonstrating the use of if, elif, and else blocks to control program flow based on conditions       
→ [conditional_statements.ipynb](Python/Conditional_Statements/conditional_statements.ipynb)
- **Loops**  
Explains how to use for and while loops in Python to iterate over sequences and execute code blocks multiple times based on conditions         
→ [loops.ipynb](Python/Loops/loops.ipynb)

</details> <!-- Close Python -->



## 🎯 Purpose

- Aggregate essential formulas, code snippets, and library references  
- Keep content minimal, practical, and easy to scan  
- Serve as a go-to resource for coding, quant finance, and technical interviews


> 💡 Tip: Star ⭐ this repo to quickly find your way back when coding or prepping interviews!

---
