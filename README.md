# Polls app

This app has
+ registration
+ you can create questions and answers as many as you need
+ user can answer only one time in question, after answering question will disappear

You can have a look works app [here](http://34.72.161.12/)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Installing on locacl machin

A step by step series of examples that tell you how to get a development env running

First need download project, in terminal write:

```
git clone https://github.com/Krasnovskii/polls_webapp_django
```

Than go to derictory 'polls_webapp_django' and install requriments:

```
pip install -r requirements.txt
```
If you dont have 'pip' and 'python3.8' than you need install it:

```
sudo apt update
```
```
sudo apt install python3.8
```
check version of 'Python':

```
python3 --version
```
If all ok you shold see ``` Python 3.8 ``` in therminal.

So we can install pip now:
```
python -m pip install --upgrade pip
```
check version of 'pip'
```
pip --version
```
if all ok, you shold see ``` pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8) ```

### Run up app

In derictory 'polls_webapp_django'
```
python3 manage.py runserver
```
if all ok tou shoold see:
```
Django version 3.2.7, using settings 'my_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
acess to app http://127.0.0.1:8000/

### Break down into end to end tests

If you wish stop testing app, you need press CTRL+C and app immediately will be stop.



## Built With

* [https://www.djangoproject.com/] Django framework used
* [https://getbootstrap.com/] - Bootstrap 5
* [https://www.sqlite.org/index.html] - SQLite


## Authors

Sergei Krasnovskii

## License

This project is licensed as open soure you can use it everywhere.

## Thank you
