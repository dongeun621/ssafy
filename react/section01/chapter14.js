let a = 1; //전역 스코프

function funcA() {
  let b = 2; // 지역스코프
  console.log(a);
  function funcB() {} //지역스코프. funA안에서만 funB호출가능
}

if (true) {
  let c = 1; // 지역스코프
}

for (let i = 0; i < 10; i++) {
  //i도 지역스코프
  let d = 1; // 지역스코프
}
