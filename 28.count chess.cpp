#include <iostream>
#include <vector>
using namespace std;

void resh(int n, int m)
{
	vector<vector<int>> dp(n+1, vector <int>(m+1,0));
	dp[1][1] = 1;
	for (int i = 2; i < dp.size(); ++i)
	{
		for (int j = 2; j < dp[0].size(); ++j)
		{
			dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j - 2];
		}
	}
	cout << dp[dp.size()-1][dp[0].size()-1];
}
int main()
{
	int n, m;
	cin >> n >> m;
	resh(n, m);
	return 0;
}
