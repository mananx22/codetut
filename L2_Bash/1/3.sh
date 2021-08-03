#The select command

#!/bin/bash
# to show select command quesiton prompt like read command
PS3="which day is today?? "
select day in mon tue wed thu fri sat sun
do
echo "Hi, Manan Today is $day"
#to break the loop
break
done
exit 0