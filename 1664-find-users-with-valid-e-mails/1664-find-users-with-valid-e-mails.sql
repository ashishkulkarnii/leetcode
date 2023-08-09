select *
from Users
where mail rlike '^[:alpha:][[:alnum:]_.-]*@leetcode[.]com$';