# 查并集

## **问题**&#x20;

有$n$个节点，节点之间有$m$对关系，找到节点直接的圈子

## **暴力解法**&#x20;

将一对有关系的节点放到一个集合中，若存在两个集合，则对集合进行合并。

## **高效解法**

* 对于新的关系，寻找两个节点是否有公共祖先，没有则合并，将一个祖先的祖先设置为另一个祖先，找祖先的代码：

```python
def find(x):
    if nums[x] != x:
        nums[x] = find(nums[x])
    return nums[x]
```

* 合并的时候将简单的树合并到复杂的树上，以尽量控制树的深度。

```python
def merge(x,y):
    if rank[x] < rank[y]:
        x, y = y, x
    rank[x] = rank[x] + rank[y]
    nums[y] = x
```
