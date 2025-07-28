# CaliforniaHousingPricingP
House Price Prediction

1.[GitHub](http://github.com)

2.[VSCODE](http://code.visualstudio.com)

3.[Gitcli](https://cli.github.com/)

4.[Heruku](https://www.heroku.com/)

5.[Google Colab](https://colab.google/)

6.[Docker](https://www.docker.com/)
 
1)
* Creating environment in conda
```
conda create -p venv python==3.8 -y

```
* Activate Environment
```
conda activate venv/
```
* Install all the libraries by creating requirements.txt and listing all the required libraries and run this command
```
pip install -r requirements.txt
```
* Add Configuration with name and email for that run this command in the same env
```
git config --global user.name
git config --global user.email
```

* Now try to add,(status) commit and push into Github Repo
```
git add .
git status
git commit -m "___"
git push origin to main
```
2)
* Creating a Flask Web Application for the Project
Make sure you have files like pickles(xgb_hy and standardization)
or json format
```
XGBoost Model
```

* Download Postman for testing the web application(if you need to test)Otherwise

* Create create css and js files and home.html for the project
```
home.html
script.js
style.css
```

* Created gunicorn (to handle mutiple requests at a time act as WSGI) by creating Procfile( "web: gunicorn app:app") in it.
```
web: gunicorn app:app
```

* Deployment in Heruko

* Dockerize the entire project using Docker
```
FROM
COPY
WORKDIR
RUN
EXPOSE
CMD
```