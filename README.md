
# Going Deeper with Plotly

### Learning Objectives

* Understand the iplot method
* Understand how to create different traces/plots like a scatter plot, or a line plot
* Understand how to have a chart with multiple traces

### Introduction

As you've seen in recent lessons, data science leans on data visualizations to draw inferences about our data, and to make sense of the math we use in making sense of this data.  We saw how plotting data with a bar chart can be used to show the relationship between $x$ and $y$ variables.  

In this lesson, we'll explore more of the functionality of the Plotly library.  As we do so, pay careful attention to the data type that our methods require: whether they are dictionaries or lists, or lists of dictionaries.  Ok, let's go!

### Drawing a line

As you know, to get started with Plotly, we first install the library on our computer.  Let's do so in Jupyter by executing the cell below.


```python
!pip install plotly
```

If plotly is already on your computer, pip will tell you that the requirement is already satisfied.  That's ok, we can happily proceed.

The next step is to import the plotly library.


```python
import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
```

If we plot offline, we do not need to provide a login.  So we plot offline, while plotting our first plot with the below line.


```python
plotly.offline.iplot([
    {}
])
```

Let's take another look at that line of code.
```python
plotly.offline.iplot([
    {}
])
```

We reference the `plotly` library, which we imported above.  Then we pass a list containing a dictionary to the `iplot` method.  That dictionary can represent a scatter trace, a line trace, or other types of traces.  

We pass the trace into a list because we can have more than one trace in the same graph - for example two bar traces displayed side by side or a scatter trace underneath a line trace.  

Now let's discuss how a trace represents data.  In the `trace` in the code below, we plot four points.  Notice that we provide the $x$ and $y$ coordinates in two separate attributes of the dictionary.  Change around the data to get a feel for how it works.


```python
trace = {'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4]}

plotly.offline.iplot([
    trace
])
```

The plot above has one trace which is a line trace.  However, this type of trace is just the default.  Note, that we did not specify any particular type.

```python
trace = {'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4]}
```

We can change it by changing the mode to `markers`.  While we are at it, let's also change the color of the markers.  


```python
trace = {'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4], 'mode': 'markers', 'marker': {'color': 'rgba(255, 182, 193, .9)'}}

plotly.offline.iplot([
    trace
])
```

Cool!  So we changed the code to markers and changed the colors of those markers by setting the rgb (red, green, blue) value.

```python
trace = {'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4], 'mode': 'markers', 'marker': {'color': 'rgba(255, 182, 193, .9)'}}
```

Now let's add more than one trace to a given graph.  We'll keep the first trace largely the same by using the same data, and color of markers.  We'll name our trace 'Some dots'  by adding the name attribute and set it equal to the corresponding string.


```python
trace0 = {'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4],
          'mode': 'markers', 'marker': {'color': 'rgba(255, 182, 193, .9)'},
          'name': 'Some dots'}
```

In the second trace, we have some new data, and set the color as blue.  Because we did not specify a mode, it defaults to connecting the points as a line.  And we name our trace as "Our nice line".   


```python
trace1 = {'x': [1.5, 2.5, 3.5, 4.5], 'y': [3, 5, 7, 9],
          'marker': {'color': 'blue'},
          'name': 'Our nice line'}
```

Finally, we create a plot of the two traces.  


```python
plotly.offline.iplot([
    trace0, trace1
])
```

### Working with types

So far, we have only worked with either scatter charts or line charts.  The two charts are really quite similar -- connecting lines versus no connecting lines  -- and plotly treats them as such.  However, there are other ways of viewing the world beyond dots and lines.  Now let's see how.

For example, we can make a bar chart simply by specifying the `type` is `bar` for a `bar` trace in our dictionary.


```python
bar_trace = {'type': 'bar', 'x': ['bobby', 'susan', 'eli', 'malcolm'], 'y': [3, 5, 7, 9], 'marker': {'color': 'blue'}, 'name': 'Our nice bar trace'}

plotly.offline.iplot([
    bar_trace
])
```

Another way to create a bar chart is to use the constructor provided by plotly.  It's not too tricky to do so.  First, we import our `graph_objs` library from Plotly.  And then we call the bar chart constructor.


```python
from plotly import graph_objs

bar_trace_via_constructor = graph_objs.Bar(
            x=['bobby', 'susan', 'eli', 'malcolm'],
            y=[3, 5, 7, 9]
    )

bar_trace_via_constructor
```

We refer to the function `graph_objs.Bar` as a constructor because it literally constructs python dictionaries with a key of `type` that equals `bar`.  Then, we can pass this dictionary to our `iplot` method to display our bar chart.


```python
bar_trace_via_constructor = graph_objs.Bar(
            x=['bobby', 'susan', 'eli', 'malcolm'],
            y=[3, 5, 7, 9]
    )


plotly.offline.iplot([
    bar_trace_via_constructor
])
```

Now let's look at some constructors for make other traces.  


```python
graph_objs.Scatter()
```


```python
graph_objs.Pie()
```

And of course, we can always use the dictionary constructor to create our dictionaries.


```python
pie_trace = dict(type="pie", labels=["chocolate", "vanilla", "strawberry"], values=[10, 5, 15])

plotly.offline.iplot([
    pie_trace
])
```

### Modifying a Chart Layout

So far we have seen how to specify attributes of traces or charts, which display our data.  Now let's see how to modify the overall layout in our chart.

Note that the format of our traces will not change.


```python
trace_of_data = {'x': [1.5, 2.5, 3.5, 4.5], 'y': [3, 5, 7, 9],
                 'marker': {'color': 'blue'},
                 'name': 'Our nice line'}
```

However, instead of passing to our `iplot` function a list of traces, we pass our `iplot` function a dictionary with a `data` key, which has a value of a list of traces.  The `layout` key points to a dictionary representing our layout.


```python
layout = {'title': 'Scatter Plot'}
trace_of_data = {'x': [1.5, 2.5, 3.5, 4.5], 'y': [3, 5, 7, 9], 'marker': {'color': 'blue'}, 'name': 'Our nice line'}

figure = {'data': [trace_of_data], 'layout': layout}

plotly.offline.iplot(figure)
```

So above we used the `layout` to name our plot's title.  Now that we have used `layout` to specify our chart's title, let's also use it to specify the range of our x axis and y axis.  Previously, we were allowing Plotly to automatically set the range.  We can also adjust the range to meet our specifications.


```python
layout = {'title': 'Scatter Plot', 'xaxis': {'range': [1, 10]}, 'yaxis': {'range': [1, 10]}}
trace_of_data = {'x': [1.5, 2.5, 3.5, 4.5], 'y': [3, 5, 7, 9], 'marker': {'color': 'blue'}, 'name': 'Our nice line'}

figure = {'data': [trace_of_data], 'layout': layout}

plotly.offline.iplot(figure)
```

We can see how adjusting the range changes our perspective of the plotted x and y values.

### Summary

In this section we explored more of Plotly's library to create different data visualizations.  We created different traces to represent our data, with each trace represented as a dictionary passed to our `iplot` method.  We saw how to display multiple traces in a chart by wrapping the traces in a list.  We learned how to use constructors like `graph_objs.Bar` to create a chart. The constructor creates a dictionary that we can pass to our `iplot` method.  Finally, we moved onto modifying the layout of our charts with another python dictionary.
