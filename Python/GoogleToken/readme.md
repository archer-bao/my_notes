expect不支持单双引号混用


alias sshjmp2='token=`gtoken`; expect -c "spawn ssh username@abc.xyz -p 123 -i ~/.ssh/key; expect \"\[M\" { send \"$token\r\";interact}"'
