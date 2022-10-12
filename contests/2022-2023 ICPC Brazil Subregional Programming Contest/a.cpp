#include <bits/stdc++.h>

using namespace std;

int main(){
  int n; cin >> n;
  string s; cin >> s;

  int ans, tam, flag;
  ans = tam = flag = 0;
  for(char c : s){
    if(c == 'a'){
      tam++;
      flag = 1;
    }
    else{
      if(tam >= 2)
        ans += tam;
      tam = 0;
      flag = 0;
    }
  }
  if(flag) ans += tam;
  cout << ans << endl;
  return 0;
}