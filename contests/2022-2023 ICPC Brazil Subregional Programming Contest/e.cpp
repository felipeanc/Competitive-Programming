#include <bits/stdc++.h>

using namespace std;

int main(){
  int n; cin >> n;
  vector<int> flechas(10e6 + 5, 0);
  int ans = 0;

  while(n--){
    int h; cin >> h;
    if(flechas[h]){
      flechas[h]--;
      flechas[h-1]++;
    }
    else{
      ans++;
      flechas[h-1]++;
    }
  }
  cout << ans << endl;
  return 0;
}