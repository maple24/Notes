## python requests vs javascript fetch
Although python and javascript are both syncronous programming language by default, python requests module is blocking and javascript fetch/axios module is not.
This means after sending a request, python waits for response, while javascript continues running following codes.
Both have some problems, for python, no further codes proceed until get response back, it is gonna take lots of time waiting. 
For javascript, response may be lost.
Asyncronous is most widely used in such situation. However, multiple threads can also solve the above problem for python since it does not lose data, it is just a matter of time.
