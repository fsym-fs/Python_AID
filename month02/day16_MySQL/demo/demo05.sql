--事务操作
--启动事务（二选一）
begin;
start transaction;

......操作
commit;

--回到事务初始状态
rollback;

begin;
delete from cls where id = 1;
update cls set score = 83 where name = 'Emma';
commit;