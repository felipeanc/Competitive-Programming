#include <bits/stdc++.h>

using namespace std;

int main(){
  int n, pos, minv, maxv;
  string s;
  pos = minv = maxv = 0;
  cin >> n >> s;
  for(char c : s){
    if(c == 'E'){
      pos -= n;
      minv = min(minv, pos);
    }
    else{
      pos += n;
      maxv = max(maxv, pos);
    }
  }
  cout << (abs(maxv) + abs(minv) >= 360 ? "S" : "N") << endl;
  return 0;
}
