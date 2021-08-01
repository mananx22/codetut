#basic operations

#!/bin/bash

x=5
y=8
echo $((x+y))
echo $((x-y))
echo $((x*y))
echo $((x/y))

#exponentiation
echo $((x**y))

#remainder of division
echo $((y%x))

# rangeless 
echo {1..10}
echo {10..1} 
echo {0..30..3}
exit 0
