FROM python:3 
#from python 3 is the virtual machine for python you can find them hub,docker.com/_/python 

WORKDIR /BattleShip193
#where are we doing the work on that machine 
#so we make the folder called /app, restriction in linux 
COPY ./battle.py .
    #the file we made 

#COPY ./requirements.txt .
#first dot is the copying from the current dir, then it will pipeline from local to virtual machine 

RUN pip install -r requirements.txt  
#install everything in the manifest 

#run pip freexzd

CMD ["python", "battle.py"]
#run a command 


