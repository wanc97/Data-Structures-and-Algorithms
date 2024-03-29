# 回溯

## **基本思想**

* 回溯就是一个**决策树**的**DFS深度优先搜索**过程；
* 基本思路：决策遍历+停止判断；
* 做决策的过程就是向子节点递归的过程，回退的时候需要撤销选择回到原来的状态，或者说回到对应节点的状态；
* 动态规划和回溯都有递归+DFS搜索：
  * 动态规划一定有重叠子问题，而回溯没有。某种程度上说，动态规划的暴力求解阶段就是回溯算法。只是有的问题具有重叠子问题性质，可以用备忘录优化，将递归树大幅剪枝，这就变成了动态规划。
  * 动态规划有求最值的过程，将子问题的结果整合成一个，而回溯是记录所有满足的结果（也可能是找到一个满足的）
  * 动态规划是返回到最顶层后得到结果，而回溯是递归到最底层得到结果。
* 有时候适当调整选择顺序可以降低最坏复杂度。

## **通用框架**

```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```

1. 路径：也就是已经做出的选择。
2. 选择列表：也就是当前可以做的选择。
3. 结束条件：也就是到达决策树底层，无法再做选择的条件。

## **常见题目**

* n皇后：每行一个皇后，所以选择列表就是每一行的皇后的列数，选择的时候判断是否冲突；
* 全排列：每一步从剩下的选择中选择；
* m个元素平分成k个元素和相同的子集：决策深度为元素数m，每个元素有k种选择，每个集合的最终总和是确定的，用于判断是否合适；
  * 可以先对元素进行排序，优先选择较大的元素，更容易触发停止条件，以减小计算量。
  * 也可以从桶的角度，先选择桶，再选择元素放不放，各个桶之间的状态相对独立一些，可以把最坏复杂度从$O(k^m)$降到$O(k\*2^m)$。
* 求子集：每一个元素加或不加是选择，没有中间的剪枝，所以也可以不用模版直接迭代；
* 求组合：按顺序依次取，每一个元素加或不加是选择，当元素数量达到指定数量时停止；
* 求排列：不按顺序取，每一个元素加或不加是选择，当元素数量达到指定数量时停止；
* 括号组合：每次加一种（左右，大小）括号进去，判断是否不合法；
  * 如果是只有一种括号可以直接用数字记录括号数量是否合法，或者迭代生成；
  * 如果有多种括号，需要用栈来判断是否合法；
* 有向无环图求所有可能路径：
  * DFS回溯：
  * BFS：
