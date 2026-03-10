//함수선언

console.log(getArea(10, 20)); //선언이 되기전에 호출돼도 상관없다. 호이스팅이 돼서 함수가 최상단으로 가서 선언됨.

function greeting() {
  console.log("안녕하세요!");
}

greeting();

function getArea(width, height) {
  let area = width * height;

  return area;
}
console.log(getArea(10, 20));
