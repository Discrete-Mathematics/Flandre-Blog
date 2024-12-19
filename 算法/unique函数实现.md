```c++
int get_unique(int a[],int n)
{
    int j = 0;
    for(int i = 0 ; i < n ; i++)
    {
        if(a[i] != a[j])
        {
            j++;
            a[j] = a[i];
        }
    }
    return j + 1;//返回最后一个不重复数字下标的下一位
}
```
