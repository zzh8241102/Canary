# Clarifications
Author: [Zihan Zhou]
> Here the so called controller layer serves as helping the api layer to retrive the data and more like a DAO layer with the mixed service and controller layer 

> To make it simple, the class and func here will be used to retriving the data and the data pre-arrange with little handing(or algo? lol), just used to avoid the api layer re-write same codes

> It is better to use DAO->Service->Controller->API
> where the controller here is used to handle the outter requests