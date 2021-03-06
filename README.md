### Just trying out discord.py 😀

### To-Do
- [x] greet a newly joined member in a channel (random message)
- [x] while adding a reaction to a message send a message to a channel (<user> gave reaction to <user>)
- [x] parameterized command, create a role named the parameter recieved and assign it to the user.
- [x] using a parameterized command(eg - !register <name>) insert the name to database, if same name tries to register again send error message to channel.
- [x] with a role restricted command retrieve all names in the database ( eg - !names)

#### Commands
- `!register yourname` - to add yourname to the db
- `!names` - to list all names in db(requires `nikhil` role)
- `!role rolename` - to get the specified role  
 
**MySQL** To Create Table
```
CREATE TABLE users (
id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255)
)
```



### Screenshots
*Bot welcoming new users*
 
![di1](https://user-images.githubusercontent.com/57913645/140576146-1b40d59c-5830-4a13-942f-b758070b6772.jpg)
 
*`!role rolename` - to get the specified role*
 
![di2](https://user-images.githubusercontent.com/57913645/140576154-bf05fbf0-bf8a-45a4-841b-6733c48ecb74.jpg)
 
*`!register yourname` - to add yourname to the db*  
*`!names` - to list all names in db(requires `nikhil` role)*
 
![di3](https://user-images.githubusercontent.com/57913645/140576160-d6e851c4-4ea0-4aef-8688-b547413acbf5.jpg)
 
*Sending message when someone reacts*
 
![di4](https://user-images.githubusercontent.com/57913645/140576168-0e0538c4-9ca2-4717-bff6-a293cc99f9de.jpg)
