```
#include<iostream>
#include<queue>
using namespace std;

struct Pos
{
    int x,y;
}; //坐标点定义

queue <Pos> q;
int n,m,x,y,tx,ty,dis[1001][1001],s_a,s_b,t_a,t_b;
const int dx[]={1,-1,0,0};
const int dy[]={0,0,1,-1};
char mp[1001][1001];
bool vis[1001][1001]; //方向等变量的定义

int bfs(int sx,int sy)
{
  q.push((Pos){sx,sy}); //起点加入队列
  vis[sx][sy]=true; //标记
  while(!q.empty()) 
  {
      x=q.front().x;
      y=q.front().y; //获取起始坐标
      q.pop(); //弹出队列
      if(符合条件) return ans(答案); 
      for(int i=0;i<走法;i++)
      {
          tx=x+dx[i];
          ty=y+dy[i];
          if(符合条件) continue;
          if(符合条件) continue; //符合条件跳过循环
          /*
                         可行,执行该部分语句
                                                    */
          q.push((Pos){tx,ty}); //加入队列
      }
  }
  return -1;
}

int main()
{
    cin>>n>>m;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
        {
        	cin>>mp[i][j];
        	if(mp[i][j]=='d')
        	{
        		s_a=i;
        		s_b=j; //获取起点坐标
			}
		}
    int c;
    c=bfs(s_a,s_b);
    if(c==-1)cout<<"No Way!"<<endl;
	  else cout<<c<<endl;
    return 0;
}
```
```
#include<iostream>
#include<queue>
using namespace std;
struct Pos
{
    int x,y;
}; //坐标点定义
queue <Pos> q;
int n,m,x,y,tx,ty,dis[1001][1001],s_a,s_b,t_a,t_b;
const int dx[]={1,-1,0,0};
const int dy[]={0,0,1,-1};
char mp[1001][1001];
bool vis[1001][1001]; //方向等变量的定义
int bfs(int sx,int sy)
{
    q.push((Pos){sx,sy});
    vis[sx][sy]=true;
    while(!q.empty())
    {
        x=q.front().x;
        y=q.front().y; 
        q.pop();  //弹出队列
        if(mp[x][y]=='m') return dis[x][y];
        for(int i=0;i<4;i++)
        {
            tx=x+dx[i];
            ty=y+dy[i];
            if(tx<=0||tx>n||ty<=0||ty>m) continue;
            if(mp[tx][ty]=='#'||vis[tx][ty]==true) continue; //不符合条件，跳过
            dis[tx][ty]=dis[x][y]+1;
            vis[tx][ty]=true;
            q.push((Pos){tx,ty});
        }
    }
    return -1;
}
int main()
{
    cin>>n>>m;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
        {
        	cin>>mp[i][j];
        	if(mp[i][j]=='d')
        	{
        		s_a=i;
        		s_b=j; //获取起点坐标
			}
		}
    int c;
    c=bfs(s_a,s_b);
    if(c==-1)cout<<"No Way!"<<endl;
	else cout<<c<<endl; //这里可以压缩一下 
    return 0;
}
```
