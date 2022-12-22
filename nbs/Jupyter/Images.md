
To show images in markdown cells:
```jupyter
![][path to the image]
```
for example:
```jupyter
![](assets/example.png)
```
will produce:
![](example.png)

One can also use HTML to show images (`src`) with lot's of flexibility: 
- to change the width add `width` (as string)
- for reference add `id`
```jupyter
<img width="500" caption="Session_rate" src="images/session_rate.jpg" id="figure_id"/>
```

then refer to the figure as: 
```text
[name to show](#figure_id)
```
 
also can refer to URL images: (for example in Google Colab we have to replace the reference by it's github link):
```
<img src="https://raw.githubusercontent.com/nesaboz/pytorched/8c41b15364234c31af4f6222b2251954131b4a94/nbs/images/transfer_learning_layer_replacement.jpg"/>
```

<img src="https://raw.githubusercontent.com/nesaboz/pytorched/8c41b15364234c31af4f6222b2251954131b4a94/nbs/images/transfer_learning_layer_replacement.jpg"/>

See this [great markdown guide](https://medium.com/analytics-vidhya/the-ultimate-markdown-guide-for-jupyter-notebook-d5e5abf728fd) for more.


