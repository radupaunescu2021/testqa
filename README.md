# testqa

Sample testing project with python bdd behave of web page https://www.demoblaze.com/


Clone repository
From inside testingPythonBehave folder open terminal

pip install behave

#run scenario

behave -n "Add laptops to cart,remove and pay" --no-logcapture

For Junit reports add --junit parameter


behave -n "Add laptops to cart,remove and pay" --no-logcapture --junit
