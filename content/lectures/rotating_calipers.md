+++
title = "Rotating Calipers"
date = 2023-04-07
draft = false
weight = 2
+++

```c++ { linenos=true, linenostart=1 }
function dist(p1,p2,p) {

  var A = p.x - p1.x;
  var B = p.y - p1.y;
  var C = p2.x - p1.x;
  var D = p2.y - p1.y;

  var dot = A * C + B * D;
  var len_sq = C * C + D * D;
  var param = -1;
  if (len_sq != 0) //in case of 0 length line
      param = dot / len_sq;

  var xx, yy;

  if (param < 0) {
    xx = p1.x;
    yy = p1.y;
  }
  else if (param > 1) {
    xx = p1.x;
    yy = p1.y;
  }
  else {
    xx = p1.x + param * C;
    yy = p1.y + param * D;
  }

  var dx = p.x - xx;
  var dy = p.y - yy;
  return Math.sqrt(dx * dx + dy * dy);
}

// Rotating Calipers Code

vector<point> p;

int n; // number of points

typedef pair<point,point> pp;

set<pp> antipodes;

int k=1;

while (dist(p[n-1],p[0],p[k+1]) > dist(p[n-1],p[1],p[k])
    ++k;

int i=1;
int j=k;

while (i <= k && j < n) {
  antipodes.add(pp(p[i],p[k]));
  while (dist(p[i],p[i+1],p[j+1]) > dist(p[i],p[i+1],p[j]) && j<m) {
     antipodes.add(pp(p[i],p[j]));
     ++j;
  }
  ++i;
}
```
