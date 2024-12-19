```c++
char s[N];
int t[N][123],cnt[N],idx=0;

//映射
int getnum(char x)
{
	if (x>='A'&&x<='Z') return x-'A';
	else if (x>='a'&&x<='z') return x-'a'+26;
	else return x-'0'+52;
}

//插入
void insert(char str[])
{
	int p=0;
	foo(i,0,strlen(str))
	{
		int c=getnum(str[i]);
		if (!t[p][c]) t[p][c]=++idx;
		p=t[p][c];
		cnt[p]++;//如果这行代码写在循环外面则不能用于解决前缀问题
	}
}

//查找
int find(char str[])
{
	int p=0;
	foo(i,0,strlen(str))
	{
		int c=getnum(str[i]);
		if (!t[p][c]) return 0;
		p=t[p][c];
	}
	return cnt[p];
}
```
```
