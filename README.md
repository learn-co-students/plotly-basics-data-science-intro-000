
# Going deeper with Plotly

### Learning Objectives

* Understand the iplot method
* Understand how to create different traces/plots like a scatter plot, or a line plot
* Understand how to have a chart with multiple traces

### Introduction

As you've seen in recent lessons, data science leans on data visualizations to draw inferences about our data, and to make sense of the math we use in making sense of this data.  We saw how plotting data with a bar chart can be used to show the relationship between $x$ and $y$ variables and how the impact that changing the y-intercept or slope variable has on a regression line.  

In this lesson, we'll explore even more functionality of the Plotly library.  As we do so, pay careful attention to the data type that our methods require: whether they are dictionaries or arrays, or arrays of dictionaries.  Ok, let's go!

### Drawing a line

As you know, to get started with Plotly, we first install the library on our computer.  Let's do so in Jupyter by executing the cell below.


```python
!pip install plotly
```

If plotly is already on your computer, pip will tell you that the require is already satisfied.  That's ok, we can happily proceed.

The next step is to import the plotly library. 


```python
import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>


If we plot offline, we do not need to provide a login.  So we plot offline, while plotting our first plot with the below line.


```python
plotly.offline.iplot([
    {}
])
```


<div id="3a85d414-1e12-4099-a932-97edc5e69ba0" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("3a85d414-1e12-4099-a932-97edc5e69ba0", [{}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


Let's take another look at that line of code.
```python
plotly.offline.iplot([
    {}
])
```

We reference the `plotly` library, which we imported above.  Then to the `iplot` method we pass a list, which has a dictionary in it.  That dictionary can represent a scatter trace, a line trace, or other types of traces.  

We pass the trace into a list because we can have more then one trace in the same graph - for example two bar traces displayed side by side or a scatter trace underneath a line trace.  

Now let's discuss how a trace represents data.  In the `trace` in the code below, we plot four points.  Notice that we provide the $x$ and $y$ coordinates in two separate attributes of the dictionary.  Change around the data to get a feel for how it works.


```python
trace = {'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4]}

plotly.offline.iplot([
    trace
])
```


<div id="e58e0367-a417-4863-a631-a873dc936967" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("e58e0367-a417-4863-a631-a873dc936967", [{"x": [1, 2, 3, 4], "y": [1, 2, 3, 4]}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


The plot above has one trace which is a line trace.  However this type of trace is just the default.  Note, that we did not specify any particular type.

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


<div id="428fe276-9942-4b5e-94f6-8a989670cb26" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("428fe276-9942-4b5e-94f6-8a989670cb26", [{"x": [1, 2, 3, 4], "y": [1, 2, 3, 4], "mode": "markers", "marker": {"color": "rgba(255, 182, 193, .9)"}}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


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


<div id="731b3213-d23e-46c1-b2d5-b3c5132c016b" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("731b3213-d23e-46c1-b2d5-b3c5132c016b", [{"x": [1, 2, 3, 4], "y": [1, 2, 3, 4], "mode": "markers", "marker": {"color": "rgba(255, 182, 193, .9)"}, "name": "Some dots"}, {"x": [1.5, 2.5, 3.5, 4.5], "y": [3, 5, 7, 9], "marker": {"color": "blue"}, "name": "Our nice line"}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


### Working with types

So far, we have only worked with either scatter charts or line charts.  The two charts are really quite similar -- connecting lines versus no connecting lines  -- and plotly treats them as such.  However, there are other ways of viewing the world beyond dots and lines.  Now let's see how.

For example, we can make a bar chart, simply by specifying the in our dictionary that the `type` is `bar` for a `bar` trace.


```python
bar_trace = {'type': 'bar', 'x': ['bobby', 'susan', 'eli', 'malcolm'], 'y': [3, 5, 7, 9], 'marker': {'color': 'blue'}, 'name': 'Our nice bar trace'}

plotly.offline.iplot([
    bar_trace
])
```


<div id="eda06702-234a-4fea-b4c2-fcc22641800d" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("eda06702-234a-4fea-b4c2-fcc22641800d", [{"type": "bar", "x": ["bobby", "susan", "eli", "malcolm"], "y": [3, 5, 7, 9], "marker": {"color": "blue"}, "name": "Our nice bar trace"}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


Now another way to create a bar chart is to use the constructor provided by plotly.  It's not too tricky to do so.  First, we import our `graph_objs` library from Plotly.  And then we call the bar chart constructor. 


```python
from plotly import graph_objs 

bar_trace_via_constructor = graph_objs.Bar(
            x=['bobby', 'susan', 'eli', 'malcolm'],
            y=[3, 5, 7, 9]
    )

bar_trace_via_constructor
```




    {'type': 'bar', 'x': ['bobby', 'susan', 'eli', 'malcolm'], 'y': [3, 5, 7, 9]}



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


<div id="feae0ef3-682c-45d1-b96d-e4878c184f88" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("feae0ef3-682c-45d1-b96d-e4878c184f88", [{"type": "bar", "x": ["bobby", "susan", "eli", "malcolm"], "y": [3, 5, 7, 9]}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


Now let's look at some constructors for make other traces.  


```python
graph_objs.Scatter()
```




    {'type': 'scatter'}




```python
graph_objs.Pie()
```




    {'type': 'pie'}



And of course, we can always use the dictionary constructor to create our dictionaries.


```python
pie_trace = dict(type="pie", labels=["chocolate", "vanilla", "strawberry"], values=[10, 5, 15])

plotly.offline.iplot([
    pie_trace
])
```


<div id="464546ec-26b8-45fc-85dd-2778fbb02ee4" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("464546ec-26b8-45fc-85dd-2778fbb02ee4", [{"type": "pie", "labels": ["chocolate", "vanilla", "strawberry"], "values": [10, 5, 15]}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


### Modifying a Chart Layout

So far we have seen how to specify attributes of traces or charts, which display our data.  Now let's see how to modify the overall layout in our chart.

Note that the format of our traces will not change.


```python
trace_of_data = {'x': [1.5, 2.5, 3.5, 4.5], 'y': [3, 5, 7, 9], 
                 'marker': {'color': 'blue'},
                 'name': 'Our nice line'}
```

However, instead of passing to our `iplot` function an array of traces, we pass our `iplot` function a dictionary with a `data` key, which has a value of an array of traces.  And a `layout` key, with a value of a dictionary representing our layout.


```python
layout = {'title': 'Scatter Plot'}
trace_of_data = {'x': [1.5, 2.5, 3.5, 4.5], 'y': [3, 5, 7, 9], 'marker': {'color': 'blue'}, 'name': 'Our nice line'}

figure = {'data': [trace_of_data], 'layout': layout}

plotly.offline.iplot(figure)
```


<div id="b6fb3a9b-9e10-4c0a-a9f1-f04425141759" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("b6fb3a9b-9e10-4c0a-a9f1-f04425141759", [{"x": [1.5, 2.5, 3.5, 4.5], "y": [3, 5, 7, 9], "marker": {"color": "blue"}, "name": "Our nice line"}], {"title": "Scatter Plot"}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


So above we used the `layout` to name our plot's title.  Now that we have used `layout` to specify our chart's title, let's also use it to specify our x axis range and y axis range.  Currently, we are allowing Plotly to automatically set our range.  But we can also specify this.


```python
layout = {'title': 'Scatter Plot', 'xaxis': {'range': [1, 10]}, 'yaxis': {'range': [1, 10]}}
trace_of_data = {'x': [1.5, 2.5, 3.5, 4.5], 'y': [3, 5, 7, 9], 'marker': {'color': 'blue'}, 'name': 'Our nice line'}

figure = {'data': [trace_of_data], 'layout': layout}

plotly.offline.iplot(figure)
```


<div id="43720a27-19ee-4e0e-91b1-587492959219" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("43720a27-19ee-4e0e-91b1-587492959219", [{"x": [1.5, 2.5, 3.5, 4.5], "y": [3, 5, 7, 9], "marker": {"color": "blue"}, "name": "Our nice line"}], {"title": "Scatter Plot", "xaxis": {"range": [1, 10]}, "yaxis": {"range": [1, 10]}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


So now, we can better see how the chart shows the proportional change between x and y values.

### Summary

In this section we saw how we can use Plotly's library to create data visualisations.  We create different traces to represent our data, with each trace represented as a dictionary which is passed to our `iplot` method.  We saw we can have multiple traces displayed in the chart, as the traces are wrapped in an array.  We saw that even when we use constructors like `graph_objs.Bar` to create a chart, all this does is create a dictionary which is then passed to our `iplot` method.  Then we moved onto modifying our layout for our charts, which is also just a python dictionary.  
