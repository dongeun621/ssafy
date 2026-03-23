// 1. 콜백함수
function main(value) {
  value();
}
function sub() {
  console.log("sub");
}
main(sub);

main(() => {
  console.log("sub");
});

// 2. 콜백함수의 활용
function repeat(count) {
  for (let idx = 1; idx <= count; idx++) {
    console.log(idx);
  }
}

repeat(5);

function repeat_1(count, callback) {
  for (let idx = 1; idx <= count; idx++) {
    callback(idx);
  }
}

repeat_1(idx, function (idx) {
  console.log(idx);
});

repeat_1(idx, function (idx) {
  console.log(idx * 2);
});
